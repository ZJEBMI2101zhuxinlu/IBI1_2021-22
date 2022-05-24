seq='ATGCAATCGACTACGATCAATCGAGGGCC'
seqence_cut=seq.count('GAATTC')
number=seq.count('GAATTC')+1
print('the number of the sequnce that can be cut:',seqence_cut)
print('the number of fragments which could be generated:',number)
#There is no enzymatic sequence and the generated DNA fragment is its own.