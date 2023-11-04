import random

# card=random.randint(100)
card_mix = []

barrels = [i for i in range(91)]
random.shuffle(barrels)

print(barrels)
# line1 = barrels[:10]
# line2 = barrels[10:20]
# line3 = barrels[20:30]
#
# print(line1)
# print(line2)
# print(line3)
numbers1_10 = []
numbers11_20 = []
numbers21_30 = []
numbers31_40 = []
numbers41_50 = []
numbers51_60 = []
numbers61_70 = []
numbers71_80 = []
numbers81_90 = []

new_barrels=[]

for i in barrels:
    # print(barrels[i])
    if 1 < barrels[i]<= 10:
        numbers1_10.append(barrels[i])
new_barrels.append(numbers1_10)

for i in barrels:
    # print(barrels[i])
    if 10 < barrels[i]<= 20:
        numbers11_20.append(barrels[i])
new_barrels.append(numbers11_20)


for i in barrels:
    # print(barrels[i])
    if 20 < barrels[i]<= 30:
        numbers21_30.append(barrels[i])
new_barrels.append(numbers21_30)

for i in barrels:
    # print(barrels[i])
    if 30 < barrels[i]<= 40:
        numbers31_40.append(barrels[i])
new_barrels.append(numbers31_40)

for i in barrels:
    # print(barrels[i])
    if 40 < barrels[i]<= 50:
        numbers41_50.append(barrels[i])
new_barrels.append(numbers41_50)

for i in barrels:
    # print(barrels[i])
    if 50 < barrels[i]<= 60:
        numbers51_60.append(barrels[i])
new_barrels.append(numbers51_60)

for i in barrels:
    # print(barrels[i])
    if 60 < barrels[i]<= 70:
        numbers61_70.append(barrels[i])
new_barrels.append(numbers61_70)

for i in barrels:
    # print(barrels[i])
    if 70 < barrels[i]<= 80:
        numbers71_80.append(barrels[i])
new_barrels.append(numbers71_80)

for i in barrels:
    # print(barrels[i])
    if 80 < barrels[i]<= 90:
        numbers81_90.append(barrels[i])
new_barrels.append(numbers81_90)


for n in numbers1_10:
    print(n)
print(numbers1_10)
print(numbers11_20)
print(numbers21_30)
print(numbers31_40)
print(numbers41_50)
print(numbers51_60)
print(numbers61_70)
print(numbers71_80)
print(numbers81_90)

x=[i for i in range(9)]
random.shuffle(x)
print(x)
x1=x[:5]
print(x1[0])
random.shuffle(x)
print(x)
x2=x[:5]
random.shuffle(x)
print(x)
x3=x[:5]
print(x1)
line1=[]
line2=[]
line3=[]
print(new_barrels)
random.shuffle(new_barrels)
print(new_barrels)
print()
for i in range(5):
    line1.append(new_barrels[x1[i]][0])
for i in range(5):
    line2.append(new_barrels[x2[i]][1])
for i in range(5):
    line3.append(new_barrels[x3[i]][2])

print(line1)
print(line2)
print(line3)





