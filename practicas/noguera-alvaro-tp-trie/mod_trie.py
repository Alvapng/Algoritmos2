class Trie:
    root = None

class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False

#-------------------------------------------------------------------------------------------------------------------
# EJERCICIO 1
#-------------------------------------------------------------------------------------------------------------------

def insert(T,element):
    if(T.root == None):
        nodoRaiz = TrieNode()
        nodoRaiz.children = []
        T.root = nodoRaiz

    actualNode = T.root

    for c in element:
        letraEncontrada = False
        for letra in actualNode.children:
            if(letra.key == c):
                actualNode = letra
                letraEncontrada = True
                break      
        if(letraEncontrada == False):
            newNode = TrieNode()
            newNode.parent = actualNode
            newNode.children = []
            newNode.key = c
            actualNode.children.append(newNode)   
            actualNode = newNode   
                    
    actualNode.isEndOfWord = True


def search(T,element):
    if(T.root == None):
        return False

    actualNode = T.root

    for c in element:
        letraEncontrada = False
        for letra in actualNode.children:
            if(letra.key == c):
                actualNode = letra
                letraEncontrada = True    
    if(letraEncontrada == False):
        return False
    if(actualNode.isEndOfWord == True):
        return True
    else:
        return False        

#-------------------------------------------------------------------------------------------------------------------
# EJERCICIO 3
#-------------------------------------------------------------------------------------------------------------------

def delete(T, element):
    if T.root == None:
        return False
    return deleteR(T.root, element, 0)

def deleteR(actualNode, element, index=0):
    if index == len(element):
        if actualNode.isEndOfWord == False:
            return False
        
        actualNode.isEndOfWord = False
        
        return len(actualNode.children) == 0

    c = element[index]
    nodoHijo = None
    
    for letra in actualNode.children:
        if letra.key == c:
            nodoHijo = letra
            break

    if nodoHijo == None:
        return False  

    debeEliminarHijo = deleteR(nodoHijo, element, index + 1)

    if debeEliminarHijo:
        actualNode.children.remove(nodoHijo)
        
        return len(actualNode.children) == 0 and actualNode.isEndOfWord == False

    return False

#-------------------------------------------------------------------------------------------------------------------
# EJERCICIO 4
#-------------------------------------------------------------------------------------------------------------------

def prefijo(T,pref,n):
    if(T.root == None):
        return False

    if(len(pref) > n):
        return False

    actualNode = T.root

    letraEncontrada = False
    for c in pref:
        for letra in actualNode.children:
            if(letra.key == c):
                actualNode = letra
                letraEncontrada = True 
                break
    if(letraEncontrada == False):
        return False

    nodoPrefijo = actualNode
    prefijoR(nodoPrefijo,pref,n)

def prefijoR(nodo,palabraActual,n):    
    if(len(palabraActual) == n):
        if(nodo.isEndOfWord == True):
                print(palabraActual)
        return

    for c in nodo.children:
        prefijoR(c,palabraActual + c.key,n)

#-------------------------------------------------------------------------------------------------------------------
# EJERCICIO 5
#-------------------------------------------------------------------------------------------------------------------        

def obtenerTodas(T):
    if(T.root == None):
        return []
    palabras = allR(T.root,"",[])
    return palabras

def allR(nodoActual,palabraActual,palabras):
    if(nodoActual.isEndOfWord == True):
        palabras.append(palabraActual)

    for c in nodoActual.children:
        allR(c,palabraActual + c.key, palabras)    

    return palabras
    
def comparar(T1,T2):
    palabrasT1 = obtenerTodas(T1)

    for c in palabrasT1:
        if(search(T2,c) == False):
            return False
    return True

#-------------------------------------------------------------------------------------------------------------------
# EJERCICIO 6
#-------------------------------------------------------------------------------------------------------------------

def palabrasInvertidas(T):
    palabras = obtenerTodas(T)

    for palabra in palabras:
        palabraInvertida = palabra[::-1]

        if(search(T,palabraInvertida) == True):
            return True

    return False    


#-------------------------------------------------------------------------------------------------------------------
# EJERCICIO 7
#-------------------------------------------------------------------------------------------------------------------

def autoCompletar(T,Cadena):
    if(T.root == None):
        return ""

    nodoActual = T.root

    for c in Cadena:
        encontrado = False

        for hijo in nodoActual.children:
            if(hijo.key == c):
                nodoActual = hijo
                encontrado = True
                break
        if(encontrado == False):
            return ""    

    sufijo = ""

    while(len(nodoActual.children) == 1 and nodoActual.isEndOfWord == False):
        nodoActual = nodoActual.children[0]
        sufijo += nodoActual.key

    return sufijo