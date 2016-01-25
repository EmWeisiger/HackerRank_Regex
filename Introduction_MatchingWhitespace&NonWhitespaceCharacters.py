# HackerRank_Regex > Introduction Challenges > Matching Whitespace & Non-Whitespace Character

Regex_Pattern = r"\S{2}\s{1}\S{2}\s{1}\S{2}"

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
