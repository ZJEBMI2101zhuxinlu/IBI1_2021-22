import re
import os
os.chdir("/Users/86183/IBI1/IBI1_2021-22/Practical9") #the marker can change the path here:)
file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
output=open('cut_genes.fa','w')
se = file.read()
se = ''.join(se.split('\n'))
se=se.lstrip('>')
gene=re.split(r'>',se)
result=''
for i in range(len(gene)):
	if re.search(r'GAATTC',gene[i]):
		a=str(re.findall(r'gene:(.+?)\s',gene[i]))
		a=a.strip("['']")
		b=str(re.findall(r'](.+)',gene[i]))
		b=b.strip("['']")
		c=len(b)
		result=result+'>'+f'{a:10}'+str(c)+'\n'+b+'\n'
result=result[:-1]
output.write(result)
file.close()
output.close()