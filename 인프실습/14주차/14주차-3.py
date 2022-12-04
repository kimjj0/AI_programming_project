import numpy as np

a = np.array([[183, 83], [168, 57], [158, 68], [163, 45], [190, 81], [172, 90]])
height = a.T[0]
weight = a.T[1]

standard_weight = []
fat_rate = []
obesity_mask = []
obesity_mask_result = []

for i in range(6):
    standard_weight.append((height[i] * 0.01) ** 2 * 22)
    fat_rate.append(((weight[i] - standard_weight[i]) / standard_weight[i]) * 100)
    if fat_rate[i] >= 20:
        obesity_mask.append('True')
        obesity_mask_result.append(round(fat_rate[i], 8))
    else:
        obesity_mask.append('False')

print("+-10% : 정상")
print("10~10% : 체중 과다")
print("20% 이상 : 비만\n")
print(a, "\n")
print(obesity_mask)
print("obesity masking result : ", obesity_mask_result,"\n")
print("********************************************")
print("n번 사람   키   몸무게   표준체중   비만도   비만유무")
print("********************************************")
for i in range(6):
    print(f'{i + 1}번 사람: {height[i]}cm {weight[i]}kg, {standard_weight[i] : .4f}, {fat_rate[i] : .4f}, {obesity_mask[i]}')
print("********************************************")

