s = "16f1d4503d9e6e480c36fc9f75f8811fd7cfa3ddd6b1270109890d49535a2f478dc47a4d1f6514525270d40635b28082"
print(s[:32])
d = s[:32]
# Answer, change iv to iv ^ s1 ^s2 after padding them to appropriate length
""" key factor to notice In CBC mode, flipping a byte in the IV or previous
ciphertext block lets you control the corresponding byte
in the decrypted plaintext — use this to flip "admin=False" to "admin=True" without knowing the key."""

def xor_strings_to_hex(s1, s2):
    # Ensure both strings are of equal length
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")

    # XOR each character and convert to hex
    result = ''.join(f"{ord(a) ^ ord(b):02x}" for a, b in zip(s1, s2))
    return result

s1 = "admin=False"
s2 = "admin=True;"
print(xor_strings_to_hex(s1,s2))
print(len(xor_strings_to_hex(s1,s2)))
str = xor_strings_to_hex(s1,s2)+"00"*5
print(str)

a = bytes.fromhex("000000000000121319165e0000000000")
b = bytes.fromhex("16f1d4503d9e6e480c36fc9f75f8811f")

# Ensure both are of same length (if not, truncate or pad b)
b = b.ljust(len(a), b'\x00')  # pad b with zeros if it's shorter

# XOR byte-by-byte
xor_result = bytes(x ^ y for x, y in zip(a, b))

# Convert result to hex
print(xor_result.hex())
