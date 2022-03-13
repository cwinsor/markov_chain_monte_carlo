# Metropolis-Hastings
Reference:
* [Will Koehrsen - Towards Data Science] (https://towardsdatascience.com/markov-chain-monte-carlo-in-python-44f7e609be98)
* code at  https://github.com/WillKoehrsen/ai-projects/blob/master/markov_chain_monte_carlo/markov_chain_monte_carlo.ipynb
* .
* [Eric F. Lock - Slides from PUBH 8442: Bayes Decision Theory and Data Analysis] (http://ericfrazerlock.com/Metropolis-Hastings_Sampling.pdf) 

The topic is Markov Chain Monte Carlo(1) specifically Metropolis-Hastings Sampling

(1) Regarding the name: Markov Chain Monte Carlo...
* "Markov" refers to the sampling technique - the current sample is based only on only the immediate prior sample - nothing earlier (markov independence statement).
* "Monte Carlo refers to a general technique of using repeated random samples to obtain a numerical answer."

**The code uses PyMC3 library** - good reference and more time should be invested here !

+===========================

The dataset from Koehrsen is a set of samples of the time at which Will goes to sleep. He has 60 samples. The variables are time (numeric) and sleep-state (nominal having 2 values).

![image](https://user-images.githubusercontent.com/4664692/158041138-03f769de-ecdd-4cb8-9c32-3daa957e1ce0.png)

A logistic regression is chosen:
* It is well suited for a binary transition
* The output is naturally in the range of 0 to 1 (can be interpreted as a cumulative probability)

![image](https://user-images.githubusercontent.com/4664692/158042200-79093b41-4738-47eb-b755-d98d2a38a212.png)

<the reviewer believes it is necessary to make an assumption the variables follow a normal distribution.  It is also necessary to establish an initial Alpha and Beta - these are updated as the algorithm goes>

"The specific MCMC algorithm we are using is called Metropolis Hastings. In order to connect our observed data to the model, every time a set of random values are drawn, the algorithm evaluates them against the data. If they do not agree with the data (I’m simplifying a little here), the values are rejected and the model remains in the current state. If the random values are in agreement with the data, the values are assigned to the parameters and become the current state. This process continues for a specified number of steps, with the accuracy of the model improving with the number of steps.
  
"To implement MCMC in Python, we will use the PyMC3 Bayesian inference library."
 
 ![image](https://user-images.githubusercontent.com/4664692/158041891-6d123b3b-dad7-40f1-8b19-52686c795183.png)

A trace of Alpha and Beta parameters show the Monte Carlo sampling
![image](https://user-images.githubusercontent.com/4664692/158041914-a7796adc-e5a9-4d95-ad38-8f7f87199580.png)

MCMC will discard many values until it starts to converge (later in the sampling)

Assessing convergence and model quality would use auto-correlation between variables - the library is a resource here and the details are omitted but would become important in practice.

![image](https://user-images.githubusercontent.com/4664692/158042024-9eb0cfa9-31cd-45d3-94be-bb2e78b5be6a.png)

With the model in place we are able to make predictions on likelihood of being asleep given a certain time.
![image](https://user-images.githubusercontent.com/4664692/158042118-fb00596f-6968-4670-8c91-56a724968fea.png)


  
