#definimos las variables
n1:int
n2:int
#pedimos al usuario los datos
n1=int(input("ingrese un valor para asignarle a n1: " ))
n2=int(input("ingrese un valor para asignarle a n2: " ))

#hacemos lo que seria aplicar las operaciones
suma=n1+n2
resta=n1-n2
multiplicacion=n1*n2

#resultado 
print("la suma de ", n1 , "+" ,n2, " da como resultado: " ,suma,)
print("la suma de " ,n1, "-" ,n2, " da como resultado: ", resta,)
print("la suma de " ,n1, "*" ,n2, " da como resultado: " ,multiplicacion,)