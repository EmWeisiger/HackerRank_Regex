# HackerRank_Regex > Introduction Challenges > Matching Anything But a Newline

Regex_Pattern = r".{3}\..{3}\..{3}\..{3}"

import re
import sys
Test_String = sys.stdin.read()

match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)
