def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # No mod inverse if not found

def multiplicative_cipher_encrypt(text, key):
    return ''.join(chr(((ord(c) - 65) * key % 26) + 65) for c in text)

def multiplicative_cipher_decrypt(cipher, key):
    inv = mod_inverse(key, 26)
    return ''.join(chr(((ord(c) - 65) * inv % 26) + 65) for c in cipher)

# 🔤 Define and preprocess the plaintext
plaintext = "I am learning information security".replace(" ", "").upper()

key_mul = 15
cipher_mul = multiplicative_cipher_encrypt(plaintext, key_mul)
decrypted_mul = multiplicative_cipher_decrypt(cipher_mul, key_mul)

print("\nMultiplicative Cipher:")
print("Encrypted:", cipher_mul)
print("Decrypted:", decrypted_mul)


