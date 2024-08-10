num1 = float(input())
# Defino una variable queue se llama numero2 y la leo del usuario
# Lo que leo lo convierot a un numero con float()
num2 = float(input())
# operacion sirve para especificar que operando usar +-*/
operacion = input()
# estas son las operaciones matematicas que se pueden hacer en mi calculadora
if operacion == '+':
	print('La suma es:', num1 + num2)

if operacion == '-':
	print(num1 - num2)

if operacion == '*':
	print(num1*num2)

if operacion == '/':
	print(num1/num2)
