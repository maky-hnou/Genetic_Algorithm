# Genetic Algorithm  

## About this repo:  
An implementation of a genetic algorithm that guesses the right answer(string) using the mutation operator.  
It has been developed on Ubuntu 18.04 using python 3.6.  

## Content:  

- **example.py:** The file containing the Genetic Algorithm example.  


## Try the example:  

`gene_set` contains the set of chars (genes) that strings (generations) will be formed of.  
The first iteration, a string (agent) will be randomly generated, its fitness value will be calculated using `get_fitness()`. Then the mutation operator will be applied every iteration and the fitness value will be calculated. This process will be repeated until we get a convergence to the target string.  

*N.B:* The convergence may take long time since there is nothing preventing the same mutation to appear in the different generations.  
