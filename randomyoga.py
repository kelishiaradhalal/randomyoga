import pandas as pd
from random import seed
from random import randint

df = pd.read_csv('poses.csv', delimiter=',')
seed(1)

noAsanas = int(input("Enter number of asanas you'd like practice: "))

for _ in range(noAsanas):
 value = randint(0, len(df))
 print(df['Asana'][value])




