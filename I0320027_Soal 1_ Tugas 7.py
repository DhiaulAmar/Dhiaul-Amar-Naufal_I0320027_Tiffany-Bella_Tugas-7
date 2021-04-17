teks = "Panik ga? Panik ga? Panik lah masa engga"

#membuat string berada di tengah
a = teks.center(70,"*")
print(a)

#mengubah string menggunakan upper dan lower
print(teks.upper())
print(teks.lower())

#mengganti kata panik
b = teks.replace("Panik", "Kaget")
print(b)

#mengitung panjang kalimat
print("Panjang string adalah : ", len(teks))