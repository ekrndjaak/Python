# 빈도수 체크하여 키 파일에 입력
def calculate_frequency(text):
    frequency_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1

    # 빈도수로 내림차순 정렬
    sorted_frequency = dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))

    # 알파벳 순서로 키를 매핑
    encryption_key = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char, _ in sorted_frequency.items():
        if not alphabet:
            break
        encryption_key[char] = alphabet[0]
        alphabet = alphabet[1:]

    return encryption_key

# 암호화
def encrypt(text, encryption_key):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in encryption_key:
                if char.isupper():
                    encrypted_text += encryption_key[char].upper()
                else:
                    encrypted_text += encryption_key[char]
            else:
                encrypted_text += char
        else:
            encrypted_text += char
    return encrypted_text

# 복호화
def decrypt(text, decryption_key):
    decryption_key = {v: k for k, v in decryption_key.items()}
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            if char in decryption_key:
                if char.isupper():
                    decrypted_text += decryption_key[char].upper()
                else:
                    decrypted_text += decryption_key[char]
            else:
                decrypted_text += char
        else:
            decrypted_text += char
    return decrypted_text

# 암호화 키 생성
with open('alphabet.txt', 'r') as f:
    text = f.read()
    encryption_key = calculate_frequency(text)

# 암호화
encrypted_text = encrypt(text, encryption_key)

# 암호문 저장
with open('encrypted_text.txt', 'w') as f:
    f.write(encrypted_text)

print("암호화 완료. 암호문은 encrypted_text.txt에 저장되었습니다.")

# 복호화 키 생성
decryption_key = {v: k for k, v in encryption_key.items()}

# 복호화
decrypted_text = decrypt(encrypted_text, decryption_key)

# 원문 저장
with open('decrypted_text.txt', 'w') as f:
    f.write(decrypted_text)

print("복호화 완료. 원문은 decrypted_text.txt에 저장되었습니다.")
