"""
Basic DPPL algorithm

literal: list of n variables
parameters:
 - instance: list of clauses
 - n: number of variable
 - m: number of clauses
output:
 - UNSAT+explanation or SAT+solution
"""
import copy

"""
Objectif: améliorer le literal par déduction logique
Amélioration par programmation dynamique:
    - Il faudrait faire un dictionnaire qui stocke pour chaque variable son apparition
"""

def unit_propagation(instance):
    inst = copy.deepcopy(instance)
    for clause in inst:
        if len(clause) == 1:
            for variable in clause:
                for i in range(len(inst)):
                    if variable in inst[i]:
                        inst[i] = [0]
                    elif -variable in inst[i]:
                        inst[i].remove(-variable)
                    if not inst[i]:
                        return "UNSAT"
    return inst

"""
def test_literal(instance, literal):
    abs_literal = [abs(x) for x in literal]
    for clause in instance:
        abs_clause = [abs(x) for x in clause]
        common_variable = list(set(abs_literal) & set(abs_clause))

        if common_variable == abs_clause:
            for i in range(len(clause)):
                # If one variable is 1
                if clause[i] == literal[i] :
                    break
                # If the clause is 0
                if i == len(clause)-1:
                    return 0 # Clause fausse => literal à abandonner
    return 1 # clause non fausse => literal à continuer
"""


""" Update an instance by computing it with a specific variable"""
def update_instance(instance, variable):
    for i in range(len(instance)):
        for j in range(len(instance[i])):
            if variable in instance[i]:
                instance[i] = [0]
            elif -variable in instance[i]:
                instance[i].remove(instance[i][j])
    return instance

""" Return the current state of computed instance """
def check_SAT(instance):
    for clause in instance:
        if not clause:
            return "UNSAT"
        elif clause != [0]:
            return "NO_STATE"
    return "SAT"

""" Classic DPLL algorithm """
def DPLL(instance):
    New_instance = unit_propagation(instance)
    result = check_SAT(New_instance)
    if result != "NO_STATE":
        return result
    if New_instance == "UNSAT":
        return "UNSAT"

    # Trouver une variable non assignée
    free_variable = 0
    for clause in New_instance:
        for i in range(len(clause)):
            if clause[i] != 0:
                free_variable = clause[i]
                break
        if free_variable:
            break
    New_instance1 = update_instance(New_instance, free_variable)
    New_instance2 = update_instance(New_instance, -free_variable)

    if DPLL(New_instance1) == "SAT":
        return "SAT"
    else:
        return DPLL(New_instance2)