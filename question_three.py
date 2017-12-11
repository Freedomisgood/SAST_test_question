from collections import Counter,OrderedDict
from data import str_demo
def get_most_common_char(docu,times):
	s=str.split(str(docu))
	dict1={}
	dict2=OrderedDict()
	list1=[]
	list2=[]
	for x in s:
		for y in x:
			if y.isalpha() ==1:
				if y not in dict1.keys():
					dict1[y] = 1
				else :
					dict1[y] +=1
	for x,y in dict1.items():
		if y >=times:
			dict2[x]=y
	dict2=OrderedDict(sorted(dict2.items(),key=lambda t:t[1],reverse=True ))
	for x in range(len(dict2)):
		temp = dict2.popitem(False)
		list2.append(temp)
	print(list2)

def save_data(data,filename,mode):
	with open(filename,mode) as f:
		f.write(data)

print (get_most_common_char(str_demo, 10))

