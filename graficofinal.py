from tkinter import *
import RPi.GPIO as GPIO
import controledeacesso
import fotos
import cv2
import time

id_cartao='teste'
id_foto='teste'



def identificar():
    resposta=controledeacesso.cartao()

    lb_txt_identificacao['text']=("Cartão identificado como " + resposta)
    global id_cartao
    id_cartao=resposta

def identificarimagem():
    camera_port = 0

    nFrames = 30

    camera = cv2.VideoCapture(camera_port)

    file = "./img/desconhecido.jpg"

    print
    "Digite <ESC> para sair / <s> para Salvar"
    emLoop = True
    num=10
    while (emLoop):

        retval, img = camera.read()
        cv2.imshow('Foto', img)

        k = cv2.waitKey(100)

        if k == 27:
            emLoop = False

        elif k == ord('s'):
            cv2.imwrite(file, img)
            emLoop = False



    cv2.destroyAllWindows()
    camera.release()
    idwebcam = fotos.identificacao()
    lb_txt_identificacao2['text'] = ("Identificação facial como " + idwebcam)
    global id_foto
    id_foto=idwebcam

def comparacaofinal():

    RELE = 17

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELE, GPIO.OUT)

    global id_cartao
    global id_foto

    if id_cartao == ['Cartão não identificado']:
        lb_txt_id_final['text']=('Entrada não permitida')

    else:
        if id_foto == id_cartao:
            lb_txt_id_final['text']=('Entrada liberada. Seja bem vindo {nome}!'.format(nome=id_cartao))
            GPIO.output(RELE, 1)
            time.sleep(2)
        else:
            lb_txt_id_final['text']=('Entrada Negada. O cartão apresentado é de {nome} e a webcam identificou {nome2}.'.format(nome=id_cartao,
                                                                                                                               nome2=id_foto))

    GPIO.cleanup()


# A janela1 é a que faz a identificação pelo rfid e apresenta na tela quem é o titular do cartão

janela1=Tk()
janela1.geometry('800x600')
janela1.title('Sistema de segurança')
janela1.configure(background='blue')

fr_quadro1=Frame(janela1, borderwidth=1, relief="solid")
fr_quadro1.place(x=25, y=10, width=750, height=250)
fr_quadro2=Frame(janela1,borderwidth=1, relief="solid")
fr_quadro2.place(x=25, y=280, width=750, height=250)


lb_texto_orientacao1 = Label(fr_quadro1, text ='Clique no botão e aproxime o cartão')
lb_texto_orientacao1.configure(font=("Arial", 12, "bold", "italic"))
lb_texto_orientacao1.place(x=200, y=10)



bt_rfid = Button(fr_quadro1, text='RFID', command = identificar)
bt_rfid.configure(font=("Arial", 16, "bold", "italic"))
bt_rfid.place(x=300, y=100)


lb_txt_identificacao=Label(fr_quadro2, text='')
lb_txt_identificacao.configure(font=("Arial", 16, "bold", "italic"))
lb_txt_identificacao.pack(side=LEFT)

bt_prosseguir = Button(fr_quadro1, text='Prosseguir-->', command =janela1.destroy)
bt_prosseguir.configure(font=("Arial", 16, "bold", "italic"))
bt_prosseguir.place(x=550, y=200)

janela1.mainloop()

#   Aqui finaliza a janela1 e inicia a janela2 que tem como objetivo fazer a captura da imagem
# e comparar com as imagens no banco de dados

janela2=Tk()
janela2.geometry('800x600')
janela2.title('Sistema de segurança')
janela2.configure(background='blue')

fr_quadro3=Frame(janela2, borderwidth=1, relief="solid")
fr_quadro3.place(x=25, y=10, width=750, height=250)
fr_quadro4=Frame(janela2,borderwidth=1, relief="solid")
fr_quadro4.place(x=25, y=280, width=750, height=250)

lb_txt_orientacao = Label(fr_quadro3, text ='Clique no botão para abrir a camera e digite s para salvar')
lb_txt_orientacao.configure(font=("Arial", 16, "bold"))
lb_txt_orientacao.place(x=70, y=10)

bt_camera = Button(fr_quadro3, text='Camera', command = identificarimagem)
bt_camera.configure(font=("Arial", 16, "bold", "italic"))
bt_camera.place(x=300, y=100)

lb_txt_identificacao2=Label(fr_quadro4, text='')
lb_txt_identificacao2.configure(font=("Arial", 16, "bold", "italic"))
lb_txt_identificacao2.pack(side=LEFT)

bt_prosseguir = Button(fr_quadro3, text='Prosseguir-->', command =janela2.destroy)
bt_prosseguir.configure(font=("Arial", 16, "bold", "italic"))
bt_prosseguir.place(x=550, y=200)

janela2.mainloop()

#   Aqui finaliza a janela2 e inicia a janela3 que finaliza o processo comparando se o titular do cartão
# é o mesmo identificado pela camera. Caso seja o mesmo ele manda uma carga ligando um rele para abrir a pota

janela3=Tk()
janela3.geometry('800x600')
janela3.title('Sistema de segurança')
janela3.configure(background='blue')

fr_quadro3=Frame(janela3, borderwidth=1, relief="solid")
fr_quadro3.place(x=25, y=10, width=750, height=250)
fr_quadro4=Frame(janela3,borderwidth=1, relief="solid")
fr_quadro4.place(x=25, y=280, width=750, height=250)

lb_txt_orientacao3 = Label(fr_quadro3, text ='Clique no botão para abrir a porta')
lb_txt_orientacao3.configure(font=("Arial", 16, "bold", "italic"))
lb_txt_orientacao3.place(x=180, y=10)

bt_abrir_porta = Button(fr_quadro3, text='Abrir Porta', command = comparacaofinal)
bt_abrir_porta.configure(font=("Arial", 16, "bold", "italic"))
bt_abrir_porta.place(x=300, y=100)

lb_txt_id_final=Label(fr_quadro4, text='')
lb_txt_id_final.configure(font=("Arial", 12, "bold"))
lb_txt_id_final.pack(side=LEFT)

janela3.mainloop()