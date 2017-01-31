from flask import url_for
from flask_flatpages.utils import pygmented_markdown

import re
import json
import IPython


ansi_escape = re.compile(r'\x1b[^m]*m')


def strip_colors(string):
    return ansi_escape.sub('', string)


def notebook_renderer(text, pages, page):
    fname = './app/static/notebooks/{}.ipynb'.format(page.path)
    with open(fname) as f:
        notebook = json.load(f)

    cells = notebook['worksheets'][0]['cells']
    muhammad_id = 0

    text += '(Download this IPython Notebook <a href="{}">here</a>.)'.format(
        url_for('static', filename='notebooks/{}.ipynb'.format(page.path))
    )
    text += '\n\n'

    for cell in cells:
        if cell['cell_type'] == 'markdown':
            text += ''.join(cell['source'])
            text += '\n'
        elif cell['cell_type'] == 'code':
            prompt_number = cell['prompt_number'] if 'prompt_number' in cell else ' '

            muhammad = 'mhd_{}'.format(muhammad_id)
            muhammad_id += 1

            text += '\n\n'
            text += '<div class="mountain ipyprompt ipycode" mhd="{}">In [{}]:</div>'.format(muhammad, prompt_number)
            text += '\n\n'
            text += '<span class="muhammad" id="{}"></span>'.format(muhammad)
            text += '\n\n'
            text += '~~~.python\n'
            text += ''.join(cell['input'])
            text += '\n'
            text += '~~~\n'

            try:
                assert all(o['output_type'] in ('stream', 'pyout', 'pyerr') for o in cell['outputs'])
            except AssertionError:
                IPython.embed()

            for output in cell['outputs']:
                if output['output_type'] in ('pyout', 'stream'):
                    muhammad = 'mhd_{}'.format(muhammad_id)
                    muhammad_id += 1

                    text += '\n\n'
                    text += '<div class="mountain ipyprompt ipyoutput" mhd="{}">Out[{}]:</div>'.format(muhammad, prompt_number)
                    text += '\n\n'
                    text += '<span class="muhammad" id="{}"></span>'.format(muhammad)
                    text += '\n\n'
                    text += '~~~.python\n'
                    text += ''.join(output['text'])
                    text += '~~~\n'
                elif output['output_type'] == 'pyerr':
                    text += '\n'.join(strip_colors(o) for o in output['traceback'])
                else:
                    IPython.embed()

    return pygmented_markdown(text, pages)
