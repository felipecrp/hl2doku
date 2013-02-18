'''
Created on Feb 17, 2013

@author: felipecrp
'''

import re
import sys


def hl2doku(content):
    #part = re.split("----", content)
    #print part
    
    content = re.sub("^'''(.*)'''<br/>\n", "====== \\1 ======\n", content)
    content = re.sub("\n----\n'''(.*)'''<br/>\n----\n", "\n\n===== \\1 =====\n\n", content)
    content = re.sub("'''", "**", content)
    content = re.sub("<br\/>", " \\\\\\\\", content)
    content = re.sub("\n----\n", "\n\n===== Background =====\n\n", content, 1)
    
    return content


content = sys.stdin.read()
content = hl2doku(content)
print content

