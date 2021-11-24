data=[]
while(True):
    NIM=input("masukan NIM: ")
    Nama=input("masukaan Nama: ")
    Tugas=input("masukan Tugas: ")
    UTS=input("masukan UTS: ")
    UAS=input("masukaan UAS: ")
    Akhir=(int(Tugas)*.30)+(int(UTS)*.35)+(int(UAS)*.35)
    data.append([NIM, Nama, Tugas, UTS, UAS, Akhir])
    ulangi=input("Tambah data (y/t)?")
    if ulangi .lower()== 't' :
        break

print("\nDaftar Nama\n")
print("==================================================")
print("|  NIM  |  Nama  | Tugas | UTS |  UAS  |  Akhir  |")
print("==================================================")
for x in data:
    print("|  {0:1}  |  {1:1}  |  {2:1}  |  {3:1}  |  {4:1}  |  {5:1}  |".format(x[0], x[1], x[2], x[3], x[4], x[5]))
print("==================================================")