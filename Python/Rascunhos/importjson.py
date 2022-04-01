import json
f = '{"Frutaria":[{"Fruta":[{"Nome":"Ananas","Quantidade":10},{"Nome":"Pera","Quantidade":20},{"Nome":"Laranja","Quantidade":30}]},{"Verduras":[{"Nome":"Alface","Quantidade":10},{"Nome":"Tomate","Quantidade":20},{"Nome":"Pepino","Quantidade":30}]}]}'
f_dict = json.loads(f)
print(f"\nDados completos (tipo {type(f_dict)})")
print(f_dict,"\n")

print("\nJSON Object Fruta")
print(f_dict['Frutaria'][0]['Fruta'][1])
print("\nNumero de Peras")
print(f_dict['Frutaria'][0]['Fruta'][1]['Quantidade'])