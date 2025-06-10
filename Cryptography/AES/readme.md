# AES-128 CBC Implementation

A pure Python implementation of the Advanced Encryption Standard (AES) with 128-bit keys in Cipher Block Chaining (CBC) mode.

## Features

- Complete AES-128 implementation from scratch
- CBC mode operation with proper chaining
- PKCS#7 padding for variable-length messages
- Includes all AES transformations:
  - SubBytes/InvSubBytes
  - ShiftRows/InvShiftRows
  - MixColumns/InvMixColumns
  - AddRoundKey
- Key expansion with Rijndael's key schedule
- Both encryption and decryption support

## Implementation Details

### Core Components

1. **Substitution Boxes**:
   - Precomputed S-box and inverse S-box for byte substitution
   - Used in SubBytes and key expansion

2. **Key Expansion**:
   - 128-bit key expanded into 11 round keys (10 rounds + initial key)
   - Implements Rijndael key schedule with:
     - RotWord
     - SubWord
     - Rcon (round constant) application

3. **AES Rounds**:
   - 10 rounds of transformation for 128-bit keys
   - Final round omits MixColumns

4. **CBC Mode**:
   - Uses Initialization Vector (IV) for first block XOR
   - Chains ciphertext blocks for subsequent operations
   - Automatic padding with PKCS#7

### File Structure

- `SBOX`/`INV_SBOX`: Precomputed substitution boxes
- `RCON`: Round constants for key expansion
- Core functions:
  - `to_matrix()`/`to_array()`: Data format conversion
  - `AddRoundKey()`: XOR with round key
  - `SubBytes()`/`SubBytes_inv()`: Byte substitution
  - `ShiftRows()`/`ShiftRows_inv()`: Row shifting
  - `MixColumns()`/`MixColumns_inv()`: Column mixing
  - `compute_next_rk()`: Key schedule round function
  - `AES128_key_expansion()`: Full key expansion

## Usage

### Encryption

```python
def AES128_CBC_encrypt(iv, master_key, plaintext):
    # Implements CBC encryption
    # Returns ciphertext as byte array