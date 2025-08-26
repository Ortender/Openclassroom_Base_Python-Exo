possibilite_operation = ["+","-","*","/"]
nombre1 = input("quel est le premier nombre? ") 
nombre2 = input("quel est le 2nd nombre? ")
if str.isnumeric(nombre1)==False or str.isnumeric(nombre2)==False:
	print("la valeur indiqué n'est pas un nombre")
	raise SystemExit("Fin du programme")
else: 
	nombre1 = int(nombre1)
	nombre2 = int(nombre2)
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
		print("Ce n'est pas une opération autorisée")
		raise SystemExit("Fin du programme")
print(resultat)
