
print("\t\nВычитание чисел\n")

#Ввод чисел

num1 = ",".join(input("Enter first number: ")).split(",") #1-е число
num2 = ",".join(input("Enter second number: ")).split(",") #2-е число
result = [] #Результат
status = 0
numbers = [i for i in range(1, 10)]

#Проверка разрядности чисел и добавление нулей для тех чисел, у которых разрядность меньше

if len(num1) > len(num2):
    for i in range(len(num1)-len(num2)):
        num2.insert(0, "0")
        
else:
    for i in range(len(num2)-len(num1)):
        num1.insert(0, "0")    


#Вычитание числел

#Если 1 число > 2 числа
try:
    if (int(''.join(num1)) >= int(''.join(num2))):
        for i in range(len(num1),0,-1):
                count = i-1
                if(int(num1[count]) >= int(num2[count])):
                    result.insert(0, str(int(num1[count]) - int(num2[count])))
                    if (status == 1):
                        result[0] = str(int(result[0]) - 1) 
                        status = 0
                else:
                    result.insert(0, str((int(num1[count]) + 10) - int(num2[count])))
                    if (status == 1):
                        result[0] = str(int(result[0]) - 1) 
                        status = 0
                    status = 1
        for i in result:
            if i != '0':
                break
            else:
                result.remove(i)
    #Если 2 число > 1 числа
    else:
        for i in range(len(num1),0,-1):
                count = i-1
                if (int(num1[count]) == int(num2[count]) ):
                    result.insert(0,'0')
                    if (status == 1):
                        if int(result[0]) < 1:    
                            result[0] = str((int(result[0])+10) - 1) 
                            status = 1
                        else:
                            result[0] = str(int(result[0]) - 1) 
                            status = 0
                elif(int(num1[count]) >= int(num2[count])):
                    result.insert(0, str(int(num2[count]) - (int(num1[count]) - 10)))
                    if (status == 1):
                        if int(result[0]) < 1:    
                            result[0] = str((int(result[0])+10) - 1) 
                            status = 1
                        else:
                            result[0] = str(int(result[0]) - 1) 
                            status = 0
                    status = 1
                elif(int(num1[count]) <= int(num2[count])):
                    result.insert(0, str(int(num2[count]) - int(num1[count])))
                    if (status == 1):
                        if int(result[0]) < 1:    
                            result[0] = str((int(result[0])+10) - 1) 
                            status = 1
                        else:
                            result[0] = str(int(result[0]) - 1) 
                            status = 0
        result.insert(0, '-')
        for i in result[1:len(result)-1]:
            if i != '0':
                break
            else:
                result.remove(i)
except ValueError:
    print("\nВы должны вводить только целые числа!")
    input("Нажмите Enter, чтобы выйти")
    exit()
    

print(f"\n********************************\n\tResult = {''.join(result)}\n********************************")