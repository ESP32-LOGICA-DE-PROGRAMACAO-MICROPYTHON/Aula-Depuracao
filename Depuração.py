ano_de_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = 2023
idade =  ano_atual - ano_de_nascimento

if idade > 100:
  print('Ancião')
elif idade <= 100 or idade >=0:
  print('Normal')
else:
  print('Ainda não nasceu')