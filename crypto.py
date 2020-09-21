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
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

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
    print(encrypt_caesar("XYZ", 1))
    print(decrypt_caesar("YZA", 1))


if __name__ == "__main__":
    main()
