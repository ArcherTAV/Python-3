inputList = input("Введите элементы списка через запятую:")
split_char = ',' if inputList.__contains__(',') else ';' if inputList.__contains__(';') else '/'
lst = [int(i) for i in inputList.split(split_char)]
shortList=list(set(lst))
print("Результат:"+",".join(map(str, shortList)))