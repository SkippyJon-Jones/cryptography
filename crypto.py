import random
import math
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypt = ""
    

    for char in plaintext:
        #checks if the character is a valid one to shift
        if(ord(char) > 64 and ord(char) < 91):
            changed = ord(char) + offset
            #checks if the shift goes over the ascii value for z
            if(changed > 90):
                changed = changed - 26
            encrypt = encrypt + chr(changed)
    return encrypt

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decrypt = ""

    for char in ciphertext:
        #checks if the character is a valid one to shift back
        if(ord(char) > 64 and ord(char) < 91):
            changed = ord(char) - offset
            #checks if the shift goes under the ascii value for a
            if(changed < 65):
                changed = changed + 26
            decrypt = decrypt + chr(changed)
    return decrypt

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encrypt = ""

    actualkeyword = ""

    i = 0
    #creates a new string that is the keyword repeating itself
    #  to become an equal length to the plain text
    for char in plaintext:
        actualkeyword = actualkeyword + keyword[i]
        #resets the indices that is looping through the original keyword
        if(i == len(keyword) - 1): 
            i = - 1
        i = i + 1

    i = 0

    for char in plaintext:
        letter = ord(char) + ord(actualkeyword[i]) - 65
        #checks to see if the character needs to loop around 
        # to beginning of alphabet
        if(letter > 90):
            letter = letter - 26
        encrypt = encrypt + chr(letter)
        i = i + 1

    return encrypt

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decrypt = ""

    actualkeyword = ""

    i = 0

    #creates a new string that is the keyword repeating itself
    #  to become an equal length to the plain text
    for char in Cipherertext:
        actualkeyword = actualkeyword + keyword[i]
        #resets the indices that is looping through the original keyword
        if(i == len(keyword) - 1): 
            i = -1
        i = i + 1

    i = 0

    for char in ciphertext:
        letter = ord(char) - ord(actualkeyword[i]) + 65
        #checks to see if the character needs to loop around 
        # to end of alphabet
        if(letter < 65):
            letter = letter + 26
        decrypt = decrypt + chr(letter)
        i = i + 1

    return decrypt

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    w = [1]
    i = 1
    total = 1
    #creates a random superincreasing sequence that starts at 1
    while i < n:
        w.append(random.randint(total+1, 2*total))
        total = total + w[i]
        i = i + 1

    W = tuple(w)

    #creates a Q value that is larger than the largest element in W
    Q = random.randint(total+1, 2*total)

    #finds an R value where its greatest common denominator with Q is 1
    while 1 == 1:
        R = random.randint(2, Q-1)
        if math.gcd(R,Q) == 1:
            break

    return (W, Q, R)

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: B - a length-n tuple of integers
def create_public_key(private_key):
    b = []
    W, Q, R = private_key
    #modifies W, the list of superincreasing values, to creat a public key
    for W_i in W:
        b.append((R * W_i) % Q)

    B = tuple(b)

    return B

## Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    listofCs = []

    for letter in plaintext:
        #converts each char in plaintext into its binary value
        # using 8 digits
        asciiValue = ord(letter)
        binaryvalue = '{0:08b}'.format(asciiValue)
        M = []

        #converts it from the binary value into a list of 
        # the binary representation
        for num in binaryvalue:
            M.append(num)

        j = 0
        C = 0
        #creates a C value that is a representation 
        # of the individual character
        for M_i in M:
            C = C + (int(M_i) * public_key[j])
            j = j + 1

        #add each C value to the list
        listofCs.append(C)

    return listofCs

# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    decryptchars = []
    W, Q, R = private_key

    #generates an S value that satisfies the equation below
    for S in range(2, Q):
        if ((S * R)%Q == 1):
            break
    C2 = []

    #creates a modified list of values from the ciphertext 
    for C in ciphertext:
        C2.append((C * S)%Q)


    for Cval in C2:
        indicesInOriginal = []
        #starts index at top of the list
        i = len(W) - 1
        #loops through the superincreasing list comparing its 
        #values with the C value
        while i > -1:
            #if its larger then go onto the next, smaller integer
            if(W[i] > Cval):
                i = i - 1
            else:
                #if smaler, subtract it from the C value
                Cval = Cval - W[i]
                #the index of the super increasing starts from the top so
                # to get the index where there is a 1 in the binary representation
                # have to subtract the index from the total number of indices
                indicesInOriginal.append(len(W) - i)
                i = i -1
            #once the C value is 0 there are no more binary values to be added
            if Cval == 0:
                break
        asciival = 0
        #loops through where the indices are in the binary value 
        #  of the original string and computes its asciivalue
        for x in indicesInOriginal:
            asciival = asciival + (2 ** (x-1))
        #converts the asciival to a char and adds 
        # it to the list of the original text
        decryptchars.append(chr(asciival))

    return decryptchars

def main():
    x = (generate_private_key())
    y = (create_public_key(x))
    print(y)

    z = (encrypt_mhkc("ADAM", y))

    print(decrypt_mhkc(z, x))



if __name__ == "__main__":
    main()
