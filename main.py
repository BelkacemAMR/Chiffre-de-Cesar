def caesar_cypher_encrypt(s, offset):
    enc_chars = str.maketrans(
        f'{chars[0]}{chars[1]}',
        f'{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}'
    )
    return str.translate(s, enc_chars)


def caesar_cypher_decrypt(s, offset):
    dec_chars = str.maketrans(
        f'{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}',
        f'{chars[0]}{chars[1]}'
    )
    return str.translate(s, dec_chars)