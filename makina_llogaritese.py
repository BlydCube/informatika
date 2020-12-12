#---------------------------------------------
# Funksionet matematikore
def shuma(a, b):
    return(a + b)
def zbritje(a,b):
    return (a - b)
def prodhimi(a, b):
    return (a * b)
def raporti(a, b):
    return (a / b)
def fuqi(a, b) :
    return (a ** b)
#---------------------------------------------------------
#Mesazhi hyres
print('--------------------------------\nveprimet e mundshme jane:\nshuma: +\nzbritje: -\nprodhimi: *\nraporti: /\nngritje ne fuqi: ^\n-------------------------------')
#----------------------------------------------------------
n = input('vendos numrat dhe veprimin e deshiruar ne formen "a + b":  ')
m = n.split()
#---------------------------------------------------------

if m[1] == '+':
    print('= '+str(shuma(int(m[0]),int(m[2]))))
elif m[1] == '-':
    print('= '+str(zbritje(int(m[0]),int(m[2]))))
elif m[1] == '*':
    print('= '+str(prodhimi(int(m[0]),int(m[2]))))
elif m[1] == '/':
    print('= '+str(raporti(int(m[0]),int(m[2]))))
elif m[1] == '^':
    print('= '+str(fuqi(int(m[0]),int(m[2]))))
else:
    print('vendos numra natyrore dhe simbolet e pershatshme')
