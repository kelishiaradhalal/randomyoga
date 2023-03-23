import pandas as pd
import random
from datetime import datetime

df = pd.read_csv('poses.csv', delimiter=',')
random.seed(datetime.now().timestamp())

noAsanas = int(input("Enter number of asanas you'd like practice: "))

for _ in range(noAsanas):
 value = random.randint(0, len(df))
 print(df['Asana'][value])




