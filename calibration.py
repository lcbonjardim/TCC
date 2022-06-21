import cv2
import time, os

while (True):
    print("Para conocer los puertos escriba en consola:")
    print("ls /dev/v4l/by-path -lh")
    print("1. 0:1.2:1.0")
    print("2. 0:1.1.2:1.0")
    print("3. 0:1.1.3:1.0")
    print("4. 0:1.3:1.0")
    print("5. 0:1.4:1.0")
    print("6. 0:1.5:1.0")
    ports = {
        1: "0:1.2:1.0",
        2: "0:1.1.2:1.0",
        3: "0:1.1.3:1.0",
        4: "0:1.3:1.0",
        5: "0:1.4:1.0",
        6: "0:1.5:1.0"
    }
    cam = input("Escoge el puerto de la camara a calibrar: ")
    puerto = ports.get(cam, "invalido")
    print(puerto)
    if not (puerto == "invalido"):
        cap = cv2.VideoCapture(0)

        stat = cap.isOpened()
        print(stat)

        while (True):
            ret, frame = cap.read()
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
            time.sleep(.05)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()