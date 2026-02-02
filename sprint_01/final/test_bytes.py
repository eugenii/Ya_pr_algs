field = [bytearray(input(), "utf-8") for _ in range(4)]
print(*field, sep='\n')
for line in field:
    for byte in line:
        if byte == 46:
            print(chr(byte), end=' ')
            continue
        print(chr(byte), end=' ')    
    print()