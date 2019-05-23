import tkinter as tk

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)

    # api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml
    # a7f87b5f44e411210dc6324575d1a4db

def get_weather(city):
    weather_key = 'a7f87b5f44e411210dc6324575d1a4db'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': city, 'units': 'Imperial'}
    response = requests.get(url, params = params)
    print(response.json())

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = 'image.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = '#60c1aa', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = '40')
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", bg = '#80c1df', font = 40, command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

lower_frame = tk.Frame(root, bg = '#60c1aa', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame)
label.place(relwidth = 1, relheight = 1)

root.mainloop()

  