"""
Desempacotamento de lista em Python
"""
lista = ['William', 'Renata', 'Vânia', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(n1, n2)
