
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import random
a = (random.randint(3, 9))

# creating the dataset
list = []
list.insert(0, 1)
list.insert(1, 2)
list.insert(2, 3)
list.insert(3, 4)
list.insert(4, 5)
list.insert(5, 6)
list.insert(6, 7)
list.insert(7, 8)
list.insert(8, 9)
list.insert(9, 10)
list.insert(10, 11)
list.insert(11, 12)
list.insert(12, 13)
list.insert(13, 14)
list.insert(14, 15)
list.insert(15, 'YES')


print(list)
import csv
i = 400
header = ['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS','ANXIETY','PEER_PRESSURE','CHRONIC DISEASE','FATIGUE','ALLERGY','WHEEZING','ALCOHOL CONSUMING','COUGHING','SHORTNESS OF BREATH','SWALLOWING DIFFICULTY','CHEST PAIN','LUNG_CANCER']
with open('totals.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    while i>0:

    # write the data
        writer.writerow(list)
        i = i - 1

dataset = pd.read_csv("total.csv")