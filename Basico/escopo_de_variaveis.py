"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - São aquelas definidas fora de qualquer função e são acessíveis em qualquer parte do seu código, a menos que sejam substituídas no escopo local de uma função.

2 -  Variáveis locais:
     - São aquelas definidas dentro de uma função e só podem ser acessadas dentro desse contexto.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel
"""

# Exemplo de variável global
numero = 42
print(numero)
print(type(numero))

# Exemplo de variável local
numero = 42
novo = 0 # A variavel 'novo' está declarada localmente dentro do bloco if.

if numero > 10:
    novo = numero + 10
    print(novo)
print(novo)

