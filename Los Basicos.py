#%% Function and digits number
def Tc(Tf):
    """

    Parameter
    ----------
    Tf : Temperature in Fahrenheit

    Returns
    -------
    Temperature in Celsius

    """
    return float((Tf-32)*5/9)
print("{:.44f}".format(Tc(189)))
#%% Lists and append
list=[]
list.append(5)
list.append(10)
list.append(20)
list.append(list[0])

#%% Mind the indent or you're gonna get an infinite loop!!!
liste = []
x = 5
while x < 21:
    liste.append(x)
    x = x * 2
liste.append(40)
a=liste
a[1]=0
b=liste[:]
id(liste)
id(a)
id(b)
if id(a)==id(b):
    print("a=b")
else:
    print("a!=b")
    
#%% Sequence
suite=list(range(0,21,1))
suite

#%% Ayo when did else and if get a child
x=1
y=2
z=1
if x>y or x==y:
    print("x=>y")
elif x>z or x==z:
    print("x=>z")
else:
    print("x<y et z")
    
#%% Interactive input
def Tc(Tf):
    return float((Tf-32)*5/9)
T_in_F= input("Enter temp. en Fahrenheit:")
T_in_F=float(T_in_F)
print("{:.20f}".format(Tc(T_in_F)))

#%% While loop
import math as mt
x0=257
ct=0
x=x0
while x>1:
    x=x//2
    ct=ct+1
print("Approximation: log2(",x0,") =",ct)
x1=mt.log2(x0)
ratio=(ct/x1)*100
print("Précision:",ratio,"%")

#%% Continue loop
notes = [10.4, 7.6, 13.5, 0, 14.5, 0, 15]

somme = 0
N = 0
for i in notes:
    somme += i
    N += 1

print("N=", N, " moyenne = %2.2f" % (somme/N))

somme = 0
N = 0
for i in notes:
    if (abs(i) < 1e-7):
        continue
    somme += i
    N += 1

print("N=", N, " moyenne = %2.2f" % (somme/N))

#%% Break loop
notes = [10.4, 7.6, 13.5, -10, 14.5, -4, 15]

somme = 0
N = 0
for i in notes:
    somme += i
    N += 1

print("N=", N, " moyenne = %2.2f" % (somme/N))


somme = 0
N = 0
for i in notes:
    if (i < 0):
        print("ERREUR: faute de frappe: ", i)
        break
    somme += i
    N += 1

print("N=", N, " moyenne = %2.2f" % (somme/N))

#%% Remove all variables
globals().clear()
