import numpy as np

key = "DDCF"
plain_text = "HELP"

# changes the key string (4 chars) into a matrix
def key_to_matrix(key):
  key = [*key.lower()]
  new_key = []
  for i in range(len(key)):
    index = ord(key[i]) - 97
    new_key.append(index)
  key_matrix = [[new_key[0], new_key[1]],[new_key[2], new_key[3]]]
  return key_matrix

def plain_text_to_matrix(plain_text):
  plain_text = [*plain_text.lower()]
  colums = len(plain_text)/2
  if colums % 2 == 0:
    pass
  else:
    plain_text.append("z")
    colums+=1

  new_text = []
  for i in range(len(plain_text)):
    index = ord(plain_text[i]) - 97
    new_text.append(index)
  
  plain_text_matrix = np.zeros( (2, int(colums)) )
  n = 0
  for r in range(2):
    for c in range(int(colums)):
        plain_text_matrix[r][c] = new_text[n]
        n+=1
  print(plain_text_matrix.tolist())
  return plain_text_matrix.tolist()
  
def plain_text_to_cipher_text(plain_text, key):
  pass

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
  return inverse_matrix

plain_text_matrix = plain_text_to_matrix(plain_text)
key_matrix = key_to_matrix(key)
plain_text_to_cipher_text(plain_text_matrix, key_matrix)