# HackerRank_Regex > Repetitions > Matching One Or More Repetitions

Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
