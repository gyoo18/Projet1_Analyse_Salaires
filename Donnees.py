import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("StudentPerformanceFactors.csv")



names = df.columns
print(names)

notes = df["Exam_Score"]
heures = df["Hours_Studied"]

plt.scatter(notes,heures)

m,b = np.polyfit(notes,heures,1)


plt.plot(notes,m*notes +b)

plt.show()

print(m,b)

