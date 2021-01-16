# Awal Kode
def faktorial(a):  # Deklarasi fungsi dengan nama faktorial
    if a == 1:  # jika nilai a == 1 maka nilai a akan di return
        return (a)
    else:
        return (a*faktorial(a-1))


# Membuat input
bil = int(input("Masukan Bilangan : "))

# Menampilkan Output
print("%d! = %d" % (bil, faktorial(bil)))
# Akhir Kode
