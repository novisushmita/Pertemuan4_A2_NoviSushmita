a,b=input().split()

if a==b:
    hasil = 'Draw'
elif (a=='[]' and b=='8<') or (a=='[]' and b=='()') or (a=='8<' and b=='()'):
    hasil = 'Pemain B menang'
else:
    hasil = 'Pemain A menang'

print(hasil)