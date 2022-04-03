#!/usr/bin/env python3
# @Date       : 2022/2/18 
# @Filename   : huawei.py
# @Tag        :
# @Autor      : LI YAO
# @Difficulty :

from heapq import *
from typing import List,  Optional
from collections import defaultdict, deque, Counter
from itertools import product,combinations,permutations,accumulate
from random import choice, randrange,randint

class ListNode: 
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# -------------------------
class Solution:
	def fenban(self, paidui ):
		students = paidui.split()
		l1 = []
		l2 = []
		flag = 0
		for i, student in enumerate(students):
			num = student.split(sep='/')
			if i == 0:
				l1.append(int(num[0]))
				continue
			if num[1] == 'N':
				flag += 1
			if flag % 2 == 1:
				l2.append(int(num[0]))
			else:
				l1.append(int(num[0]))
		
		l1.sort()
		if len(l2) == 0:
			for i in l1:
				print(l1, end = ' ')
			return None 
		l2.sort()
		
		
		if l1[0] <= l2[0]:
			for i in l1:
				print(i, end = ' ')
			print()
			for i in l2:
				print(i, end = ' ')
			return None
		else:
			for i in l2:
				print(i, end = ' ')
			print()
			for i in l1:
				print(i, end = ' ')
			return None
		
# -------------------------
a = Solution()
b = "1/N 2/Y 3/N 4/Y"
try:
	a.fenban(b)
except:
	print("ERROR")




def longest_alp(degree, string):
	vowel_string = "aeiouAEIOU"
	head, length, tail = 0, 0, len(string) - 1
	
	def flaw_degree(string):
		degree = 0
		for i in string:
			if i in vowel_string:
				continue
			degree += 1
		return degree
	
	result = []
	while head <= tail:
		if string[head].startswith(tuple(vowel_string)) and string[tail].endswith(tuple(vowel_string)):
			result.append(string[head:tail + 1])
			if string[head + 1].startswith(tuple(vowel_string)):
				tail -= 1
			else:
				head += 1
		elif string[head].startswith(tuple(vowel_string)) and not string[tail].endswith(tuple(vowel_string)):
			tail -= 1
		else:
			head += 1
			
	for item in result:
		if flaw_degree(item) == degree:
			length = max(length, len(item))
	return length


if __name__ == '__main__':
	print(longest_alp(0, "asdbuiodevauufgh"))
	print(longest_alp(2, "aeueo"))
	print(longest_alp(1, "aabeebuu"))
