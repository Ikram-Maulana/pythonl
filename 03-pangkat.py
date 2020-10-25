# Awal Kode
def pangkat(x, y):  # Deklarasi fungsi dengan nama pangkat
    if y == 0:
        return 1
    else:
        return x * pangkat(x, y-1)


# Input
x = int(input("Masukan Nilai X : "))
y = int(input("Masukan Nilai Y : "))

# Menampilkan Output
print("%d dipangkatkan %d = %d" % (x, y, pangkat(x, y)))
# Akhir Kode
