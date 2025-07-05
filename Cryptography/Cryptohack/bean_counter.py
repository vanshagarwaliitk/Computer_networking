## Bean Counter
import requests
url = "https://aes.cryptohack.org/bean_counter/encrypt/"
response = requests.get(url)
ciphertext = response.json()['encrypted']
# print(ciphertext)
print(len(ciphertext))
# 00 00 00 0D
# 49 48 44 52
# 89504E470D0A1A0A0000000D49484452
signature = bytes.fromhex("89504E470D0A1A0A0000000D49484452")
cipher_block_0 = bytes.fromhex(ciphertext[:32])  # First 8 bytes (16 hex chars)

# Recovered 8-byte keystream
keystream = bytes([x ^ y for x, y in zip(signature, cipher_block_0)])

decrypted = []

i = 0
while 32 * (i + 1) <= len(ciphertext):  # each block is 16 hex chars = 8 bytes
    block_hex = ciphertext[i * 32:(i + 1) * 32]  # 16 hex chars per 8-byte block
    block = bytes.fromhex(block_hex)
    
    # XOR block with 8-byte keystream
    plain = bytes([a ^ b for a, b in zip(block, keystream)])
    
    decrypted.append(plain)
    i += 1
print(decrypted)

with open("recovered_partial.png", "wb") as f:
    f.write(b''.join(decrypted))

