word = (input("Введите слово: "))
length = len(word)
middle_index = length // 2
if length % 2 == 0:
    result = word[middle_index -1] + word[middle_index]
else: 
    result = word[middle_index]

print("Результат: ", result)
 
