import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

IS_FLAT = 1
IS_HILLY = 2
IS_FOREST = 3
IS_CAVE = 4
# plt.style.use('seaborn-deep')

typelist = [IS_FLAT, IS_HILLY, IS_FOREST, IS_CAVE]
dataRule1 = pd.read_csv("Rule1Moving.csv")
dataRule2 = pd.read_csv("Rule2Moving.csv")

Rule1mean = []
Rule2mean = []

for t in typelist:
    typedf1 = dataRule1.loc[dataRule1["Type"] == t]
    print(len(typedf1))
    Rule1mean.append(typedf1["NumberOfSteps"].mean())
    print(Rule1mean)
    typedf2 = dataRule2.loc[dataRule2["Type"] == t]
    Rule2mean.append(typedf2["NumberOfSteps"].mean())
    print(Rule2mean)

objects=('Flat','Hilly','Forest','Cave')
x = np.arange(len(objects))
plt.bar(x, Rule1mean, align='center', alpha=0.5)
plt.xticks(x,objects)
plt.show()
