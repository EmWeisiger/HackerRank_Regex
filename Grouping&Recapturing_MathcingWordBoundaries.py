# HackerRank_Regex > Grouping and Recapturing > Matching Word Boundaries

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
