#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function

import functools
import json
import os
import re
import sys

import IPython

def main():
    if len(sys.argv) != 2:
        print("Usage: {} filename.ipynb".format(sys.argv[0]))
        return 1

    filename = sys.argv[1]
    notebook = json.load(open(filename))
    write = print

    cells = notebook['worksheets'][0]['cells']

    muhammad_id = 0

    for cell in cells:
        if cell['cell_type'] == 'markdown':
            # Easy
            write(''.join(cell['source']))
        elif cell['cell_type'] == 'code':
            # Can't use ``` or any shortcuts as markdown fails for some code
            prompt_number = cell['prompt_number'] if 'prompt_number' in cell.keys() else ' '

            muhammad = "mhd_{}".format(muhammad_id)
            muhammad_id += 1

            write("{{% mountain {} %}}".format(muhammad))
            write("In [{}]:".format(prompt_number))
            write("{% endmountain %}")
            write("{{% muhammad {} %}}".format(muhammad))

            write("{% highlight python %}")
            write(''.join(cell['input']))
            write("{% endhighlight %}")

            try:
                assert all(o['output_type'] in ('stream', 'pyout', 'pyerr')
                           for o in cell['outputs'])
            except AssertionError as e:
                print(e)
                IPython.embed()

            for output in cell['outputs']:
                if output['output_type'] == 'pyout' or output['output_type'] == 'stream':
                    muhammad = "mhd_{}".format(muhammad_id)
                    muhammad_id += 1

                    write("{{% mountain {} %}}".format(muhammad))
                    write("Out [{}]:".format(prompt_number))
                    write("{% endmountain %}")
                    write("{{% muhammad {} %}}".format(muhammad))

                    write("{% highlight python %}")
                    write(''.join(output['text']))
                    write("{% endhighlight %}")
                elif output['output_type'] == 'pyerr':
                    write('\n'.join(strip_colors(o) for o in output['traceback']))
                else:
                    print(output)
                    IPython.embed()

        write("")

ansi_escape = re.compile(r'\x1b[^m]*m')


def strip_colors(string):
    return ansi_escape.sub('', string)


if __name__ == '__main__':
    main()

