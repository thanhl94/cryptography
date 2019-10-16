import binascii

def optK(data, cipher):
  key = data ^ cipher
  return key

def otpE(data, key):
  cipher = data ^ key
  return cipher

def string2hex(data):
  temp = binascii.hexlify(data.encode('utf-8'))
  string2hex = str(temp,'ascii')
  hex_int = int(string2hex, 16)
  new_int = hex_int + 0x0
  return new_int

def otp():

  # Given plain text message A and it encrypted form from 
  # One-time pad encryption
  plainA = "attack at dawn"
  cipherA = 0x09e1c5f70a65ac519458e7e53f36

  # Given plain text B, we need to get its encrypted form
  plainB = "attack at dusk"

  # 1st We need to finds OTP key by xor plain text msg with cipher text
  # Before that, we need to convert plain text A into hex format
  hexA = string2hex(plainA)

  # Then we can get the key by decrypting the two 
  key = optK(hexA, cipherA)

  # Given key, we can now use it to encrypt our plain text message
  # Again, we have to convert our string to hex
  hexB = string2hex(plainB)
  cipherB = otpE(hexB, key)

  # Output of plain text, OTP key, and cipher text
  print('Plain Text: "' + plainB + '"')
  print('Encryption Key: ' + hex(key))
  print('Cipher Text: ' + hex(cipherB))

if __name__ == '__main__':
    otp()
