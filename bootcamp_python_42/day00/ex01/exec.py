import sys

i = 0
merge = sys.argv[1]
for i in sys.argv[2:]:
    merge = merge + ' ' + i
case = merge.swapcase()
print(case[::-1])
