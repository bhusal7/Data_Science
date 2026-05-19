import qrCode
data = "Pradeep Bhusal"
qr = qrcode.make(data)
qr.save("qrcode.png")
print("Successfully generated Qr Code")

=