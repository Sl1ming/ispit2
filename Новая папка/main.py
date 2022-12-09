with open("file.txt", "r") as f:
    data = f.readlines()
arr = []
k = 0
h = 0
for i1, i in enumerate(data):
    if i == '\n':
        arr.append([])
        for j in range(h,i1):
            arr[k].append(data[j])
        h = i1
        k += 1
a = input("Введіть ваше слово -> ")
m = []
for i1, i in enumerate(arr):
    for j in i:
        if a in j:
            m.append(i1)
            break
if len(m) != 0:
    for j in m:
        for i in arr[j]:
            print(i)
else:
    print("помилка")
















