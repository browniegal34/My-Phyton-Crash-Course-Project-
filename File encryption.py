def shift_text(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result

def process_file(filename, key, mode):
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found")
        return

    if mode == "decrypt":
        key = -key

    new_text = shift_text(content, key)
    new_name = mode + "ed_" + filename

    with open(new_name, "w") as f:
        f.write(new_text)
    print("Saved as", new_name)

print("File Encryption Tool")
mode = input("encrypt or decrypt? ").lower()
filename = input("File name: ")

try:
    key = int(input("Key (number): "))
except ValueError:
    print("Key must be a number")
    exit()

if mode in ("encrypt", "decrypt"):
    process_file(filename, key, mode)
else:
    print("Invalid option")