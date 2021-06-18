import random
def game_random():
    go= random.randint(1,15)
    while True:

        do= int(input("Введите ваше число"))
        print(go)
        if do== go:
             return "красавчик!"
        elif do<go:
            print("холодно")
        elif do>go:
            print ("жарко")

print(game_random())
