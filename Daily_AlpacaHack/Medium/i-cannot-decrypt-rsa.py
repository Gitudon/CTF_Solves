import math
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse

n = 121171405093237217063227091172111185824248557962241995647996651518028003422004265461446978461128670887791544521942407383833048111248151442041011392122935068929002416630648052784801292541758655639201511448785066170672299107294278226935064116631227052642961885774807709471051084305123234900517439397737934065023
e = 65537
phi = 121171405093237217063227091172111185824248557962241995647996651518028003422004265461446978461128670887791544521942407383833048111248151442041011392122935091315818127868894450561134101711214249383744038537542940920232549769137343118351526052753080295420884439664114630356220739171908973211717355798463354554088
flag = b'N$\x9d_\x982\xb6\xb0b\x1c=K\x05\xd3]\xe2\x14_g8\xfbDTo\x07\xa3\xd6\xf42X\xc7f)\x0c(\x1e\x9ca\xbbL?\xb3\xaah\xe29R\xf8\xad\xa2\x0b\xc5\x0b\xf5\xc7\xfb\x9d\xd9\x98x\xa7C\xd3-\xe8\x18\xa2\x18\x05\xa5"\x86\xd7\xa9\x80\xdbi\xbe\x16\x81k\xce\x8c@>x\x93\x9eG\x1f\x06\x11R\x03\x95/h6\xe3\x1b\xf5\xaed\x99p(\xed]\xd0\xa1%\xe7uKvX\x05lc\x0e\xf1\xd9\xa5\xad\xbc\xb8>C'

# 偽のメッセージを整数に戻す
m_wrong = bytes_to_long(flag)

# p + q を計算
sum_pq = phi - n - 1

# 2次方程式 x^2 - sum_pq*x + n = 0 を解く
# 判別式 D = (p+q)^2 - 4pq
D = sum_pq**2 - 4 * n
sqrt_D = math.isqrt(D)

p = (sum_pq + sqrt_D) // 2
q = (sum_pq - sqrt_D) // 2

# 検証
assert p * q == n

# 正しい phi と、間違った d を用意
phi_correct = (p - 1) * (q - 1)
d_wrong = inverse(e, phi)

try:
    # 間違った d_wrong の逆元を取って、暗号文 c を復元
    d_inv = inverse(d_wrong, phi_correct)
    c = pow(m_wrong, d_inv, n)
    # 正しい秘密鍵で本来のメッセージ m を復元
    d_correct = inverse(e, phi_correct)
    m = pow(c, d_correct, n)
    print(f"Flag: {long_to_bytes(m).decode()}")
except Exception as err:
    print(f"復元エラー: {err}")
