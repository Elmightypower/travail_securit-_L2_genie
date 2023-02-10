def OuExclusif(valeur_one, valeur_two):
interact = &quot;&quot
tableau_k = [&quot;&quot; for i in range(len(valeur_one))]
for i in range(len(valeur_one)):
variable_one = valeur_one[i:i + 1]
variable_two = valeur_two[i:i + 1]
tableau_k[i] = &quot;0&quot; if variable_one == variable_two else &quot;1&quot;
for i in tableau_k:
interact += i
return interact
def OuLogique(valeur_one, valeur_two):
interact = &quot;&quot;
tableau_k = [&quot;&quot; for i in range(len(valeur_one))]
for i in range(len(valeur_one)):
variable_one = valeur_one[i:i + 1]
variable_two = valeur_two[i:i + 1]
tableau_k[i] = &quot;1&quot; if variable_one == &quot;1&quot; or variable_two == &quot;1&quot; else &quot;0&quot;
for i in tableau_k:
interact += i
return interact
def ETlogique(va11, valeur_two):
interact = &quot;&quot;
tableau_k = [&quot;&quot;] * len(va11)
for i in range(len(va11)):
variable_one = va11[i:i + 1]
variable_two = valeur_two[i:i + 1]
tableau_k[i] = &quot;1&quot; if variable_one == &quot;1&quot; and variable_two == &quot;1&quot; else &quot;0&quot;
interact = &quot;&quot;.join(tableau_k)
return interact

def permut(val, k):
interact = &quot;&quot;
tableau_k = [0] * len(val)
for i in range(len(val)):
id = k[i:i + 1]
vid = int(id)
tableau_k[i] = val[vid]
interact += tableau_k[i]
#print(&quot;interact permut&quot;, interact)
return interact

2

def inverse_permut(k):
interact = &quot;&quot;
tableau_k = [0] * len(k)
for i in range(len(k)):
id = k[i:i + 1]
vid = int(id)
tableau_k[vid] = str(i)
interact = &#39;&#39;.join(tableau_k)
#print(&quot;interact inverse&quot;, interact)
return interact
def decalage(val, ordre, gauche):
interact = &quot;&quot;
tableau_k = [&quot;&quot;] * len(val)
s = -1 if gauche else 1
for i in range(len(val)):
variable_one = val[i:i + 1]
o = ordre
j = i
while o &gt; 0:
if j + s &lt; 0:
j = len(val) - 1
elif j + s &gt;= len(val):
j = 0
else:
j = j + s
o -= 1
tableau_k[j] = variable_one
interact = &quot;&quot;.join(tableau_k)
return interact

def generateKey(k, pk, gdecalage, ddecalage):
interact = &quot;&quot;
nk = permut(k, pk)
k1 = nk[0:4]
k2 = nk[4:8]
nk1 = OuExclusif(k1, k2)
nk2 = ETlogique(k1, k2)
dnk1 = decalage(nk1, gdecalage, True)
dnk2 = decalage(nk2, ddecalage, False)
interact = dnk1 + &quot;,&quot; + dnk2
#print(&quot;interact keygen &quot; + interact)
return interact
def roundDChiffre(val, kp, k):
interact = &quot;&quot;
perm = permut(val, kp)
interact = OuExclusif(perm, k)
return interact

3

def roundGChiffre(vald, valg, k):
interact = &quot;&quot;
fc = OuLogique(valg, k)
interact = OuExclusif(vald, fc)
return interact
def roundGDechiffre(val, kp, k):
interact = &quot;&quot;
nkp = inverse_permut(kp)
c = OuExclusif(val, k)
interact = permut(c, nkp)
return interact
def roundDDechiffre(vald, valg, k):
interact = &quot;&quot;
fc = OuLogique(valg, k)
interact = OuExclusif(vald, fc)
return interact

def main():
print(&quot;********ALGORITHME DE FREISNEL CIPHER*********&quot;)
print(&quot;Donnez une clé K de longueur 8&quot;)
key = input()
while len(key) &lt; 8:
print(&quot;La taille de la clé doit être de longueur 8&quot;)
key = input()
print(&quot;Donnez la fonction H de permutation&quot;)
h = input()
while len(h) &lt; 8:
print(&quot;La taille doit être de longueur 8&quot;)
h = input()
decg = 0
decd = 0
print(&quot;Entrez l&#39;ordre de décalage à gauche&quot;)
decg = int(input())
while decg &lt;= 0:
print(&quot;L&#39;ordre doit être supérieur à 0&quot;)
decg = int(input())
print(&quot;Entrez l&#39;ordre de décalage à droite&quot;)
decd = int(input())
while decd &lt;= 0:
print(&quot;L&#39;ordre doit être supérieur à 0&quot;)
decd = int(input())
kgen = generateKey(key, h, decg, decd)
print(&quot;Entrez la valeur N ou C à traiter&quot;)
n = input()
while len(n) &lt; 8:
print(&quot;La taille doit être de longueur 8&quot;)
n = input()
choix = -1
while choix != 1 and choix != 2:
print(&quot;Voulez-vous chiffrer ou dechiffrer? (1 pour dechiffrer et 2
pour chiffrer)&quot;)

4

choix = int(input())
print(&quot;Entrez la permutation P de 4 bits&quot;)
p = input()
while len(p) &lt; 4:
print(&quot;La taille doit être de longueur 4&quot;)
p = input()
print(&quot;Entrez la clé de permutation pour l&#39;opération de chiffrement ou
déchiffrement&quot;)
keyc = input()
while len(keyc) &lt; 8:
print(&quot;La taille doit être de longueur 8&quot;)
keyc = input()
tkey = kgen.split(&quot;,&quot;)
if choix == 2:
pn = permut(n, keyc)
g0 = pn[:4]
d0 = pn[4:8]
d1 = roundDChiffre(g0, p, tkey[0])
g1 = roundGChiffre(d0, g0, tkey[0])
d2 = roundDChiffre(g1, p, tkey[1])
g2 = roundGChiffre(d1, g1, tkey[1])
c = g2 + d2
ikey = inverse_permut(keyc)
interact = permut(c, ikey)
print(&quot;La valeur chiffrée est :&quot;, interact)
else:
pn = permut(n, keyc)
g2 = pn[:4]
d2 = pn[4:8]
g1 = roundGDechiffre(d2, p, tkey[1])
d1 = roundDDechiffre(g2, g1, tkey[1])
g0 = roundGDechiffre(d1, p, tkey[0])
d0 = roundDDechiffre(g1, g0, tkey[0])
Nd = g0 + d0
ikey = inverse_permut(keyc)
interact = permut(Nd, ikey)
print(&quot;La valeur déchiffrée est :&quot;, interact)
main()
#test value to enter k 01101101 h 65274130 n 01101110 hh 46027315 P 2013 C :
10110010
# See PyCharm help at https://www.jetbrains.com/help/pycharm/