from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re

import json
import IPython

ansi_escape = re.compile(r'\x1b[^m]*m')


def strip_colors(string):
    return ansi_escape.sub('', string)


class IPynbPreprocessor(Preprocessor):
    """ Abbreviation Preprocessor - parse text for abbr references. """

    regex = re.compile('^\s*\.ipynb\s*(?P<fname>\S+)\s*$')

    def run(self, lines):
        '''
        Find and remove all Abbreviation references from the text.
        Each reference is set as a new AbbrPattern in the markdown instance.

        '''
        print 'LINES'
        print lines
        print 'END_LINES'
        new_lines = []
        for line in lines:
            match = self.regex.match(line)
            if match:
                fname = match.group('fname')
                line = self.ipynb_line(fname)
            new_lines.extend(line.split('\n'))
        print 'NEW_LINES'
        print new_lines
        print 'END_NEW_LINED'
        return new_lines

    def ipynb_line(self, fname):
        lines = str()
        fname = 'app/static/ipynb/{}'.format(fname)
        with open(fname) as f:
            notebook = json.load(f)

        cells = notebook['worksheets'][0]['cells']

        for cell in cells:
            if cell['cell_type'] == 'markdown':
                lines += ''.join(cell['source'])
                lines += '\n'
            elif cell['cell_type'] == 'code':
                lines += '~~~.python\n'
                lines += ''.join(cell['input'])
                lines += '\n'
                lines += '~~~\n'

                try:
                    assert all(o['output_type'] in ('stream', 'pyout', 'pyerr') for o in cell['outputs'])
                except AssertionError:
                    IPython.embed()

                for output in cell['outputs']:
                    if output['output_type'] in ('pyout', 'stream'):
                        lines += '~~~.python\n'
                        lines += ''.join(output['text'])
                        # lines += '\n'
                        lines += '~~~\n'
                    elif output['output_type'] == 'pyerr':
                        lines += '\n'.join(strip_colors(o) for o in output['traceback'])
                    else:
                        IPython.embed()
        return lines


class IPynbExtension(Extension):
    """ IPynb Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        """ Insert AbbrPreprocessor before ReferencePreprocessor. """
        # md.preprocessors.add('ipynb', IPynbPreprocessor(md), '<reference')
        md.preprocessors.add('ipynb', IPynbPreprocessor(md), '_begin')
        md.registerExtension(self)


def makeExtension(*args, **kwargs):
    return IPynbExtension(*args, **kwargs)
