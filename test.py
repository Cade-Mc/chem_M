from chempy import balance_stoichiometry  # Main reaction in NASA's booster rockets:
from chempy import Substance
reac, prod = balance_stoichiometry({'NH4ClO4', 'Al'}, {'Al2O3', 'HCl', 'H2O', 'N2'})
from pprint import pprint
pprint(dict(reac))
# {'Al': 10, 'NH4ClO4': 6}
pprint(dict(prod))
# {'Al2O3': 5, 'H2O': 9, 'HCl': 6, 'N2': 3}
iron = Substance.from_formula('Fe')
x = Substance.from_formula("NH4ClO4")
print(x.mass)
