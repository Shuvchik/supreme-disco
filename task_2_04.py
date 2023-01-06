#Реализуйте алгоритм перемешивания списка.

import random
ListExample = list(range(1,10))
print ("Первоначальный список ", ListExample, end=" ")
print ("\nПеремешанный список ",random.sample(ListExample, k=len(ListExample)) ,end=" ")