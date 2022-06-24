'''
- Exercicío 3.14: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar sabendo que o carro custa 
R$ 60,00 por dia e R$ 0,15 por km rodado.

'''
qnt_dias = int(input("Por quantos dias o carro foi alugado: ")) # Quantidade de dias
km_rodados = int(input("Digite a quantidade de Km rodados: ")) #Quantidade de km rodados
total_pagar =  (qnt_dias * 60) + (km_rodados * 0.15)
# Total a pagar
print("O carro foi alugado por {} dias e foram percorridos {}km, o total a pagar = R${:5.2f}".format(qnt_dias, km_rodados, total_pagar))