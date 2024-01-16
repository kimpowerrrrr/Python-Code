import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_cipher = False

def caesar(text, shift, direction):
    for letter in text:
        if letter in alphabet:

            position = alphabet.index(letter) + 1
            if direction.lower() == "encode":
                new_position = position + shift
                while new_position > len(alphabet):
                    new_position = new_position - len(alphabet)

                shifted_letters.append(alphabet[new_position - 1])

            elif direction.lower() == "decode":
                new_position = position - shift
                new_position = new_position + len(alphabet)
                while new_position > len(alphabet):
                    new_position = new_position - len(alphabet)
                    print(alphabet[new_position - 1])

                shifted_letters.append(alphabet[new_position - 1])    
        else:
            position = text.index(letter)
            shifted_letters.append(text[position])

    message = ''.join(shifted_letters)
    print(f"{direction}d message: {message}")

print(art.logo)

while end_cipher == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shifted_letters = []

    shift = shift % 26
    caesar(text, shift, direction)

    continue_use = input("Do you want to continue? Y/N\n")
    if continue_use.lower() == "n":
        print("Goodbye!")
        end_cipher = True

