def nucleotide_calculator(DNA):
	A=0
	T=0
	C=0
	G=0
	for i in range(0,len(DNA)):
		if DNA[i].upper()=='A':
			A=A+1
		if DNA[i].upper()=='T':
			T=T+1
		if DNA[i].upper()=='C':
			C=C+1
		if DNA[i].upper()=='G':
			G=G+1
	percentage_A=A/len(DNA)
	percentage_T=T/len(DNA)
	percentage_C=C/len(DNA)
	percentage_G=G/len(DNA)
	print('percentage_A is',percentage_A)
	print('percentage_T is',percentage_T)
	print('percentage_C is',percentage_C)
	print('percentage_G is',percentage_G)
DNA_example='atcgGGTACaTTGAtgccta'
nucleotide_calculator(DNA_example)
DNA=input('sequence:')
nucleotide_calculator(DNA)