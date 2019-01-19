from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
import cgi


class MathJaxPattern(Pattern):
    def __init__(self, md):
        super().__init__(r'(?<!\\)(\$\$?)(.+?)\2', md)

    def handleMatch(self, m):
        # Pass the math code through, unmodified except for basic entity substitutions.
        # Stored in htmlStash so it doesn't get further processed by Markdown.
        text = cgi.escape(m.group(2) + m.group(3) + m.group(2))
        return self.markdown.htmlStash.store(text)


class MathJaxExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        # Needs to come before escape matching because \ is pretty important in LaTeX
        md.inlinePatterns.add('mathjax', MathJaxPattern(md), '<escape')
        md.parser.blockprocessors.add('mathjax', MathJaxBlock(md.parser), '_begin')


# def makeExtension(configs=[]):
#     return MathJaxExtension(configs)
def makeExtension(*args, **kwargs):
    return MathJaxExtension(*args, **kwargs)
