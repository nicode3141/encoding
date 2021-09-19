#Paritätsbit berechnen
#C Nicode3141 2021: github.com/nicode3141

#Funktionsweise:
#Binärzahl in die Konsole eingeben

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def calculation():

    binstring = str(binnum)
    ones = binstring.count('1')

    onesint = int(ones)
    if (onesint % 2) == 0:
        parity = '0₂'
    if(onesint % 2) != 0:
        parity = '1₂'

    print(colored(255, 0, 102, binstring)+colored(255, 0, 200,parity))
    return


while True:
    try:
        binnum = int(input("Geben sie hier ihre Binärzahl ein:"))
    except ValueError:
        print("Nummer nicht erkannt.Bitte Zahl in Binär eingeben!")
    else:
        for i in str(binnum):
            if i in '10':
                binary = True
            else:
                binary = False
                break
        if binary == False:
            print("Nummer nicht erkannt.Bitte Binärzahl eingeben!")
        else:
            break

calculation()


