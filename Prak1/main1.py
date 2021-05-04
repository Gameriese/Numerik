import numpy as np
import matplotlib.pyplot as plt
import lib1

def f1(x):
    return x**3
    
def f2(x):
    return (x**4)-2*(x**3)+3

def f3(x):
    return 3 * x**(1/5)

def f4(x):
    return np.sin(x)

x = np.linspace(-1, 2, 100) # 100 Stützstellen
plt.plot(x, f1(x))  # Plot von -1 bis 2
plt.show()  # Plot anzeigen

x = np.linspace(0, 2, 100)  # 100 Stützstellen
plt.plot(x, f2(x))  # Plot von 0 bis 2
plt.show()  # Plot anzeigen

x = np.linspace(0, 32, 100)     # 100 Stützstellen
plt.plot(x, f3(x))  # Plot von 0 bis 32
plt.show()  # Plot anzeigen

x = np.linspace(0, 7*np.pi, 100)    # 100 Stützstellen
plt.plot(x, f4(x))  # Plot von 0 bis 7pi
plt.show()  # Plot anzeigen


def true_result(f):
    if f == f1:
        return 15/4
    elif f == f2:
        return 22/5
    elif f == f3:
        return 160
    elif f == f4:
        return 2
    
def fehler1(absu):
    for f in range(1, 1000):
        if abs(15 / 4 - lib1.Sh(f1, -1, 2, f)) <= absu:
            return f
def fehler2(absu):
    for f in range(1, 1000):
        if abs(22 / 5 - lib1.Sh(f2, 0, 2, f)) <= absu:
            return f
        
def fehler3(absu):
    for f in range(1, 2000):
        if abs(160 - lib1.Sh(f3, 0, 32, f)) <= absu:
            return f
        
def fehler4(absu):
    for f in range(1, 1000):
        if abs(2 - lib1.Sh(f4, 0, 7 * np.pi, f)) <= absu:
            return f
        
print("Anzahl Teilintervalle für abs.Fehler von 0.1 bei F1", fehler1(0.1)) 
print("Anzahl Teilintervalle für abs.Fehler von 0.1 bei F2", fehler2(0.1)) 
print("Anzahl Teilintervalle für abs.Fehler von 0.1 bei F3", fehler3(0.1)) 
print("Anzahl Teilintervalle für abs.Fehler von 0.1 bei F4", fehler4(0.1)) 
Anzahlen = [fehler1(0.1), fehler2(0.1), fehler3(0.1), fehler4(0.1)]
print(Anzahlen)