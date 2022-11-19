from eval import Evaluator

print("*** zip_evaluate() ***")
words = ["le", "Loren", "Ipsun", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(f"{str((words, coefs))} = ", end="")
Evaluator.zip_evaluate(words, coefs)

words = ["le", "Loren", "Ipsun", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5, 2]
print(f"{str((words, coefs))} = ", end="")
Evaluator.zip_evaluate(words, coefs)

words = ["le", "Loren", "Ipsun", "est", 4.5]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(f"{str((words, coefs))} = ", end="")
Evaluator.zip_evaluate(words, coefs)

words = ["le", "Loren", "Ipsun", "est", "simple"]
coefs = [1.0, 2.0, 1.0, "4.0", 0.5]
print(f"{str((words, coefs))} = ", end="")
Evaluator.zip_evaluate(words, coefs)

words = []
coefs = []
print(f"{str((words, coefs))} = ", end="")
Evaluator.zip_evaluate(words, coefs)

words = ("le", "Loren", "Ipsun", "est", "simple")
coefs = (1.0, 2.0, 1.0, 4.0, 0.5)
print(f"{str((words, coefs))} = ", end="")
Evaluator.zip_evaluate(words, coefs)


words = {"le", "Loren", "Ipsun", "est", "simple"}
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(f"{str((words, coefs))} = ", end="")
Evaluator.zip_evaluate(words, coefs)

words = {"nom": "Gayerie", "prenom": "Eric"}
coefs = {1.0, 2.0}
print(f"{str((words, coefs))} = ", end="")
Evaluator.zip_evaluate(words, coefs)

print("\n*** enumerate_evaluate() ***")

words = ["le", "Loren", "Ipsun", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(f"{str((words, coefs))} = ", end="")
Evaluator.enumerate_evaluate(words, coefs)

words = ["le", "Loren", "Ipsun", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5, 2]
print(f"{str((words, coefs))} = ", end="")
Evaluator.enumerate_evaluate(words, coefs)

words = ["le", "Loren", "Ipsun", "est", 4.5]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(f"{str((words, coefs))} = ", end="")
Evaluator.enumerate_evaluate(words, coefs)

words = ["le", "Loren", "Ipsun", "est", "simple"]
coefs = [1.0, 2.0, 1.0, "4.0", 0.5]
print(f"{str((words, coefs))} = ", end="")
Evaluator.enumerate_evaluate(words, coefs)

words = []
coefs = []
print(f"{str((words, coefs))} = ", end="")
Evaluator.enumerate_evaluate(words, coefs)

words = ("le", "Loren", "Ipsun", "est", "simple")
coefs = (1.0, 2.0, 1.0, 4.0, 0.5)
print(f"{str((words, coefs))} = ", end="")
Evaluator.enumerate_evaluate(words, coefs)

words = {"le", "Loren", "Ipsun", "est", "simple"}
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(f"{str((words, coefs))} = ", end="")
Evaluator.enumerate_evaluate(words, coefs)

words = {"nom": "Gayerie", "prenom": "Eric"}
coefs = (1.0, 2.0)
print(f"{str((words, coefs))} = ", end="")
Evaluator.enumerate_evaluate(words, coefs)
