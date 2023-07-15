import tkinter as tk
from tkinter import filedialog
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def save_key_to_file(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)

def load_key_from_file(filename):
    with open(filename, 'rb') as file:
        key = file.read()
    return key

def encrypt_file(file_path, public_key_path, output_path):
    # Halka açık anahtar yükleyin
    public_key = RSA.import_key(load_key_from_file(public_key_path))
    cipher = PKCS1_OAEP.new(public_key)

    chunk_size = 245  # Her bir parça boyutu
    encrypted_chunks = []

    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            encrypted_chunk = cipher.encrypt(chunk)
            encrypted_chunks.append(encrypted_chunk)

    # Şifreli verileri birleştirerek tam şifreli dosyayı oluştur
    encrypted_data = b"".join(encrypted_chunks)

    # Şifreli veriyi kaydet
    with open(output_path, 'wb') as output_file:
        output_file.write(encrypted_data)

def select_file():
    # Anahtar çiftini oluştur
    private_key, public_key = generate_key_pair()

    # Anahtarları dosyalara kaydet
    save_key_to_file(private_key, 'private_key.pem')
    save_key_to_file(public_key, 'public_key.pem')

    file_path = filedialog.askopenfilename(initialdir="/", title="Dosya Seç")
    if file_path:
        private_key_path = 'private_key.pem'
        public_key_path = 'public_key.pem'
        encrypted_file_path = 'encrypted_file.txt'

        # Dosyayı şifrele
        encrypt_file(file_path, public_key_path, encrypted_file_path)
        print("Dosya başarıyla şifrelendi.")

root = tk.Tk()
button = tk.Button(root, text="Dosya Seç", command=select_file)
button.pack()

root.mainloop()
