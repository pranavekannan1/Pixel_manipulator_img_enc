# Image Encryption & Decryption Tool
A beginner-friendly desktop app built with Python, Tkinter, and Pillow that lets you encrypt and decrypt images using simple pixel-based logic.

# Features
1.Choose any image (PNG, JPG)
2.Enter a secret key for encryption/decryption
3.Encrypts pixel values by modifying RGB components
4.Decrypts back using the same key
5.Save the encrypted or decrypted image to your device
6.Clean and simple user interface

# Requirements
-Python 3.x
-Pillow
-Tkinter (usually included with Python)

# How to Run
1.Clone or download this repo.
2.Run the script:
            1.Select an image
            2.Enter a numeric key
            3.Click Encrypt or Decrypt.
            4.Choose where to save the result

# How It Works
-Each image pixel is made of RGB values (Red, Green, Blue). This tool uses a numeric key to modify those values:
-Encryption: (R, G, B) + key % 256
-Decryption: (R, G, B) - key % 256

It’s a simple reversible transformation, just like a Caesar cipher for images!

# Example Use Case
Hide a confidential image before sharing it online.
Basic tool to teach cryptography and image encoding in classrooms.
Beginner Python GUI project for learning and showcasing.

# License
This project is open source and free to use under the MIT License.
This project is a Python-based desktop application that allows users to secure images by encrypting and decrypting them using simple pixel manipulation techniques. The program features an interactive graphical user interface (GUI) built using Tkinter, making it user-friendly and accessible to users with no coding experience.
