from numpy import genfromtxt

df = genfromtext('poses.csv', delimiter=',', skip_header=1, usecols=[0])

print(df)
