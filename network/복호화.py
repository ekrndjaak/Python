# 복호화 코드
def caesar_decipher(encrypted_text, shift):
    result = []
    for char in encrypted_text:
        if char.isalpha():
            shift_amount = (ord('A') if char.isupper() else ord('a'))  
            decrypted_char = chr(((ord(char) - shift_amount - shift) % 26) + shift_amount)
            result.append(decrypted_char)
        else:
            result.append(char)
    return ''.join(result)

def main(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as f:
            encrypted_text = f.read()
        decrypted_text = caesar_decipher(encrypted_text, shift)
        with open(output_file, 'w') as f:
            f.write(decrypted_text)
        print(f'복호화 완료. 복호문은 {output_file}에 저장되었습니다.')
    except FileNotFoundError:
        print(f'파일을 찾을 수 없습니다: {input_file}')

if __name__ == '__main__':
    input_file = 'encrypted_alphabet.txt'  # 암호화된 알파벳 텍스트 파일
    output_file = 'decrypted_alphabet.txt'  # 복호문을 저장할 파일
    shift = 3  # 암호화에 사용한 시프트 값

    main(input_file, output_file, shift)
