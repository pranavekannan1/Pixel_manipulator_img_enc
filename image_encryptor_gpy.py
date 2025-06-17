import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    return output_path

def decrypt_image(image_path, key, output_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    return output_path

def select_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if path:
        image_path.set(path)
        img = Image.open(path).resize((200, 200))
        img_preview = ImageTk.PhotoImage(img)
        preview_label.config(image=img_preview)
        preview_label.image = img_preview

def encrypt_action():
    try:
        key = int(key_entry.get())
        path = image_path.get()
        output = filedialog.asksaveasfilename(defaultextension=".png")
        if output:
            encrypt_image(path, key, output)
            messagebox.showinfo("Success", f"Image encrypted and saved to:\n{output}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_action():
    try:
        key = int(key_entry.get())
        path = image_path.get()
        output = filedialog.asksaveasfilename(defaultextension=".png")
        if output:
            decrypt_image(path, key, output)
            messagebox.showinfo("Success", f"Image decrypted and saved to:\n{output}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- GUI Setup ---
window = tk.Tk()
window.title("Image Encryptor/Decryptor")
window.geometry("400x450")
window.resizable(False, False)

image_path = tk.StringVar()

tk.Label(window, text="Select an image:").pack(pady=5)
tk.Button(window, text="Browse Image", command=select_image).pack()

preview_label = tk.Label(window)
preview_label.pack(pady=10)

tk.Label(window, text="Enter Secret Key:").pack()
key_entry = tk.Entry(window)
key_entry.pack(pady=5)

tk.Button(window, text="Encrypt Image", bg="#4CAF50", fg="white", command=encrypt_action).pack(pady=10)
tk.Button(window, text="Decrypt Image", bg="#2196F3", fg="white", command=decrypt_action).pack(pady=5)

window.mainloop()
