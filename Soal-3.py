teori = float(input("Nilai teori murid ="))
praktek = float(input("Nilai praktek murid ="))
kkm = 70
if teori >= kkm and praktek >= kkm:
    print("Selamat, anda lulus!")
elif teori >= kkm and praktek <= kkm:
    print("Anda harus mengulang ujian praktek.")
elif teori <= kkm and praktek >= kkm:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")