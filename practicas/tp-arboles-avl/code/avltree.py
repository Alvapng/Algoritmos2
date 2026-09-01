class AVLTRee:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None


#------------------------------------------------------------------------------
# INSERT BINARYTREE
#------------------------------------------------------------------------------

def insertBST(B,element,key):
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    if(B.root == None):
        B.root = newNode
        return key
    else:
        insertR(B,newNode,B.root)
        return key

def insertR(B,newNode, actualNode):
    if(newNode.key > actualNode.key):
        if(actualNode.rightnode == None):
            actualNode.rightnode = newNode
            newNode.parent = actualNode
        else:
            insertR(B,newNode,actualNode.rightnode)
    elif(newNode.key < actualNode.key):
        if(actualNode.leftnode == None):
            actualNode.leftnode = newNode
            newNode.parent = actualNode
        else:
            insertR(B,newNode,actualNode.leftnode)          


#---------------------------------------------------------------------------------
# SEARCH
#---------------------------------------------------------------------------------

def search(B, element):
    if(B.root == None):
        return None
    else:
        node = searchR(B.root,element)
        if(node != None):
            return node.key

def searchR(actualNode,element):    

    if(actualNode == None):
        return None

    if(actualNode.value == element):
        return actualNode
    elif(actualNode.leftnode != None):
        aux = searchR(actualNode.leftnode,element)
        if(aux != None):
            return aux
    
    return searchR(actualNode.rightnode,element)               


#---------------------------------------------------------------------------------------------
# DELETE BINARYTREE
#---------------------------------------------------------------------------------------------

def deleteBST(B,element):
    if(B.root == None):
        return None
    
    nodoBuscado = searchR(B.root,element)

    if(nodoBuscado == None):
        return None

    key_retorno = nodoBuscado.key
    deleteR(B,nodoBuscado)    
    return key_retorno

def deleteR(B, node):  
    if(node.leftnode == None and node.rightnode == None):
        if(node.parent == None):
            B.root = None
        elif(node.parent.leftnode == node):
            node.parent.leftnode = None
        else:
            node.parent.rightnode = None

    elif(node.leftnode == None or node.rightnode == None):
        if(node.rightnode != None):
            hijo = node.rightnode
        else:
            hijo = node.leftnode    

        if(node.parent == None):
            B.root = hijo
            hijo.parent = None
        else:
            hijo.parent = node.parent
            if(node.parent.leftnode == node):
                node.parent.leftnode = hijo
            else:
                node.parent.rightnode = hijo    
    else:
        sucesor = node.rightnode
        while(sucesor.leftnode != None):
            sucesor = sucesor.leftnode
        
        node.key = sucesor.key
        node.value = sucesor.value

        deleteR(B,sucesor)   


#----------------------------------------------------------------------------------------------
# DELETE (A TRAVES DE KEYS)
#----------------------------------------------------------------------------------------------

def deleteKey(B,key):
    if(B.root == None):
        return None
    
    nodoBuscado = searchKey(B.root, key)
    if(nodoBuscado == None):
        return None
    keyBuscado = nodoBuscado.key
    deleteR(B,nodoBuscado)
    return keyBuscado

def searchKey(actualNode, key):
    if(actualNode == None):
        return None
    if(actualNode.key == key):
        return actualNode
    if(key < actualNode.key):
        return searchKey(actualNode.leftnode, key)
    else:
        return searchKey(actualNode.rightnode, key)     


#------------------------------------------------------------------------------------------------
#  ACCES    
#------------------------------------------------------------------------------------------------    

def acces(B, key):
    if(B.root == None):
        return None
    else:
        node = searchKey(B.root, key)
        if(node != None):
            return node.value


#------------------------------------------------------------------------------------------------
#  UPDATE        
#------------------------------------------------------------------------------------------------        

def update(B, element,key):
    if(B.root == None):
        return None
    else:
        node = searchKey(B.root, key)
        if(node != None):
            node.value = element
            return node.key


#----------------------------------------------------------------------------------------------------
#  ROTATE LEFT        
#----------------------------------------------------------------------------------------------------        

def rotateLeft(Tree,avlnode):
    nodoB = avlnode.rightnode
    if(nodoB == None):
        return

    avlnode.rightnode = nodoB.leftnode
    if(nodoB.leftnode != None):
        nodoB.leftnode.parent = avlnode

    nodoB.parent = avlnode.parent

    if(avlnode.parent == None):
        Tree.root = nodoB
    elif(avlnode == avlnode.parent.leftnode):
        avlnode.parent.leftnode = nodoB
    else:
        avlnode.parent.rightnode = nodoB   

    nodoB.leftnode = avlnode
    avlnode.parent = nodoB     

#---------------------------------------------------------------------------------------------------
# ROTATE RIGHT
#---------------------------------------------------------------------------------------------------

def rotateRight(Tree,avlnode):
    nodoB = avlnode.leftnode
    if(nodoB == None):
        return

    avlnode.leftnode = nodoB.rightnode
    if(nodoB.rightnode != None):
        nodoB.rightnode.parent = avlnode

    nodoB.parent = avlnode.parent

    if(avlnode.parent == None):
        Tree.root = nodoB
    elif(avlnode.parent.leftnode == avlnode):
        avlnode.parent.leftnode = nodoB
    else:
        avlnode.parent.rightnode = nodoB

    nodoB.rightnode = avlnode
    avlnode.parent = nodoB


#-------------------------------------------------------------------------------------------------
#  CALCULATEBALANCE            
#-------------------------------------------------------------------------------------------------          

def calculateBalance(Tree):
    if(Tree.root == None):
        return None
    else:
        calculateBalanceR(Tree.root)
    return Tree    

def calculateBalanceR(nodoActual):
    if(nodoActual == None):
        return 0

    alturaIzq = calculateBalanceR(nodoActual.leftnode)
    alturaDer = calculateBalanceR(nodoActual.rightnode)

    nodoActual.bf = alturaIzq -  alturaDer 

    return max(alturaIzq,alturaDer) + 1


#--------------------------------------------------------------------------------------------------
# REBALANCE
#--------------------------------------------------------------------------------------------------

def reBalance(Tree):
    if(Tree.root == None):
        return None
    else:
        calculateBalance(Tree)
        reBalanceR(Tree,Tree.root)
        calculateBalance(Tree)
    return Tree

def reBalanceR(Tree,nodoActual):
    if(nodoActual == None):
        return

    reBalanceR(Tree,nodoActual.leftnode)
    reBalanceR(Tree,nodoActual.rightnode)

    if(nodoActual.bf > 1):
        if(nodoActual.leftnode.bf >= 0):
            rotateRight(Tree,nodoActual)
        else:
            rotateLeft(Tree,nodoActual.leftnode)  
            rotateRight(Tree,nodoActual)   
    if(nodoActual.bf < -1):
        if(nodoActual.rightnode.bf <= 0):
            rotateLeft(Tree,nodoActual)
        else:
            rotateRight(Tree,nodoActual.rightnode)
            rotateLeft(Tree, nodoActual)    


#--------------------------------------------------------------
# INSERT AVL
#--------------------------------------------------------------

def inserr(Tree,element,key):
    insertBST(Tree,element,key)
    return reBalance(Tree)


#--------------------------------------------------------------
# DELETE AVL
#--------------------------------------------------------------

def delete(Tree, element):
    deleteBST(Tree, element)
    return reBalance(Tree)