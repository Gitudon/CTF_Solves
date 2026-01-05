flag = "0x466b776664667c6b72646c7e7a"
decoded_flag = "".join(
    chr(int(flag[i : i + 2], 16) ^ 7) for i in range(2, len(flag), 2)
)
print(decoded_flag)
