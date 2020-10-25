# Awal Kode
def fibonacci(n):  # Deklarasi fungsi dengan nama fibonnaci
    if n == 0 or n == 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


# Input
x = int(input("Masukan Batas Deret Bilangan Fibonacci : "))

# Menampilkan Output
print("================")
print("Deret Fibonacci ")
for i in range(x):
    print(fibonacci(i), end=' ')
# Akhir Kode
