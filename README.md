# Genetic Algorithm  

![Python version][python-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

## About this repo:  

An implementation of a genetic algorithm that guesses the right answer(string) using the mutation operator.  
It has been developed on Ubuntu 18.04 using python 3.6.  


## Content:  

- **example.py:** The file containing the Genetic Algorithm example.  


## Try the example:  

`gene_set` contains the set of chars (genes) that strings (generations) will be formed of.  
The first iteration, a string (agent) will be randomly generated, its fitness value will be calculated using `get_fitness()`. Then the mutation operator will be applied every iteration and the fitness value will be calculated. This process will be repeated until we get a convergence to the target string.  

*N.B:* The convergence may take long time since there is nothing preventing the same mutation to appear in the different generations.  

[python-version]:https://img.shields.io/badge/python-3.6+-brightgreen.svg
[issues-image]:https://img.shields.io/github/issues/maky-hnou/Genetic_Algorithm.svg
[issues-url]:https://github.com/maky-hnou/Genetic_Algorithm/issues
[fork-image]:https://img.shields.io/github/forks/maky-hnou/Genetic_Algorithm.svg
[fork-url]:https://github.com/maky-hnou/Genetic_Algorithm/network/members
[stars-image]:https://img.shields.io/github/stars/maky-hnou/Genetic_Algorithm.svg
[stars-url]:https://github.com/maky-hnou/Genetic_Algorithm/stargazers
[license-image]:https://img.shields.io/github/license/maky-hnou/Genetic_Algorithm.svg
[license-url]:https://github.com/maky-hnou/Genetic_Algorithm/blob/master/LICENSE
