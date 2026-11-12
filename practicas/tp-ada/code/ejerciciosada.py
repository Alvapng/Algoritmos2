def darCambio(Cambio, Monedas):
    def backtrack(restante, index):
        if restante == 0:
            return 0
        if restante < 0 or index == len(Monedas):
            return float('inf')
        
        # Opción 1: Usar la moneda actual
        usar = 1 + backtrack(restante - Monedas[index], index)
        # Opción 2: Omitir la moneda actual y pasar a la siguiente
        saltar = backtrack(restante, index + 1)
        
        return min(usar, saltar)
    
    res = backtrack(Cambio, 0)
    return res if res != float('inf') else -1

### Ejercicio 2: Mochila (Pesos)

def mochila(PesoMax, latas):
    mejor_combinacion = []
    max_peso = 0
    
    def backtrack(index, peso_actual, combinacion_actual):
        nonlocal max_peso, mejor_combinacion
        if peso_actual > PesoMax:
            return
        if peso_actual > max_peso:
            max_peso = peso_actual
            mejor_combinacion = list(combinacion_actual)
            
        for i in range(index, len(latas)):
            combinacion_actual.append(latas[i])
            backtrack(i + 1, peso_actual + latas[i], combinacion_actual)
            combinacion_actual.pop()
            
    backtrack(0, 0, [])
    return mejor_combinacion

### Ejercicio 3: Subsecuencia Creciente (Backtracking)

def subsecuenciaCreciente(numeros):
    mejor_sub = []
    
    def backtrack(index, ultimo_val, actual_sub):
        nonlocal mejor_sub
        if len(actual_sub) > len(mejor_sub):
            mejor_sub = list(actual_sub)
            
        for i in range(index, len(numeros)):
            if ultimo_val is None or numeros[i] > ultimo_val:
                actual_sub.append(numeros[i])
                backtrack(i + 1, numeros[i], actual_sub)
                actual_sub.pop()
                
    backtrack(0, None, [])
    return mejor_sub

### Ejercicio 4: Subconjunto Suma

def subconjuntoSuma(numeros, valor):
    def backtrack(index, suma_actual):
        if suma_actual == valor:
            return True
        if suma_actual > valor or index == len(numeros):
            return False
        
        return backtrack(index + 1, suma_actual + numeros[index]) or backtrack(index + 1, suma_actual)
        
    return backtrack(0, 0)


## Parte 2: Greedy

### Ejercicio 5: Administración de Actividades

def adminActividades(tareas, inicio, fin):
    # tareas es una lista de diccionarios o tuplas con 'inicio' y 'fin'
    tareas_ordenadas = sorted(tareas, key=lambda x: x['fin'])
    seleccionadas = []
    tiempo_fin_ultimo = inicio
    
    for tarea in tareas_ordenadas:
        if tarea['inicio'] >= tiempo_fin_ultimo and tarea['fin'] <= fin:
            seleccionadas.append(tarea)
            tiempo_fin_ultimo = tarea['fin']
            
    return seleccionadas

### Ejercicio 6: Búsqueda de Pares

def buscaPares(vector):
    vector.sort()
    n = len(vector)
    max_suma = 0
    for i in range(n // 2):
        suma_par = vector[i] + vector[n - 1 - i]
        if suma_par > max_suma:
            max_suma = suma_par
    return max_suma

### Ejercicio 7: Mochila con Beneficios (Greedy)

def mochila(PesoMax, latas):
    # latas: lista de diccionarios con {'peso': p, 'beneficio': b}
    latas_ordenadas = sorted(latas, key=lambda x: x['beneficio'] / x['peso'], reverse=True)
    peso_actual = 0
    seleccionadas = []
    
    for lata in latas_ordenadas:
        if peso_actual + lata['peso'] <= PesoMax:
            seleccionadas.append(lata)
            peso_actual += lata['peso']
            
    return seleccionadas


## Parte 3: Divide y Vencerás

### Ejercicio 8: Búsqueda Binaria

def busquedaBinaria(lista, x):
    def divide_y_venceras(izq, der):
        if izq > der:
            return False
        medio = (izq + der) // 2
        if lista[medio] == x:
            return True
        elif lista[medio] > x:
            return divide_y_venceras(izq, medio - 1)
        else:
            return divide_y_venceras(medio + 1, der)
            
    return divide_y_venceras(0, len(lista) - 1)


### Ejercicio 9: Búsqueda del k-ésimo menor elemento

def busquedaKesimo(lista, k):
    if not lista:
        return None
    pivote = lista[0]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    if k <= len(menores):
        return busquedaKesimo(menores, k)
    elif k <= len(menores) + len(iguales):
        return pivote
    else:
        return busquedaKesimo(mayores, k - len(menores) - len(iguales))


### Ejercicio 10: Subsecuencia Creciente (Divide y Vencerás)

def subsecuenciaCreciente(numeros):
    if not numeros:
        return []
    
    def resolver(index, ultimo):
        if index == len(numeros):
            return []
        excluir = resolver(index + 1, ultimo)
        incluir = []
        if ultimo is None or numeros[index] > ultimo:
            incluir = [numeros[index]] + resolver(index + 1, numeros[index])
            
        return incluir if len(incluir) > len(excluir) else excluir

    return resolver(0, None)


### Ejercicio 11: Elementos más cercanos a la mediana en $O(n)$

def elementosMasCercanosMediana(S, k):
    n = len(S)
    mediana = busquedaKesimo(S, n // 2 + 1)
    con_distancias = sorted(S, key=lambda x: abs(x - mediana))
    return con_distancias[:k]


### Ejercicio (Opcional): Distancia entre cadenas

def distancia(string1, string2):
    m, n = len(string1), len(string2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]


## Parte 4: Programación Dinámica

### Ejercicio 12: Dar Cambio (Programación Dinámica)

def darCambio(Cambio, Monedas):
    dp = [float('inf')] * (Cambio + 1)
    dp[0] = 0
    
    for i in range(1, Cambio + 1):
        for m in Monedas:
            if i - m >= 0:
                dp[i] = min(dp[i], dp[i - m] + 1)
                
    return dp[Cambio] if dp[Cambio] != float('inf') else -1

### Ejercicio 13: Subconjunto con suma exacta $K$

def subconjuntoSumaDP(A, K):
    n = len(A)
    dp = [[False] * (K + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
        
    for i in range(1, n + 1):
        for j in range(1, K + 1):
            if A[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - A[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][K]


### Ejercicio 14: Camino mínimo en matriz

def caminoMinimoMatriz(matriz):
    n = len(matriz)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = matriz[0][0]
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matriz[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + matriz[0][j]
        
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = matriz[i][j] + min(dp[i-1][j], dp[i][j-1])
            
    return dp[n-1][n-1]

### Ejercicio 15: Secuencia Común más Larga (LCS)

def lcs(v, w):
    m, n = len(v), len(w)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if v[i-1] == w[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]