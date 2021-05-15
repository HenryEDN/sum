from sys import exit

print("\n\tСложение чисел\n")

num1 = ",".join(input("Введите первое число: ")).split(',') #Получаем от пользователя 1-е число
num2 = ",".join(input("Введите второе число: ")).split(',') #Получаем от пользователя 2-е число
result = []  #Результат сложения
give = 0  #Флажок для того чтобы определить нужно ли добавлять 1-цу в следующий разряд


#Добавляем числу недостающие разряды.
if len(num1) > len(num2): #Если разрядность 1-го числа больше 2-го, то добавляем 2-му числу недостающие разряды
    for i in range(len(num1) - len(num2)):
        num2.insert(0,'0')
else:
    for i in range(len(num2) - len(num1)):
        num1.insert(0,'0')


#Сложение
try:
    for i in range(len(num1),0,-1):
        a = num1[int(i)-1]
        b = num2[int(i)-1]

        if (int(a) == 0 and int(b) == 0): #Если числа равны 0, то добавляем 0 в result
            result.insert(0, '0')
        elif(int(a)+int(b))<=9: #Если сумма чисел < или = 9, то добавляем результат вычисления в result
            result.insert(0, str(int(a)+int(b)))
            if give == 1:
                result[0] = str(int(result[0]) + 1)
                if int(result[0])>9: #Если после добавления единицы в этот разряд число стало больше 9, то вычитаем 10 и добавляем 1 в след. разряд
                    result[0] = str(int(result[0]) - 10)
                else:
                    give = 0
        elif(int(a)+int(b))>9: #Если сумма чисел > 10, то вычитаем 10 и добавляем 1 в след. разряд
            result.insert(0, str((int(a)+int(b))-10))
            if give == 1:
                result[0] = str(int(result[0]) + 1)
            give = 1 

    

except ValueError:
        print("\nВы должны вводить только целые числа!")
        input("Нажмите Enter, чтобы выйти")
        exit()
    

if give == 1: 
    result.insert(0,"1")


print(f"\n********************************\n\tРезультат = {''.join(result)}\n********************************")



