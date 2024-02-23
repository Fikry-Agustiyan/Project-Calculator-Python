from tkinter import*
from tkinter import messagebox

# menu login
root = Tk()
root.title("PROGRAM KALKULATOR_FIKRY AGUSTIYAN")
root.geometry("650x425+280+100")
root.resizable(0,0)
bold_font= ("Helvetica",16,"bold")

def open_kalkulator():
    window=Frame(root)
    window.pack(side=LEFT)
    window.configure(height=650,width=425)
    # Background Window

    def change_color(color):
        window.configure(background=color)


    menubar = Menu(root)
    root.config(menu=menubar)
    color_menu = Menu(menubar, tearoff=0)
    color_menu.add_command(label="Red", command=lambda: change_color("red"))
    color_menu.add_command(label="Green", command=lambda: change_color("green"))
    color_menu.add_command(label="Blue", command=lambda: change_color("blue"))
    color_menu.add_command(label="Yellow", command=lambda: change_color("yellow"))
    color_menu.add_command(label="White", command=lambda: change_color("white"))

    menubar.add_cascade(label="Color", menu=color_menu)


    entry= Entry(window,borderwidth=5,width=38,font=bold_font)
    entry.grid(row=0,column=0,columnspan=3,ipady=12,pady=10,padx=10)

    # Operasi Kalkulator
    def bilangan(number):
        entry.insert(END,number)

    def hasil():
        try:
            y=str(eval(entry.get()))
            entry.delete(0,END)
            entry.insert(0,y)
        except:
            messagebox.showinfo("Error","Syntax Error")

    def clear():
        entry.delete(0,END)
        
    # Tombol Operasi
    button_1=Button(window,text='1',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(1))
    button_1.grid(row=1,column=0)
    button_2=Button(window,text='2',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(2))
    button_2.grid(row=1,column=1)
    button_3=Button(window,text='3',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(3))
    button_3.grid(row=1,column=2)
    button_4=Button(window,text='4',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(4))
    button_4.grid(row=2,column=0)
    button_5=Button(window,text='5',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(5))
    button_5.grid(row=2,column=1)
    button_6=Button(window,text='6',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(6))
    button_6.grid(row=2,column=2)
    button_7=Button(window,text='7',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(7))
    button_7.grid(row=3,column=0)
    button_8=Button(window,text='8',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(8))
    button_8.grid(row=3,column=1)
    button_9=Button(window,text='9',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(9))
    button_9.grid(row=3,column=2)
    button_0=Button(window,text='0',font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan(0))
    button_0.grid(row=4,column=0)
    button_tambah=Button(window,text="+",font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan('+'))
    button_tambah.grid(row=2,column=3)
    button_kurang=Button(window,text="-",font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan('-'))
    button_kurang.grid(row=3,column=3)
    button_kali=Button(window,text="x",font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan('*'))
    button_kali.grid(row=4,column=2)
    button_bagi=Button(window,text="÷",font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=lambda:bilangan('/'))
    button_bagi.grid(row=4,column=1)
    button_clear=Button(window,text="clear",font=bold_font,padx=11,pady=21,width=10,borderwidth=4,command=clear)
    button_clear.grid(row=1,column=3)
    button_hasil=Button(window,text="=",font=bold_font,fg="blue",padx=11,pady=21,width=10,borderwidth=4,command=hasil)
    button_hasil.grid(row=4,column=3)

def on_closing():
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
open_kalkulator()
root.mainloop()