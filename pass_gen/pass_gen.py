import hashlib

from js import document, navigator


def convert_base(x: int, limited_characters: bool = False) -> str:
    if limited_characters:
        CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" \
                + "_-" * 5
        BASE = len(CHARS)
    else:
        START, END = 33, 127
        CHARS = "".join(chr(c) for c in range(START, END))
        BASE = END - START

    result = []
    while True:
        x, r = x // BASE, x % BASE
        result.append(CHARS[r])
        if x == 0:
            break

    return "".join(result[::-1])


def pass_gen(p: str, max_len: int = 16, limited_characters: bool = False) -> str:
    hs = hashlib.sha256(p.encode()).hexdigest()
    hs_int = int(hs, 16)
    converted_pass = convert_base(
        hs_int, limited_characters=limited_characters)
    return converted_pass[:max_len]
