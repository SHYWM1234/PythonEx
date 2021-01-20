# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 09:19:11 2020

@author: WangLei
"""
num = 2
for j in range(3, 50):
	for i in range(2, j):
		if j%i == 0:
			break
		if i == j-1 :
			print(j, end='\t')
			num += j
print('\n'+"..以内的质数和：",num)
