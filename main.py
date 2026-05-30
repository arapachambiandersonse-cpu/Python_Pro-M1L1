meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "SHEESH" : "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "WTF": "Expresion de gran sorpresa"
            }
print("Hola, sea bienvenido al programa de DICCIONARIO MODERNO, escriba alguna palabra que usted desconozca")

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
    
        print(meme_dict[word])
    else:
    
        print("No tenemos esa palabra en el diccionario, pero no te preocupes pronto añadiremos tu sugerencia")
