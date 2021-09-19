 #(7,4)Hammingcode berechnen
#C Nicode3141 2021: github.com/nicode3141

#Funktionsweise:
#Binärzahl in die Konsole eingeben
K = 4


def encode(s):

    while len(s) >= K:
        nibble = s[0:K]
        input(hamming(nibble))
        s = s[K:]

def hamming(bits):
    p1 = parity(bits, [0,1,3])
    p2 = parity(bits, [0,2,3])
    p3 = parity(bits, [1,2,3])
    return bits[0:] +p1 +p2 +p3
   # return p1 + p2 + bits[0] + p3 + bits[1:]#p1,p2,d1,p3,d2,d3,d4

def parity(s, präbi):

    sub = ""
    for i in präbi:
        sub += s[i]
    return str(str.count(sub, "1") % 2)

if __name__ == "__main__":
    print("Input:")
    input_string = input().strip()
    print(" Output:",end=' ')
    encode(input_string)
