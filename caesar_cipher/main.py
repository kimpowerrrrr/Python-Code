import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):

    for letter in text:
        position = alphabet.index(letter) + 1
        if direction.lower() == "encode":
            new_position = position + shift
            print(f"starting position: {new_position} \nletter position: {position} \ntotal index of alphabet: {len(alphabet)}")

            while new_position > len(alphabet):
                new_position = new_position - len(alphabet)
                print(f" test new position: {new_position}")

            shifted_letters.append(alphabet[new_position - 1])
            #else:
            #    shifted_letters.append(alphabet[new_position])
        elif direction.lower() == "decode":
            new_position = position - shift

            while new_position > len(alphabet):
                new_position = new_position + len(alphabet)
                print(f" test new position: {new_position}")

            shifted_letters.append(alphabet[new_position - 1])    
            #if new_position > len(alphabet):
            #    new_position = new_position + len(alphabet)
            #    shifted_letters.append(alphabet[new_position])
            #else:
            #    shifted_letters.append(alphabet[new_position])

    message = ''.join(shifted_letters)
    print(f"{direction}d message: {message}")

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shifted_letters = []

caesar(text, shift, direction)

