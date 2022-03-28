from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk

root=Tk()
root.title("Anime Power Level")
root.geometry("500x500")
root.configure(background="navyblue")
Anos(Demon King ) = ImageTk.PhotoImage(Image.open ("Anos")) 
Goku(Manga MUI) = ImageTk.PhotoImage(Image.open ("OIP.jpg"))
Omni Zeno Almighty = ImageTk.PhotoImage(Image.open ("almighty"))

label_planet= Label(root,text="Planet ",bg="blue")
label_planet_name= Label(root,font=("casteller",18,"bold"),bg="white")
label_planet_image=Label(root,bg="black",highlightthickness=5,borderwidth=2,relief=GROOVE)
label_planet_gravity_radius= Label(root,font=("casteller",18,"bold"),bg="white")
label_planet_info= Label(root,font=("casteller",10,"bold"),bg="white",wraplength=500)

planets=["Anos(Demon King)","Goku(Manga MUI)","Omni Zeno Almighty"]
selectedval=StringVar()
dropdown=ttk.Combobox(root,value=planets,textvariable=selectedval)

def PlanetInfo():
    planet=selectedval.get()
    if planet=="Anos(Demon King)":
        label_planet_name["text"]="Anos(Demon King)"
        label_planet_image["image"]=Anos
        label_planet_gravity_radius["text"]="Power Level:5(infinity)"
        label_planet_info["text"]="Level:Multiversal"
        
    elif planet=="Goku(Manga MUI":
         label_planet_name["text"]="Goku(Manga MUI)"
         label_planet_image["image"]=Oip
         label_planet_gravity_radius["text"]="Power Level:28 Septillion"
         label_planet_info["text"]="Level:Multiversal"
         
    elif planet=="Omni Zeno Almighty":
         label_planet_name["text"]=""
         label_planet_image["image"]=Almighty
         label_planet_gravity_radius_radius["text"]="Power Level:10 Nontillion"
         label_planet_info["text"]="Level:OmniVersal"

dropdown.place(relx=0.5,rely=0.1,anchor=CENTER)

btn = Button(root, text="Stats" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_planet.place(relx=0.2,rely=0.1 , anchor=CENTER) 
label_planet_name.place(relx=0.5,rely=0.25 , anchor=CENTER) 
label_planet_image.place(relx=0.5,rely=0.5 , anchor=CENTER) 
label_planet_gravity_radius.place(relx=0.5,rely=0.8 , anchor=CENTER)
label_planet_info.place(relx=0.5,rely=0.9 , anchor=CENTER) 

root.mainloop()