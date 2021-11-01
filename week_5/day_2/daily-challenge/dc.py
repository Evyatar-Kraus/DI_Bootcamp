# Instructions below ↓↓↓
# TLDR: generate Organism instances, they have a dna matrix - (each row is chromome with genes that are 1 or 0)
# Make function to mutate all the organism 
# and return the first that was fully mutated  - which means dna matrix is all 1s
# And see how many generations (loops) it took

from mutation_utils import generate_random_DNA, get_first_fully_mutated_organism
from organism import Organism

flu_virus = Organism('Flu', 25, generate_random_DNA(3,4))
tetanus_virus = Organism('Tetanus', 50,  generate_random_DNA())
hep_b_virus = Organism('Hepatitis B', 25, generate_random_DNA(6,6))
hep_a_virus = Organism('Hepatitis A', 33, generate_random_DNA(7,7))
hep_c_virus = Organism('Hepatitis C', 25, generate_random_DNA(3,4))
hep_d_virus = Organism('Hepatitis D', 25, generate_random_DNA(7,7))
hep_e_virus = Organism('Hepatitis E', 25, generate_random_DNA(4,3))
hep_f_virus = Organism('Hepatitis F', 44, generate_random_DNA(7,7))
hep_g_virus = Organism('Hepatitis G', 25, generate_random_DNA(4,4))
hep_h_virus = Organism('Hepatitis H', 77, generate_random_DNA(7,7))
hep_i_virus = Organism('Hepatitis I', 2, generate_random_DNA(7,7))

virus_list = [hep_b_virus, flu_virus,tetanus_virus,hep_a_virus,hep_c_virus,hep_d_virus,hep_e_virus,
    hep_f_virus,hep_g_virus,hep_h_virus,hep_i_virus]

full_mutation_result = get_first_fully_mutated_organism(virus_list)
if full_mutation_result:
    print(f"{full_mutation_result['name']} is fully mutated\nit took {full_mutation_result['gens']} generations.")

# Instructions :
# This challenge is about Biology that will put emphasis on your
#  knowledge of classes, inheritance and polymorphism.

# Build a DNA object. DNA is composed of chromosomes which
#  is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate,
#  meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also
# mutate the same way Chromosomes can mutate.

# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object
# and an environment parameter that sets the probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one
# gets to a DNA which is only made of 1s.
# Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and
# tell us your conclusion :)
