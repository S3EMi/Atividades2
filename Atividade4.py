def restart():
    def gotor():
        pause()
        restart()

    def pause():
        input("Pressione ENTER para continuar...")

    numbx = float(input("Digite o x: "))
    numby = float(input("Digite o y: "))

    if (numbx == 0) and (numby == 0):
        print("Origem")
        gotor()
    elif (numbx > 0 or numbx < 0) and (numby == 0):
        print("Eixo X")
        gotor()
    elif (numby > 0 or numby < 0) and (numbx == 0):
        print("Eixo Y")
        gotor()
    elif (numbx > 0) and (numby > 0):
        print("Q1")
        gotor()
    elif (numbx < 0) and (numby > 0):
        print("Q2")
        gotor()
    elif (numbx < 0) and (numby < 0):
        print("Q3")
        gotor()
    elif (numbx > 0) and (numby < 0):
        print("Q4")
        gotor()
    
restart()