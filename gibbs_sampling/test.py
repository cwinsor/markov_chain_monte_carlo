# from Cory Maklin - Towards Data Science
# https://towardsdatascience.com/gibbs-sampling-8e4844560ae5#:~:text=The%20Gibbs%20Sampling%20is%20a,to%20estimate%20complex%20joint%20distributions.

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()

# We define the function for the posterior distribution (assume C=1).
f = lambda x, y: np.exp(-(x*x*y*y+x*x+y*y-8*x-8*y)/2.)

# Then, we plot the probability distribution.

xx = np.linspace(-1, 8, 100)
yy = np.linspace(-1, 8, 100)
xg,yg = np.meshgrid(xx, yy)
z = f(xg.ravel(), yg.ravel())
z2 = z.reshape(xg.shape)
plt.contourf(xg, yg, z2, cmap='BrBG')
plt.show()

# Now, we’ll attempt to estimate the probability distribution using Gibbs Sampling.
# As we mentioned previously, the conditional probabilities are normal distributions.
# Therefore, we can express them in terms of mu and sigma.
# In the following block of code, we define functions for mu and sigma, initialize our
# random variables X & Y, and set N (the number of iterations).
N = 50000
x = np.zeros(N+1)
y = np.zeros(N+1)
x[0] = 1.
y[0] = 6.
sig = lambda z, i: np.sqrt(1./(1.+z[i]*z[i]))
mu = lambda z, i: 4./(1.+z[i]*z[i])

# We step through the Gibbs Sampling algorithm.
for i in range(1, N, 2):
    sig_x = sig(y, i-1)
    mu_x = mu(y, i-1)
    x[i] = np.random.normal(mu_x, sig_x)
    y[i] = y[i-1]
    
    sig_y = sig(x, i)
    mu_y = mu(x, i)
    y[i+1] = np.random.normal(mu_y, sig_y)
    x[i+1] = x[i]

# Finally, we plot the results.
plt.hist(x, bins=50)
plt.show()
plt.hist(y, bins=50)
plt.show()

plt.contourf(xg, yg, z2, alpha=0.8, cmap='BrBG')
plt.plot(x[::10],y[::10], '.', alpha=0.1)
plt.plot(x[:300],y[:300], c='r', alpha=0.3, lw=1)
plt.show()

# As we can see, the probability distribution obtained using the Gibbs Sampling algorithm
# does a good job of approximating the target distribution.



