
from mutation_utils import  generate_random_DNA, will_flip

class Organism():
    def __init__(self, name, env, dna=None):
        self.env = env
        self.name = name
        self.dna = dna or generate_random_DNA()

    def mutate(self):
        new_organism_dna = self.dna
        for chroms_line_idx, chroms_line in enumerate(new_organism_dna['chromosomes']):
            for gene_idx, gene in enumerate(chroms_line):
                flip = will_flip(self.env)
                if flip:
                    new_organism_dna['chromosomes'][chroms_line_idx][gene_idx] = 1 - gene
        self.dna = new_organism_dna

    def is_fully_mutated(self):
        is_fully_mutated = True
        for chroms in self.dna.get('chromosomes'):
            if sum(chroms) != len(chroms):
                is_fully_mutated = False
                break
        return is_fully_mutated

    def __repr__(self):
        return self.name + '\n' + str(self.dna)
