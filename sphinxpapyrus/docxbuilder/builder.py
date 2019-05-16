# -*- coding: utf-8 -*-
"""
    sphinxpapyrus.docxbuilder.builder
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    docx Sphinx builder.

    :copyright: Copyright 2018 by nakandev.
    :license: MIT, see LICENSE for details.
"""

from os import path

from docutils.io import StringOutput

from sphinx.builders import Builder
from sphinx.util import logging
from sphinx.util.osutil import ensuredir, os_path
from sphinx.util.console import bold, darkgreen
from sphinxpapyrus.docxbuilder.writer import DocxWriter
from sphinxpapyrus.docxbuilder.translator import DocxTranslator

# For type annotation
from docutils import nodes

logger = logging.getLogger(__name__)


def inline_toctrees(builder, doc_names, name, tree, color_func, traversed):
    """Inline all toctrees in the *tree*.

    Record all document names in *doc_names*, and output it with
    *color_func*.

    :param builder: Builder instance
    :type builder: Builder

    :param doc_names: List of document names to include
    :type doc_names: list|set

    :param name: Output document name
    :type name: str

    :param tree: Node tree
    :type tree: Node

    :param color_func: callable colorize function defined in sphinx.util.console
    :param color_func: callable

    :param traversed: list of already traversed nodes to skip duplication
    :type traversed: list of str

    :returns: Node
    """

    from six import text_type
    from docutils import nodes
    from sphinx import addnodes

    tree = tree.deepcopy()
    for node in tree.traverse(addnodes.toctree):
        new_nodes = []
        include_file_list = map(text_type, node['includefiles'])
        for include_file in include_file_list:

            # exclude already traversed files
            if include_file in traversed:
                continue

            try:
                # prevent current file to be included again
                traversed.append(include_file)

                # console output current file path
                logger.info(color_func(include_file) + " ", nonl=1)

                # include subtree
                subtree = inline_toctrees(
                    builder,
                    doc_names,
                    include_file,
                    builder.env.get_doctree(include_file),
                    color_func,
                    traversed
                )
                # remember just traversed file in document names
                doc_names.add(include_file)

            except Exception as exc:
                # low-level log for debug
                logger.debug(
                    "There was an error traversing %s: %s",
                    include_file,
                    exc
                )
                # console notification
                logger.warning(
                    'toctree contains ref to nonexisting file %r',
                    include_file,
                    location=name
                )

            else:
                # no errors while traverse
                # additionally process sections if present
                sof = addnodes.start_of_file(docname=include_file)
                sof.children = subtree.children

                for section_node in sof.traverse(nodes.section):
                    if 'docname' not in section_node:
                        section_node['docname'] = include_file
                new_nodes.append(sof)

        # what happened here?
        node.parent['numbered'] = node['numbered']
        node.parent.replace(node, new_nodes)

    return tree


class DocxBuilder(Builder):
    """
    Builds DOCX from the reST sources.
    """
    name = 'docx'
    format = 'docx'
    out_suffix = '.docx'
    allow_parallel = False
    default_translator_class = DocxTranslator

    current_doc_name = None  # type: str

    def __init__(self, app):
        super(DocxBuilder, self).__init__(app)
        # Link internal docs writer as instance property
        self.writer = None
        self.fig_numbers = None

    def get_outdated_docs(self):
        """Return an iterable of output files that are outdated, or a string
        describing what an update build will build.

        If the builder does not output individual files corresponding to
        source files, return a string here.  If it does, return an
        iterable
        of those files that need to be written.

        :returns Iterator[unicode]
        """
        return 'all documents'

    def get_target_uri(self, doc_name, typ=None):
        """Return the target URI for a document name.

        *typ* can be used to qualify the link characteristic for individual
        builders.

        :param doc_name: Document name
        :type doc_name: str, unicode

        :param typ: Document type
        :type typ: str, unicode

        :returns str
        """
        return ''

    def fix_refuris(self, tree):
        """Fix referenced URIs
        
        :param tree: Node to process
        :type tree: Node
        
        :returns: None
        """
        assert isinstance(tree, nodes.Node)
        # fix refuris with double anchor
        file_name = self.config.master_doc + self.out_suffix
        for node in tree.traverse(nodes.reference):
            if 'refuri' not in node:
                continue
            reference_uri = node['refuri']
            hash_index = reference_uri.find('#')
            if hash_index < 0:
                continue

            hash_index = reference_uri.find('#', hash_index + 1)
            if hash_index >= 0:
                node['refuri'] = file_name + reference_uri[hash_index:]

    def assemble_doctree(self, start=None):
        """Assemble all nodes together"""
        master = start if start else self.config.master_doc
        tree = self.env.get_doctree(master)
        tree = inline_toctrees(
            self, set(), master, tree, darkgreen, [master]
        )
        tree['docname'] = master
        self.env.resolve_references(tree, master, self)
        self.fix_refuris(tree)
        return tree

    def assemble_toc_fignumbers(self):
        """Assemble figure numbers

        Return figure's dict like {
            'foo': {
                'figure': {
                    'id2': (2,),
                    'id1': (1,)
                }
            },
            'bar': {
                'figure': {
                    'id1': (3,)
                }
            }
        }
        """
        new_figure_numbers = {}

        for doc_name, toc_fig_num_list in self.env.toc_fignumbers.items():
            for fig_type, fig_num_list in toc_fig_num_list.items():
                alias = "%s/%s" % (doc_name, fig_type)
                new_figure_numbers.setdefault(alias, {})

                for figure_id, fig_num in fig_num_list.items():
                    new_figure_numbers[alias][figure_id] = fig_num

        return {self.config.master_doc: new_figure_numbers}

    def prepare_writing(self, doc_names):
        """Prepare internals before :meth:`write_doc` is run"""
        if not isinstance(doc_names, dict):
            raise AssertionError(f"Expected dict, got {type(doc_names)}")
        assert all(isinstance(x, str) for x in doc_names)

        self.writer = DocxWriter(self)

    def write(self, *ignored):
        """Actual DOCX writing process"""

        doc_names = self.env.all_docs
        if self.config.docx_documents:
            docx_documents = self.config.docx_documents
        else:
            docx_documents = [(self.config.master_doc, self.config.project,
                              self.config.docx_coreproperties)]

        for entry in docx_documents:
            start, name, coreproperties = entry
            self.config.docx_coreproperties = coreproperties
            logger.info(bold('preparing documents... '), nonl=True)
            self.prepare_writing(doc_names)
            logger.info('done')

            logger.info(bold('assembling single document... '), nonl=True)
            doc_tree = self.assemble_doctree(start)
            self.env.toc_fignumbers = self.assemble_toc_fignumbers()
            logger.info('done')
            self.write_doc([start, name], doc_tree)

    def write_doc(self, doc_parts, tree_node):
        """Actual writing method"""
        assert isinstance(doc_parts, (list, tuple))
        assert 2 == len(doc_parts)
        assert isinstance(tree_node, nodes.Node)

        logger.info(bold('prepare writer'))
        start, name = doc_parts
        self.current_doc_name = start
        self.fig_numbers = self.env.toc_fignumbers.get(start, {})
        destination = StringOutput(encoding='utf-8')
        self.writer.write(tree_node, destination)
        out_filename = path.join(self.outdir, os_path(name) + self.out_suffix)
        ensuredir(path.dirname(out_filename))
        logger.info(f"Saving result into {out_filename}")
        try:
            self.writer.save(out_filename)
        except (IOError, OSError) as err:
            logger.warning("error writing file %s: %s", out_filename, err)
        logger.info('done')

    def finish(self):
        """Finish document"""
        pass
