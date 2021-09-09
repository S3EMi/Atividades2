def restart():
    def gotor():
        pause()
        restart()

    def pause():
        input("\nPressione ENTER para continuar...")
        
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    num3 = float(input("Terceiro número: "))

    def vd():  
        print("Valores foram dados como: ", num1, num2, num3)

    if (num1 > num2) and (num1 > num3) and (num2 > num3):
        print(num1, ", ", num2, ", ", num3)
        vd()
        gotor()
    elif (num1 > num2) and (num1 > num3) and (num2 < num3):
        print(num1, ", ", num3, ", ", num2)
        vd()
        gotor()
    elif (num2 > num1) and (num2 > num3) and (num1 > num3):
        print(num2, ", ", num1, ", ", num3)
        vd()
        gotor()
    elif (num2 > num1) and (num2 > num3) and (num3 > num1):
        print(num2, ", ", num3, ", ", num1)
        vd()
        gotor()
    elif (num3 > num1) and (num3 > num2) and (num1 > num2):
        print(num3, ", ", num1, ", ", num2)
        vd()
        gotor()
    elif (num3 > num1) and (num3 > num2) and (num2 > num1):
        print(num3, ", ", num2, ", ", num1)
        vd()
        gotor()

restart()