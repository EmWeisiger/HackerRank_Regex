
# HackerRank_Regex > Character Class > Excluding Specific Characters

Regex_Pattern = r'^[^1234567890][^aeiou][^bcDF][^\r\n\t\f<space>][^AEIOU][^.,]$'

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())

# Does not work in test case #5 currently. 
