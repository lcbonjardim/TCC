import RPi.GPIO as GPIO
import cv2
import time
import controledeacesso
import fotos


def main(args):
    GPIO.setmode(GPIO.BOARD)
    # Define os pinos 11 e 13 como saida
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    # Apaga os leds
    GPIO.output(11, 0)
    GPIO.output(13, 0)
    try:
        #identifica o cartão rfid
        # se não identificar o cartão corta ai
        # se identificar o cartão vai para identificação pela webcam
        cartao=(controledeacesso.cartao())
        print(cartao)
        if cartao == ['Cartão não identificado']:
            print('Entrada não permitida')
            GPIO.output(13, 1)
            time.sleep(2)
        else:

            camera_port = 0

            nFrames = 30

            camera = cv2.VideoCapture(camera_port)

            file = "./img/desconhecido.jpg"

            print
            "Digite <ESC> para sair / <s> para Salvar"

            emLoop = True

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
            idwebcam=fotos.identificacao()
            if idwebcam==cartao:
                print('Entrada liberada. Seja bem vindo {nome}!'.format(nome=cartao))
                GPIO.output(11, 1)
                time.sleep(2)
            else:
                print('Entrada Negada. O cartão apresentado é de {nome} e a webcam identificou {nome2}.'.format(nome=cartao,nome2=idwebcam))
                GPIO.output(13, 1)
                time.sleep(2)
    finally:
        GPIO.cleanup()


    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
