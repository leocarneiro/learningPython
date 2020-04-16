import sys

n = 0
for i in sys.argv:
    n += 1
if n > 2:
    print('ERROR')
    exit()
if n == 1:
    exit()
arg = sys.argv[1]
if not arg.isdigit:
    print('ERROR')
    exit()
else:
    x = int(arg)
    if x == 0:
        print('I\'m Zero')
    elif x % 2 == 0:
        print('I\'m Even.')
    else:
        print('I\'m Odd.')
