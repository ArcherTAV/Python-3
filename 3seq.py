inputList = input("Введите элементы 1-ого списка через запятую:")
set1 = {int(i) for i in inputList.split(',')}
inputList = input("Введите элементы 2-ого списка через запятую:")
set2 = {int(i) for i in inputList.split(',')}

shortList=set1-set2
print("Результат:"+",".join(map(str, shortList)))