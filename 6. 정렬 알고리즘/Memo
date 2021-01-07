from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
	n = len(a)
	for i in range(n-1):
		for j in range(n - 1, i, -1):
			if a[j - 1] > a[j]:
				a[j - 1], a[j] = a[j], a[j - 1]
				

def bubble_sort2(a: MutableSequence) -> None:
	n = len(a)
	for i in range(n - 1):
		exchng = 0
		for j in range(n - 1, i ,-1):
			if a[j - 1] > a[j]:
				a[j - 1], a[j] = a[j], a[j - 1]
				exchng += 1
		if exchng == 0:
			break
			
def bubble_sort3(a):
	n = len(a)
	k = 0
	while k < n - 1:
		for j in range(n-1, k , -1):
			if a[j - 1] > a[j]:
				a[j - 1], a[j] = a[j], a[j - 1]
				last = j
		k = last
		
def shaker_sort(a):
	left = 0
	right = len(a) - 1
	last = right
	while left < right:
		for j in range(right, left, -1):
			if a[j - 1] > a[j]:
				a[j-1],a[j] = a[j],a[j-1]
				last = j
		for j in range(left, right):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				last = j
		right = last
		
def selection_sort(a):
	n = len(a)
	for i in range(n-1):
		min = i
		for j in range(i + 1,n):
			if a[j] < a[min]:
				min = j
		a[i], a[min] = a[min], a[i]
		
def insertion_sort(a):
	n = len(a)
	for i in range(1, n):
		j = i
		tmp = a[i]
		while j > 0 and a[j -1] > tmp:
			a[j] = a[j - 1]
			j -= 1
		a[j] = tmp
		
def binary_insertion_sort(a):
	n = len(a)
	for i in range(1, n):
		key = a[i]
		pl = 0
		pr = i -1
		
		while True:
			pc = (pl + pr) // 2
			if a[pc] == key:
				break
			elif a[pc] < key:
				pl = pc + 1
			else:
				pr = pc - 1
			if pl > pr:
				break
		
		pd = pc + 1 if pl <= pr else pr + 1
		
		for j in range(i, pd, -1):
			a[j] = a[j - 1]
		a[pd] = key
				
	
