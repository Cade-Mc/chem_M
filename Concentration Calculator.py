from chempy import Substance
from chempy import balance_stoichiometry
import decimal
import elementList as el

calculator = True
def input_grams(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            return 0

def input_mol(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            return 0

while calculator:
        firstmol = None
        secondmol = None
        #                        First Molecule
        firstm = input("What is the first molecule?: ")
        fm = Substance.from_formula(firstm)
        firstg = input_grams("How many grams does it have? Type N if none: ")
        if firstg == 0:
            print("No Grams.")
        else:
            firstmol = decimal.Decimal(firstg) / decimal.Decimal(fm.mass)
            print(f'{firstmol} mol| {firstm}')

        #                        Second Molecule
        secondm = input("What is the second molecule?: ")
        if secondm is not None:
            sm = Substance.from_formula(secondm)
            secondg = input_grams("How many grams does it have? Type N if none: ")
            if secondg == 0:
                print("No Grams")
            else:
                secondmol = decimal.Decimal(secondg) / decimal.Decimal(sm.mass)
                print(f'{secondmol} mol| {secondm}')

        #                        Calculations First Molecule
        print("Only Type Integers From Here On.")
        type1 = input("What is the type of problem for the first molecule? \n\tFind M 1:\n\tFind L 2: \nFind Mol 3:"
                     "\n\tType Q to Quit!: \n\tInput:")

        if type1.lower() == "1":
            if firstmol == None:
                mol = firstmol
            else:
                mol = input("\nHow many mols?: ")
            vol = input("\nWhat is the vol. in L ")
            answer = decimal.Decimal(firstmol) / decimal.Decimal(vol)
            print(f'{answer} M')
            break

        if type1.lower() == "2":
            if firstmol == None:
                mol = firstmol
            else:
                mol = input("\nHow many mols?: ")
            M = input("\nWhat is the Molarity of the concentration?: ")
            answer = decimal.Decimal(mol) / decimal.Decimal(M)
            print(f'{answer} L')
            break

        if type1.lower() == "3":
            M = input("\nWhat is the M value?: ")
            vol = input("\nWhat is the vol. in L?: ")
            answer = decimal.Decimal(M) / decimal.Decimal(vol)
            print(f'{answer} Mol')
            break

        #                        Calculations Second Molecule
        type2 = input("What is the type of problem for the second molecule? \n\tFind M 1:\n\tFind L 2: \nFind Mol 3:"
                      "\n\tType Q to Quit!: \n\tInput:")

        if type2.lower() == "1":
            if secondmol == None:
                mol = secondmol
            else:
                mol = input("\nHow many mols?: ")
            vol = input("\nWhat is the vol. in L ")
            answer = decimal.Decimal(firstmol) / decimal.Decimal(vol)
            print(f'{answer} M')
            break

        if type2.lower() == "2":
            if secondmol == None:
                mol = secondmol
            else:
                mol = input("\nHow many mols?: ")
            M = input("\nWhat is the Molarity of the concentration?: ")
            answer = decimal.Decimal(mol) / decimal.Decimal(M)
            print(f'{answer} L')
            break

        if type2.lower() == "3":
            M = input("\nWhat is the M value?: ")
            vol = input("\nWhat is the vol. in L?: ")
            answer = decimal.Decimal(M) / decimal.Decimal(vol)
            print(f'{answer} Mol')
            break

