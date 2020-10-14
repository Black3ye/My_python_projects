#Programa realizado por Jose A. Garcia Osorio 
#Github profile https://github.com/Black3ye 
#Este programa utilizara el servidor de outlook para enviar un email desde la aplicacion.
#Recursos utilizado para orientacion Youtube, Stackoverflow y Documentacion de Python. 

#Librerias utilizadas:
import smtplib
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog,Text
from email.message import EmailMessage
import os


#Inicia el desarrollo de objetos con Tkinter
root = Tk()
root.iconbitmap(os.getcwd()+"\img\mail.ico")
root.title("Outlook Email Sender")
root.resizable(False,False)
canvas = Canvas(root, height= 500, width= 700, bg ="#212f3d")
canvas.pack()
frame = Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx =0.05, rely=0.05)
#Funcion para cargar los objetos utilizados para entrar data: subject, email's receiver y message.
def sender(usermail):    
    #Se declara los textvariables de los textboxs
    Destinario = StringVar()
    subject = StringVar()
    txtmsg = StringVar()
        
    #Se desarrolla el frame, textbox, label y button 
    canvas = Canvas(root, height= 500, width= 700, bg ="#212f3d")
    canvas.pack()  
    frame = Frame(root, bg="white")
    frame.place(relwidth=0.9, relheight=0.9, relx =0.05, rely=0.05)
    lblreceiver = Label(frame,text="Receiver's email:", bg="white").place(x=95,y=70)
    txtreceiver = Entry(frame,width=30,textvariable=Destinario)
    txtreceiver.place(x=100, y= 90)
    lblsubject = Label(frame,text="Subject:", bg="white").place(x=95,y=110)
    txtsubject = Entry(frame,width=40,textvariable=subject)
    txtsubject.place(x=100, y= 130)
    lblmessage = Label(frame,text="Message:", bg="white").place(x=95,y=150)
    txtmessage= Text(frame,width=60,height=7, wrap=WORD)
    txtmessage.place(x=100, y= 170)
    #Funcion send realiza el envio
    def send():
        #Se empieza adjuntar From, To, Subject y Mensaje
        msg = EmailMessage()
        msg['From'] = usermail
        msg['To'] = Destinario.get()
        msg['Subject'] = subject.get()
        message = txtmessage.get(1.0, END)
        msg.set_content(message)
        #Se envia el correo
        server.send_message(msg)
        messagebox.showinfo(title=None,message="Email Sended Correctly")

    btnprint = Button(frame,text="Send", command=send,width=10).place(x=545,y=415)
#Funcion para cagar objetos para garantizar el inicio de sesion
def login():
    usermail= StringVar()
    password= StringVar()
    lbltitle = Label(frame,text= "Outlook email sender",bg="white", font=("Ubuntu",24), fg="#212f3d").place(x=175, y=70)
    lblusermail = Label(frame,text="Your outlook email:", bg="white").place(x=170,y=150)
    txtusermail = Entry(frame,width=30,textvariable=usermail)
    txtusermail.place(x=300, y= 150)
    lblpassword = Label(frame,text="Your password:", bg="white").place(x=170,y=180)
    txtpassword = Entry(frame,width=30,show='*',textvariable=password)
    txtpassword.place(x=300, y= 180)
    #conectando al servidor de outlook
    try:
        global server
        server = smtplib.SMTP('smtp.outlook.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
    except:
        messagebox.showerror(title='Failure Connection', message='Outlook Email Sender need a conecction to the Internet')
        exit()

    #Funcion iniciando realiza el proceso de login en la cuenta de outlook
    def iniciando():
        try:
            server.login(usermail.get(), password.get())
            for obj in root.winfo_children():
                obj.destroy()
            sender(usermail.get())
        except:
            messagebox.showerror(title=None, message="Error: email o password incorrecto")

    btnLogin = Button(frame,text="Login", width=30 ,command=iniciando)
    btnLogin.place(x=200,y=225)
            

login()
root.mainloop()

