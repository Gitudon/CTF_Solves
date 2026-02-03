import math

v1 = 70430356624056699219964353455091734195306937238245707901514922333654568000660
v2 = 5585179348150525015655680494025565656820428601640301759505137819334580532521858
common = math.gcd(v1, v2)


def try_decode(n):
    try:
        return n.to_bytes((n.bit_length() + 7) // 8, "big").decode()
    except:
        return None


for i in range(1, 100):
    if common % i == 0:
        result = try_decode(common // i)
        if result and "Alpaca" in result:
            print(f"Found! (factor {i}): {result}")
            break
