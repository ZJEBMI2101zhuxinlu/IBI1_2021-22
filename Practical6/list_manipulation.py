marks= [45,36,86,57,53,92,65,45]
print (sorted(marks))

import matplotlib.pyplot as plt
plt.boxplot(marks,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
            )
plt.ylabel('scores')
plt.show()

avg = sum(marks)/len(marks)
print (avg)
if avg>=60:
 print ("PASS!")
else:
 print ("FAIL!")
