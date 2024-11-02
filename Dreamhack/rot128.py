# 역순환을 위한 hex_list 정의
hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

# encfile 읽기
with open('encfile', 'r', encoding='utf-8') as f:
    enc_data = f.read()

# encfile을 2자리씩 쪼개어 복호화
dec_list = []
for i in range(0, len(enc_data), 2):
    enc_hex = enc_data[i:i+2]
    index = hex_list.index(enc_hex)
    dec_index = (index - 128) % len(hex_list)  # 128 위치 왼쪽으로 시프트
    dec_list.append(int(hex_list[dec_index], 16))

# 복호화된 데이터 바이너리 파일로 저장
with open('flag_dec.png', 'wb') as f:
    f.write(bytearray(dec_list))

print("복호화된 파일이 'flag_dec.png'로 저장되었습니다.")
