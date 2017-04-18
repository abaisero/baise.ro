from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re


class CommentPreprocessor(Preprocessor):
    """ Abbreviation Preprocessor - parse text for abbr references. """

    regex = re.compile(';;.*')

    def run(self, lines):
        '''
        Find and remove all Abbreviation references from the text.
        Each reference is set as a new AbbrPattern in the markdown instance.

        '''
        return [self.regex.sub('', line) for line in lines]


class CommentExtension(Extension):
    """ Comment Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        """ Insert AbbrPreprocessor before ReferencePreprocessor. """
        # md.preprocessors.add('comment', CommentPreprocessor(md), '<reference')
        md.preprocessors.add('comment', CommentPreprocessor(md), '_begin')
        md.registerExtension(self)


def makeExtension(*args, **kwargs):
    return CommentExtension(*args, **kwargs)
