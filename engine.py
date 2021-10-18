import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    Alextian = reconhece_face("./img/Alextian.jpg")
    if(Alextian[0]):
        rostos_conhecidos.append(Alextian[1][0])
        nomes_dos_rostos.append("Alextian")

    roger1 = reconhece_face("./img/roger1.jpg")
    if(roger1[0]):
        rostos_conhecidos.append(roger1[1][0])
        nomes_dos_rostos.append("Roger")

    leandro = reconhece_face("./img/leandro.jpg")
    if (leandro[0]):
        rostos_conhecidos.append(leandro[1][0])
        nomes_dos_rostos.append("Leandro")
    
    return rostos_conhecidos, nomes_dos_rostos