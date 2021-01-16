#list absensi item nama dan nim
absensi = [{'nama': 'resita','nim': '1930511052'},
{'nama':'reski','nim': '1930511051'}
]

#append berfungsi menambahkan item kedalam list diakhir 
absensi.append({'nama': 'ikram','nim':'1930511059'})

#nama saya
pembuat = {'nama':'Drajat','nim':'1930511053'}

#menampilkan data list
for row in absensi:
        print(row['nama'],'-',
        row['nim'])
        
print()
print("ini dibuat oleh",pembuat['nama'])
print("prodi : teknik informatika B")    