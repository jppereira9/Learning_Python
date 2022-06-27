'''
- If - As condições servem para selecionar quando uma parte do programa deve ser ativada e quando simplesmente
ignorada. Em python, as estrutura de decisão é o if: Seu formato é apresentado a seguir:

if <condição> :
    bloco verdadeiro

- If nada mais é que o nosso "se". Poderemoes, entãom entendê-lo em português da seguinte forma: se a condição for
verdadeira, faça algo.

'''

#Programa 4.1 - Lê dois valores e imrpime qual o maior

a = int(input("Primeiro valor: ")) # Recebendo o primeiro valor
b = int(input("Segindo valor: ")) # Recebendo o segundo valor

if a > b : # a é maior que b?
    print("O primeiro valor é maior!")
if b > a : # b é maior que a? 
    print("O segundo valor é maior!")