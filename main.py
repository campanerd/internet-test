from tkinter import*
from PIL import Image, ImageTk
import speedtest



#cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#000000"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue
co6 = "#403d3d"  # Cinza / Gray


# Criando janela 
janela = Tk()
janela.title("Campaner Wifi")
janela.geometry("350x200")
janela.configure(bg=co1)
janela.resizable(width=FALSE, height=FALSE)




#divindo janela em dois frames
frame_logo = Frame(janela, width=350, height=60, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=140, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


#frame_logo
img_veloc = Image.open('veloc.png')
img_veloc = img_veloc.resize((55, 55))
img_veloc = ImageTk.PhotoImage(img_veloc)

l_logo_img = Label(frame_logo, height=60, image=img_veloc, compound=LEFT, padx=10,anchor='nw', font=('Ivy 16 bold'),  bg=co1)
l_logo_img.place(x=20, y=0)

l_logo_name = Label(frame_logo, text=' Davi\'s Internet Test', padx=10,anchor=NE, font=('Ivy 19 bold'),  bg=co1, fg=co4)
l_logo_name.place(x=74, y=10)

l_logo_linha = Label(frame_logo, width=350,anchor=NW, font=('Ivy 1'),  bg=co5)
l_logo_linha.place(x=0, y=57)


#funcao
def main():
    st = speedtest.Speedtest()

    download = f"{st.download() / 1_000_000:.2f}"
    upload = f"{st.upload() / 1_000_000:.2f}"

    l_down['text'] = download
    l_up['text'] = upload

    button_test['text'] = 'Test Again'
    button_test.place(x=138, y=100)

#frame_corpo

img_down_pil = Image.open('down.png')
img_down_pil = img_down_pil.resize((55, 55))
# versão Tk (para o label)
img_down_tk = ImageTk.PhotoImage(img_down_pil)
# invertendo
img_up_pil = img_down_pil.transpose(Image.FLIP_TOP_BOTTOM)
img_up_tk = ImageTk.PhotoImage(img_up_pil)


l_logo_down = Label(frame_corpo, height=60, image=img_down_tk, compound=LEFT, padx=10,anchor='nw', font=('Ivy 16 bold'),  bg=co1)
l_logo_down.place(x=125, y=35)
l_logo_up = Label(frame_corpo, height=60, image=img_up_tk, compound=LEFT, padx=10,anchor='nw', font=('Ivy 16 bold'),  bg=co1)
l_logo_up.place(x=170, y=35)

l_down = Label(frame_corpo, text='',anchor=NW, font=('Arial 28'),  bg=co1, fg=co6)
l_down.place(x=10, y=25)
l_mbps = Label(frame_corpo, text='Mbps download',anchor=NW, font=('Ivy 10'),  bg=co1, fg=co4)
l_mbps.place(x=15, y=70)

l_up = Label(frame_corpo, text='',anchor=NW, font=('Arial 28'),  bg=co1, fg=co6)
l_up.place(x=230, y=25)
l_mbps = Label(frame_corpo, text='Mbps upload',anchor=NW, font=('Ivy 10'),  bg=co1, fg=co4)
l_mbps.place(x=247, y=70)


button_test = Button(frame_corpo, command=main, text='Start Test', font=('Ivy 10 bold'), relief=RAISED,overrelief=RIDGE, bg=co5, fg=co1)
button_test.place(x=138, y=100)




janela.mainloop()
