import numpy as np
import matplotlib.pyplot as plt
array_bone = np.array(
    [[2018, 1253, 1001],
     [2019, 1611, 1532],
     [2020, 1119, 1351],
     [2021, 1849, 1773]])
year = array_bone.T[0]
boys = array_bone.T[1]
girls = array_bone.T[2]
avg = (boys + girls) // 2
plt.plot(year, boys, 'b--D')
plt.plot(year, girls, 'r--o')
plt.plot(year, avg, 'g--^')
plt.xlabel('Years')
plt.ylabel('Boys and Girls')
plt.legend(["boys", "girls", "mean"])
plt.title("Born")
plt.show()
