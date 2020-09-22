# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypt = ""
    for char in plaintext:
        if(ord(char) > 64 and ord(char) < 91):
            changed = ord(char) + offset
            if(changed > 90):
                changed = changed - 26
            encrypt = encrypt + chr(changed)
    return encrypt

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decrypt = ""
    for char in ciphertext:
        if(ord(char) > 64 and ord(char) < 91):
            changed = ord(char) - offset
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
    for char in plaintext:
        actualkeyword = actualkeyword + keyword[i]
        if(i == len(keyword) - 1): 
            i = -1
        i = i + 1

    i = 0

    for char in plaintext:
        letter = ord(char) + ord(actualkeyword[i]) - 65
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
    for char in ciphertext:
        actualkeyword = actualkeyword + keyword[i]
        if(i == len(keyword) - 1): 
            i = -1
        i = i + 1

    i = 0

    for char in ciphertext:
        letter = ord(char) - ord(actualkeyword[i]) + 65
        if(letter < 65):
            letter = letter + 26
        decrypt = decrypt + chr(letter)
        i = i + 1

    return decrypt

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
    print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))

if __name__ == "__main__":
    main()
