"""
Created on Tue Oct 31 11:09:10 2023

@author: arsan
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:53:33 2023

@author: arsan
"""

# Trabajo computacional MATEMÁTICA DISCRETA 

# Integrantes:

# - Arnesano Gabriel Santiago
# - Corral Nicolas

#Desarrollar un algoritmo que dada una matriz cuadrada ingresada determine si es
#diagonalmente dominante, en cuyo caso escriba un mensaje: “La matriz ingresada es
#diagonalmente dominante”, y agregue si lo es en forma estricta o no.


# func. que genere una matriz cuadrada de orden n:

def gen_square_matrix(n,a=-100,b=100):
    
    '''Pre: n natural, a y b enteros 
       Pos: Devuelve una matriz de orden n con coeficientes aleatorios entre a y b
    '''
    
    import numpy as np 
    import random 
    list = []
    pre_matrix = []
    for i in range(n*n): 
        list.append(random.randint(a,b)) # coeficientes aleatorios de la matriz
    for i in range (0, n*n, n):
        sublista = [list[k] for k in range (i,i+n)] # genero las 'filas' de la matriz
        pre_matrix.append(sublista)
    matrix = np.matrix(pre_matrix)
    return matrix


# genero una func. que determina si la matriz es diagonalmente dominante: 
    
def diag_dom(matrix):
    
    '''Pre: matrix es una matriz cuadrada
       Pos: Imprime por consola si es diag_dom y si lo es estrictamente'''
       
    import math 
    import numpy as np
    diag_list = []
    matrix_range = int(math.sqrt(matrix.size))
    for i in range(int(math.sqrt(matrix.size))):
        diag_list.append(abs(matrix[i,i])) # obtengo la diagonal de la matriz
    list = [np.sum(np.absolute(matrix[i])) for i in range(matrix_range)]
    list = [list[i]-diag_list[i] for i in range (matrix_range)]
    
    diag_list = np.array(diag_list)
    list = np.array(list)
    
    es_diagonal = True
    es_estricta = True
    
    for n,i in enumerate(diag_list):
        
        if i >= list[n]:
            es_diagonal
        else: 
            es_diagonal = False
            es_estricta = False
            break
        
        if i == list[n]:
            es_estricta = False
        else:
            es_estricta

    if es_estricta: 
        print('La matriz ingresada es estrictamente diagonal dominante')
    elif es_diagonal: 
        print('La matriz es diagonal dominante no estricta')
    else: 
        print('La matriz no es diagonal dominante')
    return 
