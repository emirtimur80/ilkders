meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Legue Of Legends",
            "CS" : "Counter Strike",
            "TFT": "Team Fight Tactics",
            "MC" : "Minecraft"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Böyle bir kelime yok")
