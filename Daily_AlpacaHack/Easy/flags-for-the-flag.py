def decode_risl(s):
    decoded = ""
    for c in s:
        b = c.encode("utf-8")
        if len(b) == 4 and b[0] == 0xF0 and b[1] == 0x9F and b[2] == 0x87:
            original_char = chr(b[3] - 0xA6 + ord("A"))
            decoded += original_char
        else:
            decoded += c

    return decoded


c = "🇦🇱🇵🇦🇨🇦{🇴🇲🇬🇮🇳🇺🇳🇮🇨🇴🇩🇪🇹🇭🇪🇸🇵🇪🇨🇮🇫🇮🇨🇵🇦🇮🇷🇸🇬🇮🇻🇪🇺🇸🇹🇭🇪🇸🇵🇪🇨🇮🇫🇮🇨🇲🇪🇦🇳🇮🇳🇬}"
result = decode_risl(c)
# flag format: Alpaca{[a-z]+}
result = result.replace("ALPACA{", "Alpaca{")
ans = ""
for i in range(len(result)):
    if i < 7 or i >= len(result) - 1:
        ans += result[i]
    else:
        ans += chr(ord(result[i]) + 32)

print(ans)
