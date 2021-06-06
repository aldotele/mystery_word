import base64


def decode_word(encoded_word):
    word_bytes = encoded_word.encode('ascii')
    decoded_bytes = base64.b64decode(word_bytes)
    decoded_word = decoded_bytes.decode('ascii')  # this will be the readable word
    return decoded_word
