import random
import os

def select_word():
    with open("./data.txt","r",encoding="utf-8") as f:
        a = random.choice(list(f)).strip()
        return a
        
        
def run():
    con = 20
    win = 0
    b = select_word()
    bb = b #for detecting repeating words
    c = {i:"-" for i in range(0,len(b))}

    print("Bienvenido al juego EL AHORCADO")
    print("\n"," ".join(list(c.values())))
    

    while con > 0:
        a = input("Ingresa una letra: ")
        msg = "Intenta otra letra diferente a la " + a
        os.system('cls')
        for count, value in enumerate(bb):
            if value==a:
                c[count] = a
                bb = bb.replace(a,"/",1)
                win += 1
                msg="Correcto, sigue asi"
                if win == len(b):
                    con = 0
    
        con -= 1 
        
        if con == -1:
            print("GANASTE. La palabra es: " + b)
        elif con == 0:
            print("PERDISTE. La palabra era: " + b)
        elif con != -1:
            print(" Tienes " + str(con) + " intentos.","\n")  
            print(msg)
            print(bb)

        print("\n"," ".join(list(c.values())),"\n")     

    
if __name__ == "__main__":
    run()
