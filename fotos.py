import face_recognition as fr
from engine import reconhece_face, get_rostos


def identificacao():
    desconhecido = reconhece_face("./img/desconhecido.jpg")
    if (desconhecido[0]):
        rosto_desconhecido = desconhecido[1][0]
        rostos_conhecidos, nomes_dos_rostos = get_rostos()
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
        print(resultados)
        nome = 'Desconhecido'
        # Verifica dentro de um range de rostos conhecidos se existe alguem igual
        for i in range(len(rostos_conhecidos)):
            resultado = resultados[i]
            if (resultado):
                nome = nomes_dos_rostos[i]
                print("Rosto do", nome, "foi reconhecido")
            # Se não tem ninguem igual ele devolve a mensagem que não encontrou nenhum rosto conhecido
            elif i == len(rostos_conhecidos) and resultado == False:
                print("Nao foi encontrado nenhum rosto")

    return nome
