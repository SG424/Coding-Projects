import random
x= random.randint(1, 50)
intentos= 5

try:
    while intentos>0:
        Guess=int(input("Guess the number:  "))
        if Guess > 50 or Guess < 1:
            raise Warning("Tu numero esta fuera del limite")
        if Guess==x:
            print("Correct!")
            break
        else: 
            intentos-=1
            if Guess>x:
                print("Too High")
            else:
                print("Too Low")

except Warning as e:
    print(e)

except ValueError as e:
    print("Asegúrate de escribir un número entero válido.")

else:
    pass


