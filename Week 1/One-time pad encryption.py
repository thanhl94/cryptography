import binascii

# Note:
# otpK and otpE can be combined or used as the same function as OTP
# encryption can be communtative with each other. For representation
# purposes, these will be separated as function to get key and cipher

# This function take in a plaintext and a cipher text and get the key
def optK(data, cipher):
  key = data ^ cipher
  return key
# This function encrypt plaintext by xor plaintext with the key
def otpE(data, key):
  cipher = data ^ key
  return cipher

# Convert our string plaintext into usable hex
def string2hex(data):
  temp = binascii.hexlify(data.encode('utf-8'))
  string2hex = str(temp,'ascii')
  hex_int = int(string2hex, 16)
  new_int = hex_int + 0x0
  return new_int

def otp():

  # Given plaintext message A and it encrypted form from 
  # One-time pad encryption
  # Test case:
  # plainA = "attack at dawn"
  # cipherA = 09e1c5f70a65ac519458e7e53f36
  plainA = input("Enter your plaintext: ")
  rawinput = "0x" + input("Enter your ciphertext: ")
  cipherA = int(rawinput, 16)

  # Given plaintext B, we need to get its encrypted form
  # Test case:
  # plainB = "attack at dusk"
  plainB = input("Enter your plaintext to encrypt: ")

  # 1st We need to finds OTP key by xor plain text msg with cipher text
  # Before that, we need to convert plaintext A into hex format
  hexA = string2hex(plainA)

  # Then we can get the key by decrypting the two 
  key = optK(hexA, cipherA)

  # Given key, we can now use it to encrypt our plain text message
  # Again, we have to convert our string to hex
  hexB = string2hex(plainB)
  cipherB = otpE(hexB, key)

  # Output of plain text, OTP key, and cipher text
  
  print('Plain Text: "' + plainB + '"')
  # Plain Text: "attack at dusk"
  print('Encryption Key: ' + hex(key))
  # Encryption Key: 0x6895b196690e8c30e07883844858
  print('Cipher Text: ' + hex(cipherB))
  # Cipher Text: 0x9e1c5f70a65ac519458e7f13b33

if __name__ == '__main__':
    otp()
