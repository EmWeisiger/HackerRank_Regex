# HackerRank_Regex > Repetitions > Matching {x} Repetitions

Regex_Pattern = r'^[a-zA-Z24680]{40}[13579\s]{5}$'

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
