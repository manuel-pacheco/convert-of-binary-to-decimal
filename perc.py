# INSTITUTO TECNOLOGICO DE MEXICO EN CELAYA
# AUTOR : JOSE MANUEL SOTELO PACHECO
import numpy as np
import math
binario = [11.1100101010 , 01.1000111010 , 00.0001111010 , 10.0101110000,10.0000111010]
decimal =[] 


def Bin(z):
	
	suma = 0
	suma2 = 0
	count1 = 0
	count2 = -1
	after_point = []
	before_point = []
	numbers = str(z)
	for x in range(len(numbers)):
		if(numbers[x] == "1" or numbers[x] == "0"):
			#print(numbers[x])
			if(count2 == -1):
				after_point.append(int(numbers[x]))
				count1+=1
			else:
				before_point.append(int(numbers[x]))
				count2 +=1
		else:
			count2 = 0
			#print("-1")
	for y in range(len(after_point)):
		suma += after_point[y]*pow(2,count1-1)
		count1 -=1

	for mamalon in range(len(before_point)):
		if(before_point[mamalon] != 0):
			suma2 += 1/(before_point[mamalon]*pow(2,mamalon + 1))
		'''print("#########################################")
	print(count1)
	print(count2)
	print(after_point)
	print(before_point)
	print(suma2 + suma)'''
	#Reset
	#print("#########################################")
	count1 = 0
	count2 = -1
	np.delete(after_point,0,0)
	np.delete(before_point,0,0)
	return (suma + suma2)



for i in range(len(binario)):
	y = Bin(binario[i])
	print(y)
