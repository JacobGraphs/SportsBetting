import numpy as np
import pandas as pd

f = open('/kaggle/input/betfair-sports/betfair_140901.csv', 'r')
T = f.read().split('\n')
f.close()
headers = T[0].split(',')
bug_lines = []
for t in T:
    c = t.count(',')
    if c > 16:
        bug_lines.append(t)
        print('--------------')
        print(t)
        print('--------------')
        for i in range(len(headers)):
            print(headers[i]+' : '+t.split(',')[i])
        print(t.split(',')[16:])
for bl in bug_lines:
    T.remove(bl)

f = open('fixed_betfair_dataset.csv', 'w')
f.write('')
f.close()
f = open('fixed_betfair_dataset.csv', 'a')
for t in T:
    f.write(t + '\n')
f.close()

