import numpy as np
from enigma import para_one_hot, para_string, cifrar, decifrar, enigma, de_enigma

def main():
    mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    n = len(alfabeto)
    
    P = np.eye(n)[np.random.permutation(n)]
    E = np.eye(n)[np.random.permutation(n)]
    
    print("=== Exemplo de One-Hot Encoding ===")
    one_hot_msg = para_one_hot(mensagem)
    print("Matriz One-Hot:")
    print(one_hot_msg)
    
    print("\n=== Conversão de One-Hot para String ===")
    string_msg = para_string(one_hot_msg)
    print("Mensagem recuperada:")
    print(string_msg)
    
    print("\n=== Exemplo de Cifra Simples ===")
    mensagem_cifrada = cifrar(mensagem, P)
    print("Mensagem cifrada:")
    print(mensagem_cifrada)
    
    print("\n=== Exemplo de Decifra Simples ===")
    mensagem_recuperada = decifrar(mensagem_cifrada, P)
    print("Mensagem recuperada:")
    print(mensagem_recuperada)
    
    print("\n=== Exemplo de Cifra Enigma ===")
    mensagem_enigma, lista_de_permutacoes = enigma(mensagem, P, E)
    print("Mensagem cifrada com Enigma:")
    print(mensagem_enigma)
    
    print("\n=== Exemplo de Decifra Enigma ===")
    mensagem_enigma_recuperada = de_enigma(mensagem_enigma, lista_de_permutacoes)
    print("Mensagem recuperada com Enigma:")
    print(mensagem_enigma_recuperada)

if __name__ == "__main__":
    main()
