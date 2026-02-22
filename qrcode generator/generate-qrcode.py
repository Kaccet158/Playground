import qrcode

url = input("URL: ").strip()
path = "/Users/kacpe/Desktop/qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(path)

print("Generated")



