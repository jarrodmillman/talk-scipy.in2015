import numpy as np
import matplotlib.pyplot as plt

x = np.recfromcsv("majors.csv")
years = np.asarray(x['year'])
years[1::2] = '""'
years = [y[1:-1] for y in list(years)]
majors = x['count']

y = np.recfromcsv("stat133enroll.csv")
stat133 = y['count']

index = np.arange(len(years))
bar_width = 0.35
opacity = 0.7

plt.bar(index, stat133, bar_width, alpha=opacity, color='b', label='Stat 133 enrollment')
plt.bar(index + bar_width, majors, bar_width, alpha=opacity, color='r', label='Undergraduate majors')
plt.xticks(index + bar_width, years, size='small')
plt.xlabel("Academic year")
plt.ylabel("Number of students")
plt.legend(loc="best")
plt.show()

