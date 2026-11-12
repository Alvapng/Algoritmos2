#EJERCICIO 1

def existChar(s, c):
    for char in s:
        if char == c:
            return True
    return False

#EJERCICIO 2

def isPalindrome(s):
    inicio = 0
    fin = len(s) - 1
    
    while inicio < fin:
        if s[inicio] != s[fin]:
            return False
        inicio += 1
        fin -= 1
        
    return True


#EJERCICIO 3

def mostRepeatedChar(s):
    if not s:
        return ""
    
    frecuencias = {}
    for char in s:
        frecuencias[char] = frecuencias.get(char, 0) + 1
        
    char_max = s[0]
    max_freq = 0
    
    for char in s:
        if frecuencias[char] > max_freq:
            max_freq = frecuencias[char]
            char_max = char
            
    return char_max


#EJERCICIO 4

def getBiggestIslandLen(s):
    if not s:
        return 0
        
    max_isla = 1
    isla_actual = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            isla_actual += 1
        else:
            if isla_actual > max_isla:
                max_isla = isla_actual
            isla_actual = 1
            
    if isla_actual > max_isla:
        max_isla = isla_actual
        
    return max_isla


#EJERCICIO 5

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
        
    conteo = {}
    for char in s1:
        conteo[char] = conteo.get(char, 0) + 1
        
    for char in s2:
        if char not in conteo or conteo[char] == 0:
            return False
        conteo[char] -= 1
        
    return True


#EJERCICIO 6

def verifyBalancedParentheses(s):
    pila = []
    for char in s:
        if char == '(':
            pila.append(char)
        elif char == ')':
            if not pila:
                return False
            pila.pop()
    return len(pila) == 0


#EJERCICIO 7

def reduceLen(s):
    pila = []
    for char in s:
        if pila and pila[-1] == char:
            pila.pop()
        else:
            pila.append(char)
    return "".join(pila)


#EJERCICIO 8

def isContained(s, sub):
    it = iter(s)
    return all(c in it for c in sub)



#EJERCICIO 9

def isPatternContained(s, p, c):
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    dp[0][0] = True
    
    for j in range(1, m + 1):
        if p[j - 1] == c:
            dp[0][j] = dp[0][j - 1]
            
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == c:
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                
    return dp[n][m]



#EJERCICIO 14

def compute_lps(p):
    m = len(p)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMP(text, pattern):
    if not pattern or not text:
        return None
        
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    
    indices = []
    i = 0
    j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return indices if indices else None



#EJERCICIO 15

def KMPmod(text, pattern):
    if not pattern or not text:
        return None
        
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    
    indices = []
    i = 0
    j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == m:
            indices.append(i - j)
            j = 0 
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return indices if indices else None