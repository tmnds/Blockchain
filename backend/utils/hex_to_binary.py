from backend.utils.crypto_hash import crypto_hash

HEX_TO_BINARY_COVERSION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def hex_to_binary(hex_string):
    binary_string = ''

    for character in hex_string:
        binary_string+=HEX_TO_BINARY_COVERSION_TABLE[character]

    return binary_string

def main():
    number = 9981
    hex_number = hex(number)[2:]
    print(f'hex_number: {hex_number}')
    
    binary_number = hex_to_binary(hex_number)
    print(f'binary_number: {binary_number}')

    original_number = int(binary_number, 2)
    print(f'original_number: {original_number}')

    crypto_hash_to_binary = hex_to_binary(crypto_hash('foo-data'))
    print(f'crypto_hash_to_binary: {crypto_hash_to_binary}')

if __name__ == '__main__':
    # hex_to_binary('55a9f4f8994b1bbf2058ea38c8efb6c459000814d5f39c087002571639e6230e')
    main()