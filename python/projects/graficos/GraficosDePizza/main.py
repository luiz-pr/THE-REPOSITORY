import matplotlib
import numpy as np

y = np.array([ 35, 25, 25, 15])

mylabels = ['maçãs', 'Bananas', 'Laranjas', 'Melancias']

myexpode = [0.2, 0, 0, 0]

plt.pie(y, labels=mylabels, explode=myexpode, shadow=True)
plt.show()