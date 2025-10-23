import qrcode
import base64
import os

def generate_qr(data, filename="qr_code.png"):
    """
    Generates a QR code from the given data and saves it as a PNG file.
    
    :param data: The data to encode (string).
    :param filename: Output filename (default: qr_code.png).
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

def main():
    print("Simple QR Code Generator")
    print("Choose data type:")
    print("1. Link/URL")
    print("2. Text")
    print("3. Contact (vCard)")
    print("4. WiFi Access")
    print("5. Image (as base64-encoded URL or data)")
    
    choice = input("Enter choice (1-5): ").strip()
    
    if choice == "1":
        url = input("Enter URL: ").strip()
        generate_qr(url, "qr_link.png")
    elif choice == "2":
        text = input("Enter text: ").strip()
        generate_qr(text, "qr_text.png")
    elif choice == "3":
        # vCard format for contact
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"
        generate_qr(vcard, "qr_contact.png")
    elif choice == "4":
        # WiFi format: WIFI:S:<SSID>;T:<WPA|WEP|>;P:<password>;;
        ssid = input("Enter WiFi SSID: ").strip()
        security = input("Enter security type (WPA, WEP, or none): ").strip().upper()
        password = input("Enter password (leave blank if none): ").strip()
        wifi_data = f"WIFI:S:{ssid};T:{security};P:{password};;"
        generate_qr(wifi_data, "qr_wifi.png")
    elif choice == "5":
        image_path = input("Enter image file path: ").strip()
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                encoded = base64.b64encode(img_file.read()).decode('utf-8')
                data = f"data:image/png;base64,{encoded}"  # Assumes PNG; adjust for other formats
                generate_qr(data, "qr_image.png")
        else:
            print("Image file not found.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()