meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            'GG': 'Tanggapan terhadap sesuatu yang keren',
            'NT': 'Tanggapan atas kegagalan menang main game'
            }


while True:
            word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
            
            if word in meme_dict.keys():
                # Apa yang harus kita lakukan jika kata itu ditemukan?
                print(meme_dict[word])
                break        
            else:
                # Apa yang harus kita lakukan jika kata itu 
                print('KATA TERSEBUT TIDAK VALID')
