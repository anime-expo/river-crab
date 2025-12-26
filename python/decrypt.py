import re

mapping = {"草":0, "泥":1, "马":2}

def convert(array:list[str]) -> list[int]:
    return [mapping[i] for i in array]

def base3_decode(digits: list[int]) -> int:
    value = 0
    for d in digits:
        value = value * 3 + d
    return value

def decrypt_base3(data: list[list[int]]) -> str:
    byte_values = bytes(base3_decode(d) for d in data)
    return byte_values.decode("utf-8")

input_text = input()
decode_data = [list(x) for x in re.sub(r"[^草泥马，]", "", input_text).split("，")]
decode_data = [convert(x) for x in decode_data]
decode_text = decrypt_base3(decode_data)
print(decode_text)