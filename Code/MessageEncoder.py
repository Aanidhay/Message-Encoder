from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("Decoder and Encoder")

# Define fullscreen as a global variable
fullscreen = False

# Initial font sizes
normal_font_size = 12
fullscreen_font_size = 20

# Custom Fonts
custom_font_title = ("Helvetica", fullscreen_font_size, "bold")
custom_font_label = ("Helvetica", normal_font_size)
custom_font_button = ("Helvetica", normal_font_size, "bold")

# Background Colors
bg_color = "lightgray"
button_bg_color = "lightblue"
button_fg_color = "white"

def center_window():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 500
    window_height = 300

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

Label(root, text="ENCODE DECODE", font=custom_font_title).pack()
Label(root, text="CAESAR CIPHER", font=custom_font_title, fg="blue").pack(side=BOTTOM)

Text = StringVar()
Result = StringVar()  # Rename EncodedText to Result

def Encode(message):
    encoded = ""
    for char in message:
        encoded += chr(ord(char) + 1)  # Caesar cipher with a shift of 1
    return encoded

def Decode(encoded_message):
    decoded = ""
    for char in encoded_message:
        decoded += chr(ord(char) - 1)  # Reverse the Caesar cipher
    return decoded

def Mode():
    input_text = Text.get()
    encoded_text = Encode(input_text)
    Result.set(encoded_text)  # Set the value of Result

def DecodeText():
    input_text = Text.get()
    decoded_text = Decode(input_text)  # Decode the input text directly
    Result.set(decoded_text)  # Set the value of Result

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    Result.set("")

# Fullscreen Function
def ToggleFullscreen():
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

    # Update font sizes based on fullscreen mode
    if fullscreen:
        custom_font_title = ("Helvetica", fullscreen_font_size, "bold")
        custom_font_label = ("Helvetica", fullscreen_font_size)
        custom_font_button = ("Helvetica", fullscreen_font_size, "bold")
    else:
        custom_font_title = ("Helvetica", normal_font_size, "bold")
        custom_font_label = ("Helvetica", normal_font_size)
        custom_font_button = ("Helvetica", normal_font_size, "bold")

    # Update fonts for labels and buttons
    for widget in root.winfo_children():
        if isinstance(widget, Label):
            widget.configure(font=custom_font_title)
        elif isinstance(widget, Button):
            widget.configure(font=custom_font_button)

    root.update_idletasks()  # Update the window size
    center_window()  # Recenter the widgets

# Message Label and Entry
Label(root, font=custom_font_label, text="MESSAGE").pack(pady=5)
entry_message = Entry(root, font=custom_font_label, textvariable=Text, bg="ghost white")
entry_message.pack(padx=10, pady=5)

# Result Text Display (formerly Encoded Text)
Label(root, font=custom_font_label, text="RESULT").pack(pady=5)
entry_result = Entry(root, font=custom_font_label, textvariable=Result, bg="ghost white")
entry_result.pack(padx=10, pady=5)

# Encode Button
Button(root, font=custom_font_button, text="ENCODE", command=Mode, bg="LightGrey", padx=5, pady=5).pack(pady=5)

# Decode Button
Button(root, font=custom_font_button, text="DECODE", command=DecodeText, bg="LightGrey", padx=5, pady=5).pack(pady=5)

# Reset and Exit Buttons
Button(root, font=custom_font_button, text="RESET", width=6, command=Reset, bg="LimeGreen", padx=5, pady=5).pack(pady=10)
Button(root, font=custom_font_button, text="EXIT", width=6, command=Exit, bg="OrangeRed", padx=5, pady=5).pack(pady=10)

# Full Screen Button (Bottom Right)
Button(root, text="Max/Min Screen", width=12, command=ToggleFullscreen, bg="lightgray", font=custom_font_button).pack(side=BOTTOM, anchor=SE, padx=10, pady=10)

# Center align all widgets horizontally
center_window()

root.mainloop()




