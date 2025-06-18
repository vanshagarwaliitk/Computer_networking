import requests
import string

# Oracle URL function
def get_ciphertext(plaintext_hex):
    url = f"http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext_hex}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["ciphertext"]
    else:
        raise Exception(f"Request failed: {response.status_code}")

# Characters to test
charset = string.ascii_letters + string.digits + string.punctuation
print(string.punctuation)
flag = ""
for i in range(31, -1, -1):
    # Pad with '00' so that the unknown char is at the end of the first block
    prefix = "00" * i
    block_len = 64  # 16 bytes = 32 hex characters

    # Get reference ciphertext
    original_ciphertext = get_ciphertext(prefix)
    target_block = original_ciphertext[:block_len]  # first 16-byte block

    for ch in charset:
        test_input = prefix + ''.join([c.encode().hex() for c in flag + ch])
        test_cipher = get_ciphertext(test_input)

        if test_cipher[:block_len] == target_block:
            flag += ch
            print(f"[+] Found character: {ch} | Flag so far: {flag}")
            break

print(f"\nFinal flag: {flag}")
