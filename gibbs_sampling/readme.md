a^2+b^2=c^2
foo



# Gibbs Sampling
References:
* [Cory Maklin - Towards Data Science](https://towardsdatascience.com/gibbs-sampling-8e4844560ae5#:~:text=The%20Gibbs%20Sampling%20is%20a,to%20estimate%20complex%20joint%20distributions)
* foo
* bar

Gibbs sampling can be used if we want a multivariate distribution p(X,Y) but only know the conditional distributions p(X|Y), p(Y|X).

The algorithm starts by randomly choosing X^0^ and Y~0~.  Then for N iterations it alternately samples a new Y~n+1~ from P(Y|X~n~) and X~n+1~ from P(X|Y~n~). 

![image](https://user-images.githubusercontent.com/4664692/158027170-adf6b05b-9d40-474e-b6df-3a6d6ceeabfb.png)


```math
a^2+b^2=c^2
```

foo
