dicc_frutas_1 = {"Nome":"Maca",
					"Quantidade":10}
					
dicc_frutas_2 = {"Nome":"Pera",
					"Quantidade":20}

dicc_frutas_3 = {"Nome":"Laranja",
					"Quantidade":30}

dicc_verduras_1 = {"Nome":"Cenoura",
						"Quantidade":10}

dicc_verduras_2 = {"Nome":"Tomate",
						"Quantidade" : 20}

dicc_verduras_3 = {"Nome":"Pepino",
						"Quantidade":30}
						
lista_frutas = [dicc_frutas_1,dicc_frutas_2,dicc_frutas_3]

lista_verduras = [dicc_verduras_1,dicc_verduras_2,dicc_verduras_3]

dicc_fruta = {"Fruta":lista_frutas}
dicc_verduras = {"Verduras" : lista_verduras}

mercearia = {"Mercearia" : [dicc_fruta,dicc_verduras]}

print(mercearia)

