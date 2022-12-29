#program mengetahui gaji bersi kariwayan dalam setiap bulannya

gaji_pokok=int(input("masukkan gaji pokok : "))

lama_lembur=int(input("masukkan lama lembur : "))

rumus = lama_lembur * 55000 + gaji_pokok

print(rumus)