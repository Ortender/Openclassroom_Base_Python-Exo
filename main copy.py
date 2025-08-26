possibilite_operation = ["+","-","*","/"]
nombre1 = input("quel est le premier nombre? ")
while not str.isnumeric(nombre1):
	print("la valeur indiqué n'est pas un nombre")
	nombre1 = input("quel est le premier nombre? ")
nombre1 = int(nombre1)
nombre2 = input("quel est le 2nd nombre? ")
while not str.isnumeric(nombre2):
	print("la valeur indiqué n'est pas un nombre")
	nombre2 = input("quel est le 2nd nombre? ")
nombre2 = int(nombre2)
operation = input(f"quelle est l'opération (les possibilités sont {possibilite_operation})? ")
while operation not in possibilite_operation:
			print("Ce n'est pas une opération autorisée")
			operation = input(f"quelle est l'opération (les possibilités sont {possibilite_operation})?")
match operation:
	case "+":
		resultat = nombre1 + nombre2
	case "-":
		resultat = nombre1 - nombre2
	case "*":
		resultat = nombre1 * nombre2
	case "/":
		if nombre2==0:
			print("le dénominateur d'une division ne peut pas être 0")
			raise SystemExit("Fin du programme")
		else:
		 resultat = round(nombre1 / nombre2, 2)
	case _:
		print("nananère")
print(resultat)
