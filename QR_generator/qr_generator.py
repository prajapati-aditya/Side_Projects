# pip install qrcode pillow
import qrcode

# ask the user for the link of which qr is to be generated

link = input("Enter your link : www.youtube.com") 
link = link.lower()

#taking colour input for block and back
block = input("enter colour for the blocks of the qr : ")
block = block.lower()

back = input("Enter colour for the back of the qr : ")
back = back.lower()

# input for file name
file_name=input("Enter name for image file : ")
file_name=file_name.lower()

# creating the instance of the qrcode object
qr = qrcode.QRCode(version=1, box_size=5, border=5)

# passing this link into the object and making the qr
qr.add_data(link)
qr.make()

#saving and generating the qr 
img = qr.make_image(fill_color=block, back_color=back)
img.save(file_name)
img.show()