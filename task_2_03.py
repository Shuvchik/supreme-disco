# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# -Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

IntNumberSeries = int(input("Введите целое число: "))
SummerList_IntNumberSeries=0
for i in range(1,IntNumberSeries+1):
     List_IntNumberSeries = round(((1+1/i)**i),2)
     print (List_IntNumberSeries)
     SummerList_IntNumberSeries=SummerList_IntNumberSeries +List_IntNumberSeries
print ("Сумма всех чисел ряда равна: ",SummerList_IntNumberSeries)