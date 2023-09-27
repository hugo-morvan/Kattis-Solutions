n, m = map(int, input().split())
ciphertext = input().strip()
plaintext = input().strip()

# Extend the plaintext by adding n-1 asterisks at the beginning
plaintext = '*' * (n-1) + plaintext

# Iterate backwards over the ciphertext and plaintext, computing the keystream
keystream = ""
for i in range(m-1, n-2, -1):
    ciphertext_char = ord(ciphertext[i]) - 97  # Convert from character to integer 0-25
    plaintext_char = ord(plaintext[i]) - 97  # Convert from character to integer 0-25
    keystream_char = (ciphertext_char - plaintext_char) % 26  # Compute the keystream character
    keystream = chr(keystream_char + 97) + keystream  # Convert from integer to character and add to the front of the keystream

# Print the result
print(keystream)
