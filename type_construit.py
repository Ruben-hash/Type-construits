


phrase = input("entrez une phrase s'il vous plait.:")

n = 0

for i in phrase:
    if "E" == i or "e" == i or "é" == i or "è" == i or "ê" == i or "ë" == i:
        n += 1
print("il y a {} de e dans votre phrase".format(n))

#faire attention au nom des variable
#condition 'string' entre guillemets


 
phrase = input("entrez une phrase s'il vous plait.:")

n = 0
a = 0 
o = 0
I = 0
e = 0
u = 0
y = 0
for i in phrase:
    if "a" == i or "o" == i or "i" == i or "e" == i or "u" == i or "y" == i:
        n += 1
        if "a" == i:
            a += 1
        elif "o" == i:
            o += 1
        elif "i" == i:
            I += 1
        elif "e" == i:
            e += 1
        elif "u" == i:
            u += 1
        elif "y" == i:
            y += 1

print("il y a {} de e dans votre phrase dont {} a, {} o, {} i, {} e, {} u, {} y ".format(n,a,o,I,e,u,y))



def pluriel(mot):
  p = len(mot) - 2
  for i in range(len(mot)):
      if mot[-1] == "s":
          mot = mot
      elif mot[-1] == "l" and mot[-2] == "a":
          mot = mot[0:p] + "aux"
      elif mot[-1] != "s":
          mot = mot+"s"
  return mot

