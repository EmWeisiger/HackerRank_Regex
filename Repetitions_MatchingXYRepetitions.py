# HackerRank_Regex > Repetitions > Matching {x, y} Repetitions

Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
