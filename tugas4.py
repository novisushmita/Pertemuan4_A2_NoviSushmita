#kode program yang terdapat kesalahan
a='a'
i='i'
u='u'
e='e'
o='o'
jml_a=0
jml_i=0
jml_u=0
jml_e=0
jml_o=0

n=input().lower()
kata=list(n)

if(a in kata):
    jml_a=kata.count('a')
if(i in kata):
    jml_a=kata.count('b')
if(u in kata):
    jml_a=kata.count('u')
if(e in kata):
    jml_a=kata.count('e')
if(o in kata):
    jml_a=kata.count('o')
    
total = jml_a+jml_i+jml_u+jml_e+jml_o
print(total)

"""
#kode program yang telah diperbaiki
a='a'
i='i'
u='u'
e='e'
o='o'
jml_a=0
jml_i=0
jml_u=0
jml_e=0
jml_o=0

n=input().lower()
kata=list(n)

if(a in kata):
    jml_a=kata.count('a')
if(i in kata):
    jml_a=kata.count('i')
if(u in kata):
    jml_a=kata.count('u')
if(e in kata):
    jml_a=kata.count('e')
if(o in kata):
    jml_a=kata.count('o')
    
total = jml_a+jml_i+jml_u+jml_e+jml_o
print(total)
"""
