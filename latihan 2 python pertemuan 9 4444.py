#Buat sebuah lits sebayah 5 elemen dengan nilai bebas
el=[1,2,3,"akmal","kurang","makan"]
print(el)
print
#Tampilan elemen 3
print("elemen ketiga=>",el[3])
print(el)
print("elemen ke 2 s/d 4 => ",el[2:4])
print(el)
print("elemen terakhir=> ",el[-1])
print(el)
print("=====Perubahan Elemen=====")
print("mengubah cinta menjadi benci")
el[4]="benci"
print(el)
#ubah elemen 4 sampai dengan elemen terakhir
el[4],el[5]="sayang","jantung"
print("perubahan elemen 4-akhir=> ",el)
print(el)
print()
print("###dibawah ini list baru###")
print()
el2=[10,11,12,13,14,15]
print("list el2 =>",el2)
print()
print("menggabungkan sebagaian dari elemen el ke el2")
elemen=el+el2
el.extend(el)
print(el2)
      
