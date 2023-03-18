# Kalkulator Perhitungan Luas Segitiga & Volume Kubur
while True:
    user_pilih = input("Pilih Perhitungan Sederhana, Luas Segitiga, Volume Kubus: ")
    if user_pilih == "perhitungan dasar":
        print("\n", "="*10, "PERHITUNGAN DASAR", "="*10)
        angka_pertama = float(input("Masukkan Angka Pertama: "))
        operator = input("Masukkan Operator: ")
        angka_kedua = float(input("Masukkan Angka Kedua: "))
        
        if operator == "+":
            hasil = angka_pertama + angka_kedua
            print(f'Ini adalah hasil dari pertambahan = {hasil}')
        elif operator == "-":
            hasil = angka_pertama - angka_kedua
            print(f'Ini adalah hasil dari pengurangan = {hasil}')
        elif operator == "*":
            hasil = angka_pertama * angka_kedua
            print(f'Ini adalah hasil dari perkalian = {hasil}')
        elif operator == "/":
            hasil = angka_pertama / angka_kedua
            print(f'Ini adalah hasil dari pembagian = {hasil}')
        
        akhir_pd = input("Akhiri perhitungan? (y/n): ")
        if akhir_pd == "y":
            break

    elif user_pilih == "luas segitiga":
        print("\n", "="*10, "LUAS SEGITIGA", "="*10)
        alas = float(input("Masukkan Alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = alas * tinggi / 2
        print(f'Ini adalah hasil dari luas segitiga = {luas}')

        akhir_pd = input("Akhiri perhitungan? (y/n): ")
        if akhir_pd == "y":
            break

    elif user_pilih == "volume kubus":
        print("\n", "="*10, "VOLUME KUBUS", "="*10)
        sisi = float(input("Masukkan Sisi: "))
        volume = sisi ** 3
        print(f'Ini adalah hasil dari volume kubus = {volume}')
    
        akhir_pd = input("Akhiri perhitungan? (y/n): ")
        if akhir_pd == "y":
            break

print("\n", "="*10, "AKHIR DARI PROGRAM", "="*10)