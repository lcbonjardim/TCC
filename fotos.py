import face_recognition as fr
from engine import reconhece_face, get_rostos

desconhecido = reconhece_face("./img/desconhecido.jpg")
if (desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nomes_dos_rostos = get_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

    # Verifica dentro de um range de rostos conhecidos se existe alguem igual
    for i in range(len(rostos_conhecidos)):
        resultado = resultados[i]
        if (resultado):
            print("Rosto do", nomes_dos_rostos[i], "foi reconhecido")
        # Se não tem ninguem igual ele devolve a mensagem que não encontrou nenhum rosto conhecido
        else:
            if i == len(rostos_conhecidos) and resultado == False:
                print("Nao foi encontrado nenhum rosto")
