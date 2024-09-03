# Enigma

## Descrição

O `enigma` é um pacote minimalista em Python que simula uma máquina Enigma simples. Ele permite cifrar e decifrar mensagens usando matrizes de permutação, combinando conceitos de álgebra linear com criptografia. Este projeto é ideal para fins educacionais, demonstrando como técnicas matemáticas podem ser aplicadas em criptografia.

## Funcionalidades

- **One-Hot Encoding:** Converte uma mensagem em uma matriz one-hot, que é uma representação binária da mensagem.
- **Cifra e Decifra Simples:** Cifra e decifra mensagens utilizando uma matriz de permutação fixa.
- **Cifra Enigma:** Aplica uma cifragem dinâmica semelhante à máquina Enigma, onde a matriz de permutação é alterada após cada caractere.
- **Decifra Enigma:** Reverte o processo de cifragem Enigma utilizando uma lista de permutações acumuladas durante a cifragem.

## Instalação

Para instalar o pacote, clone este repositório e utilize o `pip` para a instalação:

```bash
git clone https://github.com/Mateus1711-ctrl/enigma-.git
cd enigma
pip install .
