import datetime
n = str(datetime.datetime.today())
s = "{0}-{1}-{2}".format(n[0:4],n[5:7],n[8:10])
print(s)