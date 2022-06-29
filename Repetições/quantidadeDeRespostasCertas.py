'''
Exercicío 5.10 - Um programa para corrigir um teste de múltipla escolha com três questões. A resposta da primeira pergunta é "b", a segunda
, "a" e da terceira "d". O programa conta conta um ponto a cada resposta correta
'''

pontos = 0 # Contador de pontos recebe 0
questao = 1 # questao recebe 1

while questao <= 3 : # Enquanto questão for menor ou igual a 3, faça:
    resposta = input("Digite sua resposta da {} questao: " .format(questao)) #Recebendo a resposta da pergunta
    if questao == 1 and resposta == 'b' or resposta == 'B' : # Questão 1 - Resposta - B
        pontos = pontos + 1 # Caso houver acerto, a quantidade de ponto é incrementado
    if questao == 2 and resposta == 'a' or resposta == 'A' : # Questão 2 - Resposta - A
        pontos = pontos + 1 # Caso houver acerto, a quantidade de ponto é incrementado
    if questao == 3 and resposta == 'd' or resposta == 'd' : # Questão 3 - Resposta - D
        pontos = pontos + 1 # Caso houver acerto, a quantidade de ponto é incrementado
    questao = questao + 1 # Questão é incrementada
print("O aluno fez {} ponto(s)" .format(pontos)) # Exibe a quantidade de ponto(s)