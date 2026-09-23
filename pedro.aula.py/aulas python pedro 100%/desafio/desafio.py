# Converte Celsius para Fahrenheit
def celsius_para_fahrenheit(c):
    fahrenheit = (c * 9 / 5) + 32
    return fahrenheit


# Teste
print(celsius_para_fahrenheit(25))


# Verifica a senha
def validar_senha(senha):
    return len(senha) >= 8


# Senha válida
print(validar_senha("12345678"))

# Senha curta
print(validar_senha("1234"))


# Calcula os preços
def caixa(*precos):
    total = sum(precos)
    mais_caro = max(precos)
    media = total / len(precos)

    return total, mais_caro, media


# Teste dos preços
print(caixa(10, 25.5, 7, 40))


# Mostra os dados do aluno
def ficha_aluno(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


# Dados do aluno
ficha_aluno(nome="Carlos", idade=18, nota=8.5, turma="A")


# Soma dois números
def somar(a, b):
    return a + b


# Multiplica dois números
def multiplicar(a, b):
    return a * b


# Calcula a média
def media(a, b):
    return (a + b) / 2


# Adiciona um item na lista
def adicionar_item(lista, item):
    nova_lista = lista.copy()
    nova_lista.append(item)

    return nova_lista


# Lista de notas
notas = [7, 8, 9]

# Adiciona a nota 10
resultado = adicionar_item(notas, 10)

# Mostra a nova lista
print(resultado)

# Mostra a lista original
print(notas)