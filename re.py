hand = open('code.txt')
for line in hand:
    line = line.rstrip()
    if line.find('^From:') >= 0:
        print(line)

import re

hand = open('code.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)