from pwn import remote
from Crypto.Util.number import isPrime

base_str = "6" * 666
found_prime = ""

# 条件を満たす素数を探す
for i in range(10000):
    candidate_str = base_str + str(i) + "3"
    if isPrime(int(candidate_str)):
        found_prime = candidate_str
        print("[+] 条件を満たす素数を発見しました！")
        break

if not found_prime:
    print("[-] 素数が見つかりませんでした。")
    exit()


io = remote("34.170.146.252", 15827)

io.recvuntil(b"p > ")

io.sendline(found_prime.encode())

result = io.recvall().decode()

print(result.strip())
