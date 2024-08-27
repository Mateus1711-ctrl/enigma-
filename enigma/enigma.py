import numpy as np


alfabeto = "abcdefghijklmnopqrstuvwxyz "
n = len(alfabeto)


char_para_indice = {char: idx for idx, char in enumerate(alfabeto)}
indice_para_char = {idx: char for idx, char in enumerate(alfabeto)}


def para_one_hot(mensagem):

    T = len(mensagem)
    M = np.zeros((n, T))
    for i, char in enumerate(mensagem):
        if char in char_para_indice:
            M[char_para_indice[char], i] = 1
    return M  


def para_string(M):
    indices = np.argmax(M, axis=0)
    return ''.join(indice_para_char[idx] for idx in indices)

