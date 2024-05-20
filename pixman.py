from PIL import Image

def encrypt_image(image_path, encryption_key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Encrypt the image by applying a basic mathematical operation to each pixel
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # Example encryption: multiply each RGB value by the encryption key
            encrypted_pixel = tuple((p * encryption_key) % 256 for p in pixel)
            encrypted_pixels.append(encrypted_pixel)
    
    # Create a new image with the encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(image_path, decryption_key):
    # Open the encrypted image
    encrypted_img = Image.open(image_path)
    width, height = encrypted_img.size
    
    # Decrypt the image by applying the inverse operation to each pixel
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = encrypted_img.getpixel((x, y))
            # Example decryption: divide each RGB value by the decryption key
            decrypted_pixel = tuple((p // decryption_key) % 256 for p in pixel)
            decrypted_pixels.append(decrypted_pixel)
    
    # Create a new image with the decrypted pixels
    decrypted_img = Image.new(encrypted_img.mode, encrypted_img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        
        image_path = input("Enter the path to the image file: ")
        if choice == 'e':
            encryption_key = int(input("Enter the encryption key (an integer): "))
            encrypt_image(image_path, encryption_key)
        else:
            decryption_key = int(input("Enter the decryption key (an integer): "))
            decrypt_image(image_path, decryption_key)
        
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
