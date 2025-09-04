age = int(input('age: '))
price = 100
result = "Yakuniy narx: {} so'm ({} chegirma qo'llanildi)"
if age >= 0 and age <= 6:
    print(result.format( (price - (price * 0.50)),"50%" ) )
elif age >= 7 and age <= 17:
    print(result.format( (price - (price * 0.20)),"20%" ) )
elif age >=18 and age <= 60:
    print(result.format( (price),"0%" ) )
elif age > 60:
    print(result.format( (price - (price * 0.30)),"30%" ) )
else:
    print('Xato yosh kiritildi!')