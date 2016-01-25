
# HackerRank_Regex > Introduction Challenges > Matching Start & End

Regex_Pattern = r"^\d\w{4}\.$"

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
