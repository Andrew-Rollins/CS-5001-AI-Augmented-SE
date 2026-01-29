import string

class DecryptionUtils:
    def __init__(self, key: str):
        self.key_ = key

    def caesar_decipher(self, ciphertext: str, shift: int) -> str:
        shift %= 26
        plaintext = []
        for c in ciphertext:
            if c.isalpha():
                base = 'A' if c.isupper() else 'a'
                shifted = (ord(c) - ord(base) - shift + 26) % 26 + ord(base)
                plaintext.append(chr(shifted))
            else:
                plaintext.append(c)
        return ''.join(plaintext)

    def vigenere_decipher(self, ciphertext: str) -> str:
        decrypted = []
        key_len = len(self.key_)
        key_idx = 0

        for c in ciphertext:
            if c.isalpha():
                shift = ord(self.key_[key_idx % key_len].lower()) - ord('a')
                base = 'a' if c.islower() else 'A'
                # work in lowercase then restore case
                dec_char = (ord(c.lower()) - ord('a') - shift + 26) % 26 + ord('a')
                dec_char = chr(dec_char)
                decrypted.append(dec_char.upper() if c.isupper() else dec_char)
                key_idx += 1
            else:
                decrypted.append(c)
        return ''.join(decrypted)

    def rail_fence_decipher(self, encrypted_text: str, rails: int) -> str:
        if rails <= 1:
            return encrypted_text

        n = len(encrypted_text)
        # initialize fence with placeholder characters
        fence = [['\n' for _ in range(n)] for _ in range(rails)]

        direction = -1
        row = 0
        col = 0
        # mark the positions that will hold characters
        for i in range(n):
            if row == 0 or row == rails - 1:
                direction = -direction
            fence[row][col] = '*'
            col += 1
            row += direction

        # fill the marked positions with the encrypted text
        idx = 0
        for r in range(rails):
            for c in range(n):
                if fence[r][c] == '*':
                    fence[r][c] = encrypted_text[idx]
                    idx += 1

        # read the fence in zig‑zag order to reconstruct plain text
        direction = -1
        row = 0
        col = 0
        plain_text = []
        for i in range(n):
            if row == 0 or row == rails - 1:
                direction = -direction
            plain_text.append(fence[row][col])
            col += 1
            row += direction

        return ''.join(plain_text)
