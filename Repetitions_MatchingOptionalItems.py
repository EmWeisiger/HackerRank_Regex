# HackerRank_Regex > Repetitions > Matching Optional Items

Regex_Pattern = r'^[a-zA-Z]*s$'

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
