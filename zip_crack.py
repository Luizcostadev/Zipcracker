import zipfile
import itertools
import string

def try_password(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except:
        return False

def crack_zip(zip_file_path, dictionary_path):
    with open(dictionary_path, 'r') as dictionary_file:
        passwords = dictionary_file.readlines()

    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        for password in passwords:
            password = password.strip()
            if try_password(zip_file, password):
                print(f"Password found: {password}")
                return
        print("Password not found in the dictionary.")

# Example usage
zip_file_path = 'path/to/your/encrypted.zip'
dictionary_path = 'path/to/your/dictionary.txt'
crack_zip(zip_file_path, dictionary_path)