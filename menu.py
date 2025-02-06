import ceaser as ce
import vigenere as vi

if __name__ == '__main__':
    while True:
        result = input("\n1 for Caesar kryptering, 2 for Caesar dekryptering, 3 for Caesar brute-force, 4 for krypter fil, 5 for dekrypter fil, 6 for brute-force med hyppigheder, 7 for Vigenère kryptering, 8 for Vigenère dekryptering, 9 for afslut: ")

        if result == "1":
            input_string = input("Indtast den tekst, du vil kryptere: ")
            encrypted_text = ce.crypting(input_string)
            print(f"Krypteret tekst: {encrypted_text}")

        elif result == "2":
            input_string = input("Indtast den tekst, du vil dekryptere: ")
            decrypted_text = ce.decrypt(input_string)
            print(f"Dekrypteret tekst: {decrypted_text}")

        elif result == "3":
            input_string = input("Indtast den krypterede tekst, du vil brute-force: ")
            ce.bruteforce(input_string, ce.decrypt)

        elif result == "4":
            ce.crypt_file()

        elif result == "5":
            filename = input("Indtast filnavnet på den krypterede fil, du vil dekryptere: ")
            ce.uncrypt_file(filename)

        elif result == "6":
            filename = input("Indtast filnavnet på den krypterede fil, du vil brute-force med hyppigheder: ")
            ce.brute_force_with_frequencies(filename)

        elif result == "7":
            input_string = input("Indtast den tekst, du vil kryptere med Vigenère: ")
            key = input("Indtast nøglen: ")
            encrypted_text = vi.encrypt_vigenere(input_string, key)
            print(f"Krypteret tekst: {encrypted_text}")

        elif result == "8":
            input_string = input("Indtast den tekst, du vil dekryptere med Vigenère: ")
            key = input("Indtast nøglen: ")
            decrypted_text = vi.decrypt_vigenere(input_string, key)
            print(f"Dekrypteret tekst: {decrypted_text}")

        elif result == "9":
            print("Afslutter programmet.")
            break