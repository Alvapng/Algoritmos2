from mod_trie import *

T = Trie()

insert(T,"banana")
insert(T,"bananaso")
insert(T,"balon")
insert(T,"bajon")

print(search(T,"banana"))
print(search(T,"bananaso"))
print(search(T,"bajoneria"))

delete(T,"banana")
print(search(T,"banana"))
print(search(T,"bananaso"))

print("---------------------------------")

T2 = Trie()
insert(T2,"patos")
insert(T2,"pato")
insert(T2,"paternal")
insert(T2,"patas")
insert(T2,"papas")
insert(T2,"peras")

#prefijo(T2,"pa",5)

#palabras = obtenerTodas(T2)

#for c in palabras:
 #   print(c)

insert(T,"patos")
insert(T,"pato")
insert(T,"paternal")
insert(T,"patas")
insert(T,"papas")
insert(T,"peras") 

print(comparar(T2,T))

print("---------------------------")

insert(T2,"sotap")

print(palabrasInvertidas(T2))

print(palabrasInvertidas(T))