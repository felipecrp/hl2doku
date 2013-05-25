'''
Created on Feb 17, 2013

@author: felipecrp
'''

import re
import sys


def hl2doku(content):
    content = re.sub("^'''(.*)'''<br>\n", "====== \\1 ======\n", content)
    content = re.sub("\n----\n'''(.*)'''<br>\n----\n", "\n\n===== \\1 =====\n\n", content)
    content = re.sub("'''", "**", content)
    content = re.sub("<br>", " \\\\\\\\", content)
    content = re.sub("\n----\n", "\n\n===== Background =====\n\n", content, 1)

    # Rearrange Skill Section
    content = re.sub("\n\*\*Skills \*\*(([A-Za-z ]+( \([A-Za-z0-9 ]+\))? [+-][0-9]+)( \([A-Za-z0-9-+, ]+\))?), ", "\n**Skills**\n\n  * \\1\n", content)
    content = re.sub("\*\* Modifiers \*\*", "  * **Modifiers: **", content)
    while re.search("\n(([A-Za-z ]+( \([A-Za-z0-9 ]+\))? [+-][0-9]+)( \([A-Za-z0-9-+, ]+\))?)(, )?", content):
        content = re.sub("\n(([A-Za-z ]+( \([A-Za-z0-9 ]+\))? [+-][0-9]+)( \([A-Za-z0-9-+, ]+\))?)(, )?", "\n  * \\1\n", content)
    content = re.sub(" \\\\\\\\\n\*\*Languages \*\*", "\n\n**Languages** ", content)

    return content


content = sys.stdin.read()
content = hl2doku(content)
print content


