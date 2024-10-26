from cryptography.fernet import Fernet

def load_key():
  file=open("Password Manager/key.key", "rb")
  key=file.read()
  file.close()
  return key

key=load_key()
fer=Fernet(key)


# def write_key():
#   key=Fernet.generate_key()
#   with open("Password Manager/key.key", "wb") as key_file:
#     key_file.write(key)

# write_key()

def view():
  with open('Password Manager/passwords.txt') as f:
    for line in f.readlines():
      data=line.rstrip()
      user, passw=data.split("|")
      print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
  name=input('Account Name: ')
  pwd=input("Password: ")
  with open('Password Manager/passwords.txt','a') as f:
    f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")


while True:
   mode = input(
       "Would you like to add a new password or view existing ones(view, add)?, please press q to exit:").lower()
   if mode == "q":
    break

   elif mode == "view":
      view()

   elif mode == "add":
      add()

   else:
      print("Invalid mode.")


