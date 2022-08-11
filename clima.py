from tkinter import  Tk, Button, Entry, Label,PhotoImage,Frame
from PIL import Image  #pip install Pillow
import requests        #pip install requests
import time

class Ventana(Frame):
    def __init__(self, master, *args):
        super().__init__( master,*args)
        self.click = True
        
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.frame = Frame(self.master, bg='Turquoise1', highlightbackground='black',highlightthickness=2)
        self.frame.grid(columnspan=3, row = 0, sticky='nsew', padx=5, pady=5)
        self.frame2 = Frame(self.master, bg='yellow', highlightbackground='black',highlightthickness=2)
        self.frame2.grid(column=0, row = 1, sticky='nsew', padx=5, pady=5)
        self.frame3 = Frame(self.master, bg='red', highlightbackground='black',highlightthickness=2) #pink
        self.frame3.grid(column=1, row = 1, sticky='nsew', padx=5, pady=5)
        self.frame4 = Frame(self.master, bg='deep sky blue', highlightbackground='black',highlightthickness=2)
        self.frame4.grid(column=2, row = 1, sticky='nsew', padx=5, pady=5)
        self.frame5 = Frame(self.master, bg='cyan2', highlightbackground='black',highlightthickness=2) #light coral
        self.frame5.grid(column=0, row = 2, sticky='nsew', padx=5, pady=5)
        self.frame6 = Frame(self.master, bg='aquamarine', highlightbackground='black',highlightthickness=2)
        self.frame6.grid(column=1, row = 2, sticky='nsew', padx=5, pady=5)
        self.frame7 = Frame(self.master, bg='sky blue', highlightbackground='black',highlightthickness=2) #HotPink1
        self.frame7.grid(column=2, row =2 , sticky='nsew', padx=5, pady=5)

        self.widgets()

    def animacion(self): 
        self.frame.config(highlightbackground='black')
        self.frame2.config(highlightbackground='black')
        self.frame3.config(highlightbackground='black')
        self.frame4.config(highlightbackground='black')
        self.frame5.config(highlightbackground='black')
        self.frame6.config(highlightbackground='black')
        self.frame7.config(highlightbackground='black')
        self.obtener_tiempo()
        gif = Image.open('buscar.gif')
        frames = gif.n_frames
        if self.click == True:			
            for i in range(1, frames):				
                self.inicio = PhotoImage(file ='buscar.gif', format='gif -index %i' %(i))
                self.bt_inicio['image'] = self.inicio
                time.sleep(0.04)					
                self.master.update()
                self.click= False
                if i + 1 == frames:
                    self.click = True					
    def obtener_tiempo(self):
        ciudad = self.ingresa_ciudad.get()
        #key :  'f08c20ee319398d4ccb55d6a775da82211'
        #API = 'api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'

        #Actualizar  la API key con la de su cuenta: 
        API = 'https://api.openweathermap.org/data/2.5/weather?q=' +ciudad+ '&appid=c77a716698803a136824b8218c369805'  
        try:
            json_datos = requests.get(API).json()
            self.temp['text'] = str(int(json_datos['main']['temp'] - 273.15)) + " °C"
            self.temp_min['text'] = str(int(json_datos['main']['temp_min'] - 273.15))  +" °C"
            self.temp_max['text'] = str(int(json_datos['main']['temp_max'] - 273.15)) +" °C"
            self.presion['text'] = str(json_datos['main']['pressure']) + ' hPa'
            self.humedad['text'] = str(json_datos['main']['humidity']) + ' %'	    
            self.viento['text'] = str(int(json_datos['wind']['speed'])*18/5) + ' km/h'
            self.localidad['text'] =  json_datos['name'] + ' - '+ json_datos['sys']['country'] 
            print(json_datos)
        except:
            self.aviso['text'] =  'No pa usted esta re loco'
            self.temp['text'] = ''
            self.temp_min['text'] = ''
            self.temp_max['text'] = ''
            self.presion['text'] = ''
            self.humedad['text'] = ''
            self.viento['text'] = ''
            self.master.update()
            time.sleep(1)	    	
            self.aviso['text'] = ''
            self.localidad['text'] = ''				
    def widgets(self):
        self.inicio = PhotoImage(file ='buscar.gif')
        self.imagen_temp = PhotoImage(file ='tem.png')
        self.imagen_temp_min = PhotoImage(file ='minima3.png')
        self.imagen_temp_max = PhotoImage(file ='trm.png')
        self.imagen_humedad = PhotoImage(file ='humedad1.png')
        self.imagen_viento = PhotoImage(file ='viento1.png')
        self.imagen_presion = PhotoImage(file ='precipitacion1.png')
        self.bt_inicio = Button(self.frame, image= self.inicio, bg='red',highlightthickness=0, activebackground='white', bd=0, command = self.animacion)
        self.bt_inicio.grid(column=0, row=0, padx=2, pady=2)
        self.ingresa_ciudad = Entry(self.frame, font=('Comic Sans MS', 12),highlightbackground ="black", highlightcolor= "green2", highlightthickness=2)
        self.ingresa_ciudad.grid(column=1,row=0)
        Label(self.frame,text='Buscar',fg= 'black', bg='Turquoise1',font=('Comic Sans MS',10)).grid(column=2,row=0, padx=5)
        self.aviso = Label(self.frame,fg= 'red', bg='Turquoise1',font=('Comic Sans MS',12))
        self.aviso.grid(column=3,row=0, padx=5)
        self.localidad = Label(self.frame,fg= 'red', bg='Turquoise1',font=('Arial',20, 'bold'))
        self.localidad.grid(column=4,row=0, padx=5)

        Label(self.frame2,text='Temperatura', bg='yellow').pack(expand=True) #Kaufmann BT 
        Label(self.frame3,text='Temperatura Maxima', bg='red').pack(expand=True)
        Label(self.frame4,text='Temperatura Minima' , bg='deep sky blue').pack(expand=True)
        Label(self.frame5,text='Humedad' , bg='cyan2').pack(expand=True)
        Label(self.frame6,text='Viento' , bg='aquamarine').pack(expand=True)
        Label(self.frame7,text='Presión' , bg='sky blue').pack(expand=True)

        Label(self.frame2, image= self.imagen_temp, bg='yellow').pack(expand=True, side='left')
        Label(self.frame3, image= self.imagen_temp_max, bg='red').pack(expand=True, side='left')
        Label(self.frame4, image= self.imagen_temp_min, bg='deep sky blue').pack(expand=True, side='left')
        Label(self.frame5, image= self.imagen_humedad, bg='cyan2').pack(expand=True, side='left')
        Label(self.frame6, image= self.imagen_viento, bg='aquamarine').pack(expand=True, side='left')
        Label(self.frame7, image= self.imagen_presion, bg='sky blue').pack(expand=True, side='left')

        self.temp = Label(self.frame2,  bg='yellow',font=('Arial',25))
        self.temp.pack(expand=True, side='right')
        self.temp_max = Label(self.frame3,bg='red',font=('Arial',23))
        self.temp_max.pack(expand=True, side='right')
        self.temp_min = Label(self.frame4, bg='deep sky blue',font=('Arial',23))
        self.temp_min.pack(expand=True, side='right')
        self.humedad = Label(self.frame5, bg='cyan2',font=('Arial',23))
        self.humedad.pack(expand=True, side='right')
        self.viento = Label(self.frame6, bg='aquamarine',font=('Arial',20))
        self.viento.pack(expand=True, side='right')
        self.presion = Label(self.frame7, bg='sky blue',font=('Arial',20))
        self.presion.pack(expand=True, side='right')

if __name__ == "__main__":
    ventana = Tk()
    ventana.title('')
    ventana.config(bg='Darkslategray2')
    ventana.minsize(height= 330,width=670)
    ventana.resizable(0,0)
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='Clima.png'))
    ventana.geometry('500x300+180+80')
    app = Ventana(ventana)
    app.mainloop()