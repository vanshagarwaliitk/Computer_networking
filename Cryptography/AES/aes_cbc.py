## Input: 1-D byte array for the plaintext
## Output: 1-D byte array for the padded plaintext
def pad(plaintext):
    pad_elm = 0x00
    if len(plaintext) % 16 == 0:
        pad_len = 0
    else:
        pad_len = 16 - len(plaintext) % 16
    padded_plaintext = plaintext + [pad_elm] * pad_len
    return padded_plaintext

## Input: 1-D byte array for the padded plaintext
## Output: 1-D byte array for the unpadded plaintext
def unpad(padded_plaintext):
    pad_elm = 0x00
    for i in range(len(padded_plaintext)-1, -1, -1):
        if padded_plaintext[i] != pad_elm:
            break
    unpadded_plaintext = padded_plaintext[:i+1]
    return unpadded_plaintext

## Input: 1-D byte array for the IV (Assume the IV is always 16 bytes)
## Input: 1-D byte array for the master key
## Input: 1-D byte array for the plaintext
## Output: 1-D byte array for the ciphertext
def AES128_CBC_encrypt(iv, master_key, plaintext):
    padded_plaintext = pad(plaintext)
    
    ### Your code starts ###
    ciphertext=[]
    block_size = 16
    prev_block_array = iv
    for i in range(0,len(padded_plaintext),block_size):
        plain_block_array = padded_plaintext[i:i + block_size]
        for i in range(len(plain_block_array)):
            plain_block_array[i] = plain_block_array[i]^prev_block_array[i]
        prev_block_array = AES128_encrypt(master_key,plain_block_array)
        for i in range(len(prev_block_array)):
            ciphertext.append(prev_block_array[i])

    ### Your code ends ###

    return ciphertext


## Input: 1-D byte array for the IV (Assume the IV is always 16 bytes)
## Input: 1-D byte array for the master key
## Input: 1-D byte array for the ciphertext
## Output: 1-D byte array for the plaintext
def AES128_CBC_decrypt(iv, master_key, ciphertext):
    
    ### Your code starts ###
    plaintext = []
    # ciphertext.reverse()
    block_size = 16
    prev_block_array = iv
    for i in range(0,len(ciphertext),block_size):
        cipher_array = ciphertext[i:i+block_size]
        plain_array = AES128_decrypt(master_key,cipher_array)
        for i in range(len(plain_array)):
            plain_array[i] = plain_array[i]^prev_block_array[i]
        for i in range(len(plain_array)):
            plaintext.append(plain_array[i])
        prev_block_array = cipher_array
        
    ### Your code ends ###

    unpadded_plaintext = unpad(plaintext)
    return unpadded_plaintext
