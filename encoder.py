import string

def generate_vigenere_table():
    table = {}
    for i, char in enumerate(string.ascii_uppercase):
        shifted_alphabet = string.ascii_uppercase[i:] + string.ascii_uppercase[:i]
        table[char] = shifted_alphabet
    return table

def generate_key(message, key):
    key = key.upper()
    key_index = 0
    extended_key = ''
    for char in message:
        if char in string.ascii_uppercase:
            extended_key += key[key_index]
            key_index = (key_index + 1) % len(key)
        else:
            extended_key += char
    return extended_key

def encrypt(message, key):
    vigenere_table = generate_vigenere_table()
    key = generate_key(message, key)
    encrypted_text = ''
    for i, char in enumerate(message):
        if char in string.ascii_uppercase:
            row = key[i]
            col = char
            encrypted_text += vigenere_table[row][string.ascii_uppercase.index(col)]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    vigenere_table = generate_vigenere_table()
    key = generate_key(ciphertext, key)
    decrypted_text = ''
    for i, char in enumerate(ciphertext):
        if char in string.ascii_uppercase:
            row = key[i]
            col = vigenere_table[row].index(char)
            decrypted_text += string.ascii_uppercase[col]
        else:
            decrypted_text += char
    return decrypted_text

def main():
    message = ""
    while True:
        line = input("Enter a line of text (or 'done' to finish): ").strip()
        if line.lower() == 'done':
            break
        message += line.upper()

    key = input("Enter the keyword: ").upper()

    encrypted = encrypt(message, key)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
