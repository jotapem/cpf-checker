import sys

from src.cpf_checker import CPF_Checker

def help_message():
    return "Usage is `python demo.py [CPF,]"

if len(sys.argv) < 2:
    print(help_message())
    exit(-1)

cpfs = sys.argv[1:]
print("Analyzing %d CPFs" % (len(cpfs),))

checker = CPF_Checker()
for cpf in cpfs:
    checker.cpf = cpf
    if checker.check():
        print("Input %s is a valid CPF: %s" % (cpf, checker.pretty))
    else:
        print("Input %s is not a valid CPF" % (cpf,))
