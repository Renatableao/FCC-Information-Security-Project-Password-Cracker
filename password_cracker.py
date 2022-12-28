import hashlib

def crack_sha1_hash(hash, use_salts = False):

  file1 = open('top-10000-passwords.txt', 'r')

  password_hash = {}

  for line in file1:
    line = line.replace("\n", "")
    if use_salts:
      file2 = open('known-salts.txt', 'r')
      for salt in file2:
        salt = salt.replace("\n", "")
        salt_prep = salt + line
        line_hash_prep = hashlib.sha1(salt_prep.encode()).hexdigest()
        password_hash[line_hash_prep] = line
        salt_app = line + salt
        line_hash_app = hashlib.sha1(salt_app.encode()).hexdigest()
        password_hash[line_hash_app] = line
    else:
      line_hash = hashlib.sha1(line.encode()).hexdigest()
      password_hash[line_hash] = line
      

  if hash in password_hash:
    return password_hash[hash]
  return "PASSWORD NOT IN DATABASE"
    
    
      