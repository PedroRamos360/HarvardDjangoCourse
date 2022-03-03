# lambda é uma função de uma linha que recebe um valor e retorna outro

carros = [
    { 'carro': 'celta', 'valor': 15 },
    { 'carro': 'ferrari', 'valor': 1200},
    { 'carro': 'camaro', 'valor': 1000},
]

carros.sort(key=lambda carro: carro['valor'])
print(carros)