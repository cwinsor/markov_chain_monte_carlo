# Gibbs Sampling
Reference:
* [Cory Maklin - Towards Data Science](https://towardsdatascience.com/gibbs-sampling-8e4844560ae5#:~:text=The%20Gibbs%20Sampling%20is%20a,to%20estimate%20complex%20joint%20distributions)

Gibbs sampling can be used if we want a multivariate distribution p(X,Y) but only know the conditional distributions p(X|Y), p(Y|X).

The algorithm starts by randomly choosing X_0 and Y_0. Then for N iterations it alternately samples a new Yn+1 from P(Y|X_n) and X_n+1 from P(X|Y_n). 

![image](https://user-images.githubusercontent.com/4664692/158027170-adf6b05b-9d40-474e-b6df-3a6d6ceeabfb.png)

An example is given - if the joint and conditional probabilities are:

![image](https://user-images.githubusercontent.com/4664692/158029583-ed6f98a6-2a3c-4f6b-b533-9d095d98d1b4.png)

then the conditional probabilities are normal distributions parameterized by mean and standard deviations:

![image](https://user-images.githubusercontent.com/4664692/158030027-80f5513c-f34d-4c72-8d7d-9d4a43d3cfdd.png)

Now that we have the expected data (the joint distribution) and the ability to compute conditional distributions we can implement the algorithm to create the observed estimate of the joint distribution.  Code is in the .py file.
