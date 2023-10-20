import random

def generate_password(length=12):
  """Generates a random password of the given length.

  Args:
    length: The length of the password.

  Returns:
    A random password of the given length.
  """

  characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
  password = ""
  for i in range(length):
    password += random.choice(characters)
  return password

if __name__ == "__main__":
  print(generate_password())
