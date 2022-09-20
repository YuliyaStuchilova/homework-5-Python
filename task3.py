# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('test1.txt', 'r', encoding='UTF-8') as file:
    coding = file.read()

count = 1
stroka = ''
for i in range(len(coding)-1):
    if coding[i] == coding[i+1]:
        count += 1
    else:
        stroka = stroka+str(count)+coding[i]
        count = 1
    
stroka = stroka + str(count) + coding[-1]

print(stroka)

with open('test2.txt', 'r', encoding='UTF-8') as file2:
    decod = file2.read()

stroka_decod = ''
count2 = ''
for i in range(len(decod)):
    if decod[i].isdigit():
        count2 += decod[i]
    else:
        stroka_decod = stroka_decod+int(count2)*decod[i]
        count2 = ''
    

print(stroka_decod)

