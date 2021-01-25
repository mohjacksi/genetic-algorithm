from fuzzywuzzy import fuzz
import random
import string


class Individual:

    def __init__(self, length):

        self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.fitness = -1

    def __str__(self):

        return 'String: ' + str(self.string) + ' Fitness: ' + str(self.fitness)



def start():

    individuals = init_individuals(population, my_string_len)

    for generation in range(generations):

        print('Generation: ' + str(generation))

        individuals = fitness(individuals)
        individuals = selection(individuals)
        individuals = crossover(individuals)
        individuals = mutation(individuals)

        if any(individual.fitness >= 90 for individual in individuals):

            print('Threshold met!')
            exit(0)


def init_individuals(population, length):

    return [Individual(length) for _ in range(population)]


def fitness(individuals):

    for individual in individuals:

        individual.fitness = fuzz.ratio(individual.string, my_string)

    return individuals


def selection(individuals):
    
    #sort the individuals
    individuals = sorted(individuals, key=lambda individual: individual.fitness, reverse=True)
    print('\n'.join(map(str, individuals)))
    
    #select top 20% of individuals
    individuals = individuals[:int(0.2 * len(individuals))]

    return individuals


def crossover(individuals):

    offspring = []

    for _ in range((population - len(individuals)) // 2):

        parent1 = random.choice(individuals)
        parent2 = random.choice(individuals)
        child1 = Individual(my_string_len)
        child2 = Individual(my_string_len)
        split = random.randint(0, my_string_len)
        child1.string = parent1.string[0:split] + parent2.string[split:]
        child2.string = parent2.string[0:split] + parent1.string[split:]

        offspring.append(child1)
        offspring.append(child2)

    individuals.extend(offspring)

    return individuals


def mutation(individuals):

    for individual in individuals:

        for point, param in enumerate(individual.string):

            if random.uniform(0.0, 1.0) <= mutation_rate:

                individual.string = individual.string[0:point] + random.choice(string.ascii_letters) + individual.string[point+1:]

    return individuals

my_string = None
my_string_len = None
population = 20
generations = 10000
mutation_rate = 0.1 #10%

if __name__ == '__main__':

    my_string = 'MohammedNaseer'
    my_string_len = len(my_string)
    start()
