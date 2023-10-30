import segno

qrccode = segno.make_qr("Hello, World")

qrcode.save("basic_qrcode.png")
