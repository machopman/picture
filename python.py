import tkinter
from PIL import Image, ImageTk
from io import BytesIO
import requests

window = tkinter.Tk()

url = "http://www.majorcineplex.com/uploads/movie/1792/thumb_1792.jpg"
r = requests.get(url)

pilImage = Image.open(BytesIO(r.content))
pilImage.mode = 'RGBA'
pilImage = pilImage.resize((50, 50), Image.ANTIALIAS)


image = ImageTk.PhotoImage(pilImage)

label = tkinter.Label(image=image)
label.pack()

window.mainloop()