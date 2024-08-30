import numpy as np


alfabeto = "abcdefghijklmnopqrstuvwxyz "
n = len(alfabeto)


char_para_indice = {char: idx for idx, char in enumerate(alfabeto)}
indice_para_char = {idx: char for idx, char in enumerate(alfabeto)}


def para_one_hot(mensagem):

    colunas = len(mensagem)
    M = np.zeros((n, colunas))
    for i, char in enumerate(mensagem):
        if char in char_para_indice:
            M[char_para_indice[char], i] = 1
    return M  


def para_string(M):
    indices = np.argmax(M, axis=0)
    return ''.join(indice_para_char[idx] for idx in indices)


def cifrar(mensagem, P):
    M = para_one_hot(mensagem)
    M_cifrada = np.dot(P, M)
    return para_string(M_cifrada) 


def decifrar(mensagem, P):
    M = para_one_hot(mensagem)
    P_inv = np.linalg.inv(P)
    M_decifrada = np.dot(P_inv, M)
    return para_string(M_decifrada)


def enigma(msg: str, P: np.array, E: np.array):
    mensagem_cifrada = []
    P_current = P.copy()  
    lista_de_permutacoes = []  
    
    for c in msg:
        mensagem_cifrada.append(cifrar(c, P_current))
        lista_de_permutacoes.append(P_current.copy())
        P_current = np.dot(P_current, E)  
    
    return ''.join(mensagem_cifrada), lista_de_permutacoes




def de_enigma(msg: str, lista_de_permutacoes: list):
    mensagem_decifrada = []
    
    for i, c in enumerate(msg):
        P_current = lista_de_permutacoes[i]
        mensagem_decifrada.append(decifrar(c, P_current))
    
    return ''.join(mensagem_decifrada)
