def caesarCipher(s, k):
    result = []
    k = k % 26 
    
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            
            # เลื่อนตัวอักษรและจัดการการวนลูปกลับไปที่ a-z ใหม่
            shifted = chr((ord(char) - base + k) % 26 + base)
            result.append(shifted)
        else:
            result.append(char)
            
    return "".join(result)