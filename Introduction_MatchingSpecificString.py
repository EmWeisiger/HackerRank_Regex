# HackerRank_Regex > Introduction Challenges > Matching Specific String

Regex_Pattern = r'hackerrank'

import re

Test_String = raw_input()

match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)
