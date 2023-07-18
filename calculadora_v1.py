# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("Seja Bem vindo(a) a calculadora! \n")

# Crias as funções 
def adiçao(num1, num2):
    return num1 + num2 

def subtraçao(num1, num2):
    return num1 - num2 

def multiplicaçao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2 

def menu():
  print('Escolha uma das opções abaixo abaixo: \n')
  print('1 - Adição')
  print('2 - Subtração')
  print('3 - Multiplicação')
  print('4 - Divisão')
  print("5 - Sair")
  print("\n")


while True: 
  
  menu()

  escolha = int(input(("Digite a opção escolhida: ")))
  print('\n')

  if escolha == 5:
     print("Ok, saindo da calculadora...")
     break

  num1 = float(input("Digite o primeiro número: "))
  print('\n')
  num2 = float(input("Digite o segundo número: "))
  print('\n')
  
  if escolha == 4 and num2 == 0:
     print("Não é possével fazer divisão por zero!")
     print("\n")

  elif escolha == 1:
     print(num1, "+", num2, "=", adiçao(num1, num2))
     print('\n')

  elif escolha == 2:
     print(num1, "-", num2, "=", subtraçao(num1, num2))
     print("\n")
  elif escolha == 3:
     print(num1, "*", num2, "=", multiplicaçao(num1, num2))
     print('\n')

  elif escolha == 4:
     print(num1, "/", num2, "=", divisao(num1, num2))
     print('\n')

  else: 
     print("Operação inválida!") 

