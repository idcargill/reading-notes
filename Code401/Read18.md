# Cryptography

[Khan Academy Encryption](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:data-encryption-techniques/a/encryption-decryption-and-code-cracking)

[Into to Cryptography](https://thebestvpn.com/cryptography/)

## Symmetric Encryption

Word Shifts:

- Caesar cipher
- Vigenere cipher

Limited complexity and susceptible to frequency analysis.

### Symmetric Cryptography

Keys are large random primary numbers.\
Keys are generated and public keys are exchanged.  Encryption is based on large prime number factoring and modular arithmetic.

- Data is sent in a one-way function encrypted with the public key.
- Data is deciphered with the private key.

### Advanced Encryption Standards

- [AES](https://thebestvpn.com/advanced-encryption-standard-aes/)
- Used by VPNs
- Keys for encoding access to hardware and data bases.

### Asymmetric Cryptography

- 2 different keys. One public, one private.

## Hashing

- SHA-256
- Used to verify a fixed size match.  Similar to checksum.
- Changes data into unreadable text.

## Key Exchange Algorithms

- [Diffie-Hellman wiki](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
- Very computationally expensive to crack.
- Public base and modulus
- Two parties exchange public keys and send each other secret numbers. The shared calculation will decrypt without ever sharing public keys.
