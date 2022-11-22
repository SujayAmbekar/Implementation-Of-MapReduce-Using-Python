import wc_mapper as wcm
import wc_reducer as wcr
import grep_mapper as gmp
import grep_reducer as grd
import argparse
import sys

file = sys.argv[1]
files = sys.argv[1:]
choice = int(input("Enter\n1.Word Count\n2.Grep - Single Word Query\n3.Grep - Phase Query\n4.Exit\n"))

def intersect(lst):
	temp = []
	for i in lst[0]:
		flag = True
		for j in range(1,len(lst)):
			if i not in lst[j]:
				flag = False
			if flag==False:
				break
		if flag:
			temp.append(i)	
	return temp			

if choice==1:
	words = wcm.mapper(file)
	wcr.reducer(words)

elif choice==2:
	pattern = input("Enter the word to be searched\n")
	words = gmp.mapper(pattern, files)
	ans = grd.reducer(words)
	for i in ans:
		print(i,ans[i])

elif choice==3:
	lst=[]
	phrase = input("Enter the Pharse\n")
	phrases = phrase.split(" & ")
	for p in phrases:		
		words = gmp.mapper(p, files)
		ans = grd.reducer(words)
		lst.append(ans)
	
	d=dict()
	for file in files:
		d[file]=[]
	for i in range(len(files)):
		temp=[]
		for j in lst:
			temp.append(j[files[i]])
		d[files[i]] = intersect(temp)
	for i in d:
		print(i,d[i])	

elif choice==4:
	exit()		

