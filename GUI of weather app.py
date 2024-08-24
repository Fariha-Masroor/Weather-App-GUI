import tkinter    
# importing a library
from tkinter import PhotoImage
from tkinter import ttk
import json
import requests
def func_get_weather():
   
 
   city=select_city_dropdowm.get()
  

   api_key="bb987833b27071d257d465788621a456"
   api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
   server_data=requests.get(api_url)
   server_data_json=server_data.json()

   temp=server_data_json["main"]["temp"]
   pressure=server_data_json["main"]["pressure"]
   humidity=server_data_json["main"]["humidity"]
   
   output_label.config(text=f'temperature:{temp}°C,'
                            f'pressure:{pressure},'
                            f'humidity:{humidity}%'
 )
  
   output_label.pack(pady=10)








root=tkinter.Tk()
# creating a window
root.geometry("500x600")
# giving some dimensions to window
root.title("Weather App")
# giving the title to the window screen

image_path=r"C:\Users\Malik ITS\Desktop\soap-bubbles-foam-background-3.png"
bg_image=PhotoImage(file=image_path)
set_bg_image=tkinter.Label(root,image=bg_image)
set_bg_image.place(relheight=1,relwidth=1)

app_header=tkinter.Label(root,text="Weather App",font=("poppins",30),bg="white",fg="blue")
app_header.pack(pady=20)

select_city_label=tkinter.Label(root,text="select city",font=("poppins",24))
select_city_label.pack(pady=20)


cities=["Karachi","Lahore","Islamabad","Muzaffarabad","Abbotaabd"]
select_city_dropdowm=ttk.Combobox(root,values=cities,font=("poppins",16))
select_city_dropdowm.pack(pady=20)

get_weather_button=tkinter.Button(root,text="Get Weather",font=("poppins",16),command=func_get_weather)
get_weather_button.pack(pady=10)

output_label=tkinter.Label(root,text="",font=("poppins",16))

root.mainloop()
# keeping the window open and in loop

