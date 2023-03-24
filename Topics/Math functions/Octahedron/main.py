import math
num = int(input())

area = (math.sqrt(3) * 2 * pow(num, 2))
volume = (1/3 * math.sqrt(2) * pow(num, 3))

print(str(round(area, 2)) + " " + str(round(volume, 2)))
