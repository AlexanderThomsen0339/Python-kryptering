def generate_key(msg, key):
    """
    En meget simpel kode. Simpelt laver en nøgle.
    I tilfældet at at den givet nøgle ikke er lang nok, vil koden automatisk gøre den lang nok med den givet nøgle.
    """
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])

    key_join = "".join(key)
    return key_join

def crypting_vigenere(text, key, encrypt=True):
    """
    Ved at sætte encrypting til True/False. Vil koden enten sætte "shift" til
    at begynde at kryptere eller decryptere.
    """
    key = generate_key(text, key)
    result = []

    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i].lower()) - ord('a')
            if not encrypt:
                shift = -shift

            start = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)

    joint_text = "".join(result)
    return joint_text

def encrypt_vigenere(text, key):
    """
    Text er plaintext, som er det der skal krypteres.
    Key er den nøgle som bruges til at kryptere text med.
    Husk at nøgle skal have samme størrelse som text.
    """
    return crypting_vigenere(text, key, encrypt=True)


def decrypt_vigenere(text, key):
    """
    Text er plaintext, som er det der skal krypteres.
    Key er den nøgle som bruges til at kryptere text med.
    Husk at nøgle skal have samme størrelse som text.
    """
    return crypting_vigenere(text, key, encrypt=False)


"""
Kilder:

https://www.geeksforgeeks.org/vigenere-cipher/
https://www.youtube.com/watch?v=SkJcmCaHqS0
https://thepythoncode.com/article/implementing-the-vigenere-cipher-in-python
"""