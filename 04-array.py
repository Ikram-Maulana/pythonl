# Awal kode
print("Program menghitung rata-rata dengan array di python")
print("===================================================")
print("test")

array = []
jumlah = 0

data = int(input("Masukan jumlah banyaknya data : "))

for i in range(0, data):
    nilai = int(input("Masukan nilai ke-%d : " % (i+1)))
    array.append(nilai)

jumlah = sum(array)
rata = jumlah/data

print("\nHasil nilai total adalah : %d" % (jumlah))
print("Hasil rata-rata adalah : %0.2f" % (rata))

# Akhir kode
