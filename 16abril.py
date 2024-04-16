meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso", 
            "CREEPY": "Aterrador, siniestro",
            "XD": "Cara volteada riendo","ROFL": "Respuesta a broma",
            "NTP": "No te preocupes", 
            "SMN": " Abreviatura de Simon, significa sí",
            "BV": "Carita con lentes y boca abierta"
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!):")

if word in meme_dict.keys():
    print("Significado:",meme_dict[word])
else:
    print("No se encuentra en el diccionario")
