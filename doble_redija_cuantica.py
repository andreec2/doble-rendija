
def accimatrizvector(a,b):

    if len(a[0]) == len(b):
        c = [0]*len(a)

    for i in range(len(a)):
        for j in range(len(b)):
                c[i] += a[i][j] * b[j]
    return c

def accimatrizvectortupla(a,b):

    if len(a[0]) == len(b):
        c = [0]*len(a)

    for i in range(len(a)):
        for j in range(len(b)):
                tupla = multiplex(a[i][j],b[j])
                c[i] += tupla
    return c

def matrizxvector(matriz, vector, clips):

    ket_resultante = vector
    for i in range(clips):
        ket_resultante = accimatrizvector(matriz, ket_resultante)

    return ket_resultante

def main():

    matriz =  [[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[0,1/3,0,1,0,0,0,0],[0,1/3,0,0,1,0,0,0],[0,1/3,1/3,0,0,1,0,0],[0,0,1/3,0,0,0,1,0],[0,0,1/3,0,0,0,0,1]]
    matriz2 = [[0,0,0,0,0,0,0,0],
               [1/2**(1/2),0,0,0,0,0,0,0],
               [1/2**(1/2),0,0,0,0,0,0,0],
               [0,(-1+1j)/6**(1/2),0,1,0,0,0,0],
               [0,(-1-1j)/6**(1/2),0,0,1,0,0,0],
               [0,(1-1j)/6**(1/2),(-1+1j)/6**(1/2),0,0,1,0,0],
               [0,0,(-1-1j)/6**(1/2),0,0,0,1,0],
               [0,0,(1-1j)/6**(1/2),0,0,0,0,1]]
    vector = [1j,0,0,0,0,0,0,0]


    ket = matrizxvector(matriz, vector, 2)
    print(ket)

main()




