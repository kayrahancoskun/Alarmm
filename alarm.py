saat=int(input("Lüften saati giriniz"))
if saat<7: 
    print("Uyumaya devam.") 
if saat>7:
    print("geç kaldin acil uyan")
elif saat==7: 
    print("Alarm çaliyor, kalk!") 
else: 
    print("Lütfen bir saat giriniz.") 
