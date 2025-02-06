import string

freq_norm = [0.64297, 0.11746, 0.21902, 0.33483, 1.00000, 0.17541,
             0.15864, 0.47977, 0.54842, 0.01205, 0.06078, 0.31688, 0.18942,
             0.53133, 0.59101, 0.15187, 0.00748, 0.47134, 0.49811, 0.71296,
             0.21713, 0.07700, 0.18580, 0.01181, 0.15541, 0.00583]
    
def letter_frequency(text):
    #Lower teksten grundet at freq er på lower case letters
    text = text.lower()
    letter_count = {letter: 0 for letter in string.ascii_lowercase}
    
    # tæller antallet i texten.
    for char in text:
        if char.isalpha():
            letter_count[char] += 1
    
    total_letters = sum(letter_count.values())

    #Finder ud af hvor mange % der er tilstede, og hvor letter går igen i %.
    letter_percentage = {letter: (count / total_letters) * 100 for letter, count in letter_count.items()}
    return letter_percentage

def calculate_shift(crypt_text):
    frequencies = letter_frequency(crypt_text)

    #Sammenligner teksten vi har nu UDEN at dekryptere det, ser vi på hvor mange der går igen i forhold til freq_norm.
    #Den retunere nu den IKKE dekrypteret text tilbage som er den mest sandsynlige.
    most_frequent_char = max(frequencies, key=frequencies.get)

    shift = (ord(most_frequent_char) - ord('e')) % 26
    return shift

def brute_force_with_frequencies(filename):
    with open(filename, "r") as file:
        crypt_text = file.read()

    print("\nBrute-force forsøger at finde den mest sandsynlige shift ved at analysere hyppigheder:")

    shift = calculate_shift(crypt_text)
    print(f"Den mest sandsynlige shift er: {shift}")
    decrypted_text = decrypt(crypt_text, shift)
    print(f"Dekrypteret tekst med shift {shift}: {decrypted_text}")

    return decrypted_text

def bruteforce(text, crypting_func):
    print("\nBrute-force forsøger alle mulige shifts:")

    array = []

    for shift in range(1, 27):  
        decrypted_text = crypting_func(text, shift)
        array.append(decrypted_text)
        print(f"Shift {shift}: {decrypted_text}")

    return array

def load_file(filename):
    with open(filename, "rb") as f:
        return f.read().decode('utf-8')

def crypt_file():
    with open("txt.txt", "rb") as uncrypted_file:
        file_content = uncrypted_file.read().decode('utf-8')

    crypted_text = crypting(file_content)

    with open("crypted_text.txt", "w") as crypted_file:
        crypted_file.write(crypted_text)

def uncrypt_file(filename):
    encrypted_text = load_file(filename)

    possible_decryptions = bruteforce(encrypted_text, decrypt)

    with open("decrypted_texts.txt", "w") as decrypted_file:
        for idx, text in enumerate(possible_decryptions):
            decrypted_file.write(f"Shift {idx + 1}: {text}\n")

def crypting(text, shift=3):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def decrypt(text, shift=3):
    return crypting(text, shift=-shift)

def bruteforce(text, crypting_func):
    print("\nBrute-force forsøger alle mulige shifts:")

    array = []

    for shift in range(1, 27):  
        decrypted_text = crypting_func(text, shift)
        array.append(decrypted_text)
        print(f"Shift {shift}: {decrypted_text}")

    return array
"""
Kilder:
https://en.wikipedia.org/wiki/Letter_frequency
https://labex.io/tutorials/python-how-to-perform-frequency-analysis-in-python-420898
https://null-byte.wonderhowto.com/how-to/use-beginner-python-build-brute-force-tool-for-sha-1-hashes-0185455/

"""