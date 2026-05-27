#Berechnung der Fibonacci-Folge
#Hier wird die iterative Berechnungsmethode verwendet.

def fibonacci(n):
    a, b = 0, 1
    i = 0
    print(f" n = {i}, Fibonacci-Zahl: {a}")
    while i < n:
        a, b = b, a+b
        i += 1
        print(f" n = {i}, Fibonacci-Zahl: {a}")
    return a

print("\n Berechnung der Fibonacci-Folge")
print("\n F0 = 0, F1 = 1 und Fn = Fn-1 + Fn-2 für alle n >= 2.")
while True:
    n = int(input("\n Iteration n bis zu der die Fibonacci-Folge berechnet werden soll eingeben: "))
    ergebnis = fibonacci(n)
    print(f" Das Ergebnis der Fibonacci-Folge bis zur Iteration {n} ist {ergebnis}.")
    beenden = input(" Weitere Berechnung j/n: ")
    if beenden != "j":
        print()
        break
# Dies ist nur ein Test!    