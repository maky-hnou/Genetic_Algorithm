import datetime
import random


def gen_parent(length, gene_set):
    genes = []
    while len(genes) < length:
        sample_size = min(length - len(genes), len(gene_set))
        genes.extend(random.sample(gene_set, sample_size))
    return ''.join(genes)


def get_fitness(guess):
    fitness = sum(1 for expected, actual in zip(
        target, guess) if expected == actual)
    return fitness


def mutate(parent, gene_set):
    index = random.randrange(0, len(parent))
    child_genes = list(parent)
    new_gene, alternate = random.sample(gene_set, 2)
    child_genes[index] = (alternate if new_gene
                          == child_genes[index] else new_gene)
    return ''.join(child_genes)


def display(guess, start_time):
    time_diff = datetime.datetime.now() - start_time
    fitness = get_fitness(guess)
    print('{}\t{}\t{}'.format(guess, fitness, time_diff))


if (__name__ == '__main__'):
    random.seed()
    gene_set = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.'
    target = 'Hello World!'
    start_time = datetime.datetime.now()
    best_parent = gen_parent(len(target), gene_set)
    bestFitness = get_fitness(best_parent)
    display(best_parent, start_time)
    while True:
        child = mutate(best_parent, gene_set)
        childFitness = get_fitness(child)
        if (bestFitness >= childFitness):
            continue
        display(child, start_time)
        if (childFitness >= len(best_parent)):
            break
        bestFitness = childFitness
        bestParent = child
