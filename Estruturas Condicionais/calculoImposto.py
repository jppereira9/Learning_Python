# Programa 4.3 - Cálculo de Imposto de Renda

salario = float(input("Digite o salario para o calculo do imposto: ")) # Recebendo o salário
base = salario  # Base recebe salário
imposto = 0 # Guarda o valor do imposto

if salario > 3000 : # Caso o salário seja maior que R$ 3000,00
    imposto = imposto + (base - 1000) * 0.35 # Cálculo do imposto para essa faixa salarial
    base = 3000 # base = 3000
if base > 1000 : # base maior que R$ 1000,00
    imposto = imposto + (base - 1000) * 0.20# Cálculo do imposto para essa faixa salarial
print("Salario: R$ {:5.2f} - Imposto a pagar: R$ {:5.2f}".format(salario, imposto)) # Exibindo o valor do imposto a ser pago

