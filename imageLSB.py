from PIL import Image
import sys

def hide_message(image_path, message, output_path="cover_new.png"):
    
   
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'

   
    img = Image.open(image_path)
    if img.mode != "RGB": 
        img = img.convert("RGB")
    pixels = img.load()

   
    binary_index = 0
    for y in range(img.height):
        for x in range(img.width):
            if binary_index < len(binary_message):
                r, g, b = pixels[x, y]
                new_r = (r & ~1) | int(binary_message[binary_index])  
                pixels[x, y] = (new_r, g, b)
                binary_index += 1
            else:
                break
        if binary_index >= len(binary_message):
            break

   
    img.save(output_path)
    print(f"Message successfully hidden in '{output_path}'")

if __name__ == "__main__":
    


    if len(sys.argv) != 4:
        print("Usage: python imageLSB.py hide <image_path> <message>")
    else:
        hide_message(sys.argv[2], sys.argv[3])

def retrieve_message(image_path):
    """Retrieves a hidden message from an image using LSB steganography."""
   
    img = Image.open(image_path)
    pixels = img.load()

    binary_message = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]  
            binary_message += str(r & 1) 
            if binary_message[-16:] == '1111111111111110':  
                binary_message = binary_message[:-16]  
               
                message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
                print("Retrieved message:", message)
                return

    print("No hidden message found.")

if __name__ == "__main__":
   
    
    if len(sys.argv) != 3:
        print("Usage: python imageLSB.py retrieve <image_path>")
    else:
        retrieve_message(sys.argv[2])
