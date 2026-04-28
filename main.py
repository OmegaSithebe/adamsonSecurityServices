import qrcode

url = "https://www.adamsonsecurityservices.co.za/"
file_path = "C:/Users/User/Documents/Projects/Nkosi Mbewe/adamsonSecurityServices/qr_code.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)