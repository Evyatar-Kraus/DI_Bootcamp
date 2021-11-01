
from random import randint

from mutation_constants import MAX_RANDOM_FLIP_NUM, MIN_RANDOM_FLIP_NUM, MAX_ENV_MODIFIER, \
    MIN_ENV_MODIFIER, THRESHOLD_FLIP_NUMBER, THRESHOLD_ENV_MODIFIER

# list comprehension is awesome
def generate_random_DNA(chroms_lines=10, genes_in_line=10):
    return {'chromosomes':  [[randint(0, 1) for _ in range(0, genes_in_line)] for _ in range(0, chroms_lines)]}

#flip or not - with some excitement - env for modifying the random
def will_flip(env):
    chance_num = randint(MIN_RANDOM_FLIP_NUM, MAX_RANDOM_FLIP_NUM)
    #0 env is no mutations
    if env == MIN_ENV_MODIFIER:
        return False
    #100 env is no mutations
    if env == MAX_ENV_MODIFIER:
        return True
    else:
        #some modifying
        if env > THRESHOLD_ENV_MODIFIER:
            chance_num = min(MAX_RANDOM_FLIP_NUM, chance_num + env)
        elif env < THRESHOLD_ENV_MODIFIER:
            chance_num =  max(MIN_RANDOM_FLIP_NUM, chance_num - env)
    if chance_num >= THRESHOLD_FLIP_NUMBER:  # flip
        return True
    else: #dont flip
        return False


def get_first_fully_mutated_organism(organism_list=[]):
    fully_mutated_found = False
    current_organism = None
    generations_until_full_mutation = 0
    try:
        while not fully_mutated_found:
            for organism in organism_list:
                current_organism = organism
                organism.mutate()
                generations_until_full_mutation += 1
                if current_organism.is_fully_mutated():
                    fully_mutated_found = True
                    break
    except KeyboardInterrupt:
        print("Stopped by keyboard interruptd, generations so far:", generations_until_full_mutation)
        return None 
    else:
        return {'name':current_organism.name , 'gens':generations_until_full_mutation}
