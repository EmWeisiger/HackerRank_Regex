# HackerRank_Regex > Repetitions > Matching Zero Or More Repetitions

Regex_Pattern = r'^\d\d+[a-z]*[A-Z]*$'

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
