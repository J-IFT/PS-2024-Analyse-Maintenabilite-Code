import random

def system_state(a, b):
    if random.random() > 0.5:
        if a > 10 and b < 5:
            return "ouvert"
        else:
            return "fermé"
    else:
        return "ouvert"

if __name__ == "__main__":
    a = int(input("Entrez la valeur de a : "))
    b = int(input("Entrez la valeur de b : "))
    
    result = system_state(a, b)
    print(f"Le système est {result}")