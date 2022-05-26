# Name: manikanta uppulapu
# Roll number: BT21BTECH11005

import matplotlib.pyplot as plt
from scipy.stats import binom

n = 50
p = 0.25

# Answer
print(binom.pmf(17, n, p))

# Plot
X = list(range(n + 1))
Y = binom.pmf(X, n, p)
plt.stem(X, Y, linefmt='r-', markerfmt='ro', basefmt='k--')
plt.title('Probability Mass Function')
plt.xticks(X)
plt.xlabel('$Y$')
plt.ylabel('Probability')
plt.savefig('../figs/fig-1.png')
plt.show()
