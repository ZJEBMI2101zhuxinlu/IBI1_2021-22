from xml.dom.minidom import parse
import xml.dom.minidom

domtree = xml.dom.minidom.parse("go_obo.xml")
obo=domtree.documentElement
terms=obo.getElementsByTagName('term')
print('the total number of terms currently recorded in GO is',len(terms))

dic={}
for term in terms:
	is_as=[]
	for i in term.getElementsByTagName('is_a'):
		is_as.append(i.childNodes[0].data)
	ids= term.getElementsByTagName('id')[0].childNodes[0].data
	for is_a in is_as:
		if is_a in dic:
			dic[is_a].append(ids)
		else:
			dic[is_a]=[ids]

def counter(list_):
	for i in list_:
		if i not in list0:
			list0.append(i)
			if i in dic:
				counter(dic[i])
	return len(list0)

totallist=[]
translist=[]
for term in terms:
	childnodes=0
	list0=[]
	ids=term.getElementsByTagName('id')[0].childNodes[0].data
	if ids in dic:
		childnodes=counter(dic[ids])
	totallist.append(childnodes)
	if 'translation' in term.getElementsByTagName("defstr")[0].childNodes[0].data:
		translist.append(childnodes)

import matplotlib.pyplot as plt
plt.boxplot(totallist,
			labels= ["GO"],
            )
plt.title("the distribution of childnodes across terms")
plt.ylabel('childnodes number')
plt.show()

plt.boxplot(translist,
			labels= ["translation GO"],
            )
plt.title("the distribution of childnodes across terms associated with translation")
plt.ylabel('childnodes number')
plt.show()

avg1=sum(totallist)/len(totallist)
avg2=sum(translist)/len(translist)
if avg1>avg2:
	print("The translation terms contain, on average, a smaller number of childnodes than the overall Gene Ontology.")
if avg1<avg2:
	print("The translation terms contain, on average, a greater number of childnodes than the overall Gene Ontology.")
#The translation terms contain, on average, a greater number of childnodes than the overall Gene Ontology.