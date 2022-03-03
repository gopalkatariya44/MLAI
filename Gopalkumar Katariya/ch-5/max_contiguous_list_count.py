ls =[0,8,4,12,2,12,4,9,1,3,5,13,1,3,5,13,2,4,6,8,3]

lst1 = []
lst2 = [lst1]

for i in range(len(ls)):

    if len(lst1) == 0:
        lst2[i].append(ls[i])

    elif lst2[-1][-1] <= ls[i]:
        lst2[-1].append(ls[i])

    else:
        lst2.append([ls[i]])

print(lst2)

temp_list = max(lst2, key = len)
for i in lst2:
    if len(i) == len(temp_list):
        print(i)
