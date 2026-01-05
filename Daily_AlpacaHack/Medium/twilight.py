def decode_hex_values(hex_values):
    decoded_chars = []

    for i, hex_value in enumerate(hex_values):
        if i % 2 == 0:  # Function 'a' was used
            char_code = hex_value - i
        else:  # Function 'b' was used
            char_code = hex_value ^ i

        decoded_chars.append(chr(char_code))

    return "".join(decoded_chars)


# Provided hexadecimal values
hex_values = [
    0x41,
    0x6D,
    0x72,
    0x62,
    0x67,
    0x64,
    0x81,
    0x46,
    0x74,
    0x79,
    0x6B,
    0x68,
    0x6D,
    0x45,
    0x6F,
    0x6C,
    0x7B,
    0x4E,
    0x7B,
    0x7D,
    0x73,
    0x42,
    0x85,
    0x79,
    0x7C,
    0x7C,
    0x8C,
    0x77,
    0x7D,
    0x73,
    0x82,
    0x62,
]

# Decode the values
decoded_message = decode_hex_values(hex_values)
print("Decoded Message:", decoded_message)
