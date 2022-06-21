from tkinter import *
import controledeacesso
import fotos
import cv2

def Clicktime (valid = False, sec=None):
    if valid == False:
        sec=10
    if sec==0:
        time['text']= 'Acabou!'
    else:
        sec-=1
        time['text']=sec
        time.after(1000, lambda: Clicktime(True,sec))

def identificar():
    resposta=controledeacesso.cartao()

    texto_identificacao1['text']=("Cartão identificado como " + resposta)

def identificarimagem():
    camera_port = 0

    nFrames = 30

    camera = cv2.VideoCapture(camera_port)

    file = "./img/desconhecido.jpg"

    print
    "Digite <ESC> para sair / <s> para Salvar"
    Clicktime()
    emLoop = True
    num=10
    while (emLoop):

        retval, img = camera.read()
        cv2.imshow('Foto', img)

        k = cv2.wait(100)


        if k == 27:
            emLoop = False

        elif k == ord('s'):
            cv2.imwrite(file, img)
            emLoop = False



    cv2.destroyAllWindows()
    camera.release()
    idwebcam = fotos.identificacao()
    texto_identificacao['text'] = ("Identificação facial como " + idwebcam)

janela1=Tk()
janela1.geometry('600x400')
janela1.title('Sistema de segurança')
texto_orientacao1 = Label(janela1, text ='Clique no botão e aproxime o cartão')
texto_orientacao1.configure(font=("Arial", 16, "bold", "italic"))
texto_orientacao1.grid(column=2, row=0, padx=70, pady=30)



botao1 = Button(janela1, text='RFID', command = identificar)
botao1.configure(font=("Arial", 16, "bold", "italic"))
botao1.grid(column=2, row=1, padx=50, pady=32)


texto_identificacao1=Label(janela1, text='')
texto_identificacao1.configure(font=("Arial", 16, "bold", "italic"))
texto_identificacao1.grid(column=2, row=3, padx=50, pady=72)

janela1.mainloop()

janela=Tk()
janela.geometry('600x400')
janela.title('Sistema de segurança')
texto_orientacao = Label(janela, text ='Clique no botão para identificação facial!')
texto_orientacao.configure(font=("Arial",16,"bold","italic"))
texto_orientacao.grid(column=2, row=0, padx=70, pady=30)



botao = Button(janela,text='Camera', command = identificarimagem)
botao.configure(font=("Arial",16,"bold","italic"))
botao.grid(column=2, row=1, padx=50,pady=32)

time=Label(janela, text='00', fg='blue')
time.place(x=65, y=130)

texto_identificacao=Label(janela, text='')
texto_identificacao.configure(font=("Arial",16,"bold","italic"))
texto_identificacao.grid(column=2, row=3, padx=50, pady=72)


janela.mainloop()