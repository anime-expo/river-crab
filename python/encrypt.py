mapping = ["草", "泥", "马"]

def convert(array:list[int]) -> list[str]:
    return [mapping[i] for i in array]

def base3_encode(n:int) -> list[int]:
    if n == 0:
        return [0]

    digits = []
    while n > 0:
        digits.append(n % 3)
        n //= 3
    return digits[::-1]

def base3_encrypt(text: str) -> list[list[int]]:
    data = text.encode("utf-8")
    return [base3_encode(b) for b in data]

input_text = input()
encode_data = base3_encrypt(input_text)
output_data = [convert(x) for x in encode_data]
output_text = "，".join("".join(row) for row in output_data) + "。"
print(output_text)