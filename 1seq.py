count = int(input("Количество элементов:"))
lst = list()
for i in range(1,count+1):
    lst.append(int(input(f"Введите {i} элемент:")))
lst.sort()
print(lst)