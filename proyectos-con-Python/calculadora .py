numero1=int(input("Di un numero "))
numero2=int(input("Di otro numero "))
operacion=input("Que operación:suma,resta, multiplicacion, división ")
if operacion=="suma":
    operacion="suma"
    print(numero1+numero2)
elif operacion=="resta":
    operacion="resta" 
    print(numero2-numero1)
elif operacion=="multiplicacion":
    operación="multiplicación"
    print(numero1*numero2)
elif operacion=="division":
    operacion="división "
    print(numero1/numero2)