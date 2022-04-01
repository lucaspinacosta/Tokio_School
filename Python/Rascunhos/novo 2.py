import json

dicc_frutaria = {'Mercearia': [{'Fruta': [{'Nome': 'Maca', 'Quantidade': 10}, {'Nome': 'Pera', 'Quantidade': 20}, {'Nome': 'Laranja', 'Quantidade': 30}]}, {'Verduras': [{'Nome': 'Cenoura', 'Quantidade': 10}, {'Nome': 'Tomate', 'Quantidade': 20}, {'Nome': 'Pepino', 'Quantidade': 30}]}]}

print("tipo de dados:",type(dicc_frutaria))
print("\nDados em Estrutura de Python(dicionario): \n")
print(dicc_frutaria)

json_frutaria = json.dumps(dicc_frutaria)
print("\nDados em JSON:\n")
print(json_frutaria)

print(f"\nTipo de dados {type(json_frutaria)}")

f_dict = json.loads(json_frutaria)
print(f"\n{type(f_dict)}")
print("\n",f_dict['Mercearia'][0])
print("\n",f_dict['Mercearia'][1])
print("\n",f_dict['Mercearia'][0]['Fruta'][0])
