from markdown.util import etree, AtomicString
from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor


class HaikuProcessor(BlockProcessor):

    def test(self, parent, block):
        lines = block.split('\n')
        return len(lines) == 4 and lines[0].strip() == '.haiku'

    def run(self, parent, blocks):
        block = blocks.pop(0)
        lines = block.split('\n')[1:]

        div = etree.SubElement(parent, 'div')
        div.set('class', 'haiku')
        for i, line in enumerate(lines):
            p = etree.SubElement(div, 'p')
            p.text = AtomicString(line)


class HaikuExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        # print md.parser.blockprocessors
        md.parser.blockprocessors.add(
            'haiku',
            HaikuProcessor(md.parser),
            # '_begin'
            '<paragraph'
            # '_end'
        )
        md.registerExtension(self)


def makeExtension(*args, **kwargs):
    return HaikuExtension(*args, **kwargs)
