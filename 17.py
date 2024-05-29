def ln(s):
    return len(''.join(s.split()))

c1_9 = ln("""one two three four five six seven eight nine""")
c10 = ln("ten")
c11_19 = ln("""eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen""")
c20_90 = ln("""twenty thirty forty fifty sixty seventy eighty ninety""")
cand = ln("and")
chun = ln("hundred")

c1_99 = 9 * c1_9 + c10 + c11_19 + 10 * c20_90
c1_999 = 100 * c1_9 + 900 * chun + 9 * 99 * cand + 10 * c1_99
c1000 = ln("one thousand")
print(c1_999 + c1000)
