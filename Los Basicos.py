#%% Function and digits number
def Tc(Tf):
    return float((Tf-32)*5/9)
print("{:.20f}".format(Tc(189)))

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