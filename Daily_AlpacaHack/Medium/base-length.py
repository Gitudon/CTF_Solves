from base64 import *

bite_15_data = "AAAAAAAAAAAAAAA"
bite_15_b32 = b32encode(bite_15_data.encode()).decode().rstrip("=")
bite_15_b64 = b64encode(bite_15_data.encode()).decode().rstrip("=")

print(f"Bite-15 Base32 : '{bite_15_b32}'")
print(f"Bite-15 Base64 : '{bite_15_b64 + " " * 10}'")
