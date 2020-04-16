import datetime
tup = (3, 30, 2019, 9, 25)
time = datetime.datetime(tup[2], tup[3], tup[4], tup[0], tup[1], 0)
print('{:%m/%d/%Y %H:%M}'.format(time))
