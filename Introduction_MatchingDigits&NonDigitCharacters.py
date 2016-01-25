# HackerRank_Regex > Introduction Challenges > Matching Digits & Non-Digit Characters

Regex_Pattern = r"^\d{2}\D\d{2}\D\d{4}"

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())
