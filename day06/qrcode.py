import qrcode
name=input("Enter your name: ")
image = qrcode.make(name)
image.save("qrcode.png")
print("QR code generated and saved as qrcode.png")