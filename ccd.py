import tkinter as tk
from tkinter import messagebox

def decode_caesar_cipher(text, shift):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text

def display_all_shifts(text):
    shifts = []
    for shift in range(26):
        decoded_text = decode_caesar_cipher(text, shift)
        shifts.append(f"Shift {shift}: {decoded_text}")
    return shifts

def decode_with_key():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_key.get())
        if shift < 0 or shift > 25:
            raise ValueError
        decoded_text = decode_caesar_cipher(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decoded_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift key (0-25).")

def decode_without_key():
    text = input_text.get("1.0", tk.END).strip()
    shifts = display_all_shifts(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n".join(shifts))

# Create the UI
root = tk.Tk()
root.title("Caesar Cipher Decoder")

# Input Text
input_label = tk.Label(root, text="Enter text to decode:")
input_label.pack(pady=5)
input_text = tk.Text(root, height=5, width=40)
input_text.pack(pady=5)

# Shift Key
shift_label = tk.Label(root, text="Enter shift key (0-25):")
shift_label.pack(pady=5)
shift_key = tk.Entry(root)
shift_key.pack(pady=5)

# Buttons
decode_key_button = tk.Button(root, text="Decode with Key", command=decode_with_key)
decode_key_button.pack(pady=5)

decode_no_key_button = tk.Button(root, text="Decode without Key", command=decode_without_key)
decode_no_key_button.pack(pady=5)

# Output Text
output_label = tk.Label(root, text="Decoded text:")
output_label.pack(pady=5)
output_text = tk.Text(root, height=10, width=40)
output_text.pack(pady=5)

# Run the app
root.mainloop()
