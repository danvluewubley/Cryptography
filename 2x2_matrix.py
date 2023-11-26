import numpy as np

key = "DDCF"
plain_text = "HELPS"

# changes the key string (4 chars) into a matrix
def key_to_matrix(key):
  key = [*key.lower()]
  new_key = []
  for i in range(len(key)):
    index = ord(key[i]) - 97
    new_key.append(index)
  key_matrix = [[new_key[0], new_key[1]],[new_key[2], new_key[3]]]
  print("Matrix for the key:")
  print(key_matrix)
  return key_matrix

def plain_text_to_matrix(plain_text):
  plain_text = [*plain_text.lower()]
  colums = len(plain_text)/2
  if colums % 2 == 0:
    pass
  else:
    plain_text.append("z")
    colums+=0.5

  new_text = []
  for i in range(len(plain_text)):
    index = ord(plain_text[i]) - 97
    new_text.append(index)
  
  plain_text_matrix = np.zeros( (2, int(colums)) )
  n = 0
  for c in range(int(colums)):
    for r in range(2):
        plain_text_matrix[r][c] = new_text[n]
        print(plain_text_matrix)
        n+=1
  print("Matrix for the plain text:")
  print(plain_text_matrix.tolist())
  return plain_text_matrix.tolist()
  
def plain_text_to_cipher_text(plain_text, key):
  cipher_text_array = []
  for n in range(len(plain_text[0])):
    for r in range(2):
      result = (key[r][0] * plain_text[0][n] + key[r][1] * plain_text[1][n]) % 26 + 97
      cipher_text_array.append(chr(int(result)).upper())
  cipher_text = ""
  print("Cipher Text: " + cipher_text.join(cipher_text_array))
  return cipher_text_array

# utilizes the modular multiplicative inverse properity to identify the congruent determinant
def inverse_modular(modular, a):
  n = 0
  for n in range(20):
    value = a*n
    if value % 26 == 1:
      return n

# inverts the matrix
def matrix_inverter(matrix):
  determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
  determinant = inverse_modular(26, determinant)
  
  adjoint = [[matrix[1][1], -matrix[0][1]],[-matrix[1][0],matrix[0][0]]]
  inverse_matrix = [[(adjoint[0][0]*determinant)%26,(adjoint[0][1]*determinant)%26],[(adjoint[1][0]*determinant)%26,(adjoint[1][1]*determinant)%26]]
  print(inverse_matrix)
  return inverse_matrix

def cipher_text_to_plain_text(cipher_text, key):
  plain_text_array = []
  cipher_text_array = []
  if len(cipher_text) % 2 == 0:
    colums = len(cipher_text)/2
  else:
    colums = len(cipher_text)/2+0.5
  for n in range(len(cipher_text)):
    index = ord(cipher_text[n])-65
    cipher_text_array.append(index)

  print(cipher_text_array)
  
  cipher_text_matrix = np.zeros( (2, int(colums)) )
  n = 0
  for c in range(int(colums)):
    for r in range(2):
        cipher_text_matrix[r][c] = cipher_text_array[n]
        print(cipher_text_matrix)
        n+=1
  print("Matrix for the plain text:")
  print(cipher_text_matrix)

  inverse_key_matrix = matrix_inverter(key)
  for n in range(int(colums)):
    for r in range(2):
      result = (inverse_key_matrix[r][0] * cipher_text_matrix[0][n] + inverse_key_matrix[r][1] * cipher_text_matrix[1][n]) % 26 + 97
      plain_text_array.append(chr(int(result)).upper())
      print(result)
  plain_text = ""
  print("Cipher Text: " + plain_text.join(plain_text_array))
  return plain_text_array



plain_text_matrix = plain_text_to_matrix(plain_text)
key_matrix = key_to_matrix(key)
cipher_text_matrix = plain_text_to_cipher_text(plain_text_matrix, key_matrix)
cipher_text_to_plain_text(cipher_text_matrix, key_matrix)
