# Exemplo de AttributeError
a = "abc"
b = a.length
print(b)

# Exemplo corrigido de AttributeError
a = "abc"
b = len(a)
print(b)