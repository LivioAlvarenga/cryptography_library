# Python program implementing Image Steganography

# O módulo PIL é usado para extrair pixels da imagem e modificá-la
from PIL import Image


# Converta dados de codificação em formato binário de
# 8 bits usando o valor ASCII de caracteres
def genData(data):

    # lista de códigos binários de dados fornecidos
    cod_bin = []

    for i in data:
        cod_bin.append(format(ord(i), "08b"))
    return cod_bin


# Os pixels são modificados de acordo com os dados binários
# de 8 bits e finalmente retornados
def modPix(pix, data):

    datalist = genData(data)
    lendata = len(datalist)
    img_data = iter(pix)

    for i in range(lendata):

        # Extraindo 3 pixels por vez
        pix = [
            value
            for value in img_data.__next__()[:3]
            + img_data.__next__()[:3]
            + img_data.__next__()[:3]
        ]

        # O valor do pixel deve ser ímpar para 1 e par para 0
        for j in range(0, 8):
            if (datalist[i][j] == "0") and (pix[j] % 2 != 0):

                if pix[j] % 2 != 0:
                    pix[j] -= 1

            elif (datalist[i][j] == "1") and (pix[j] % 2 == 0):
                pix[j] -= 1

        # O oitavo pixel de cada conjunto informa se deve parar
        # ou ler mais. 0 significa continuar lendo; 1 significa
        # que a mensagem acabou.
        if i == lendata - 1:
            if pix[-1] % 2 == 0:
                pix[-1] -= 1
        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(nova_img, data):
    w = nova_img.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(nova_img.getdata(), data):

        # Colocando pixels modificados na nova imagem
        nova_img.putpixel((x, y), pixel)
        if x == w - 1:
            x = 0
            y += 1
        else:
            x += 1


# Codificar dados em imagem
def encode():
    img = input("Digite o nome da imagem (com extensão): ")
    image = Image.open(img, "r")

    data = input("Insira os dados a serem codificados : ")
    if len(data) == 0:
        raise ValueError("Os dados estão vazios")

    nova_img = image.copy()
    encode_enc(nova_img, data)

    new_img_name = input("Digite o nome da nova imagem (com extensão): ")
    nova_img.save(new_img_name, str(new_img_name.split(".")[1].upper()))


# Decodifique os dados na imagem
def decode():
    img = input("Digite o nome da imagem (com extensão) :")
    image = Image.open(img, "r")

    data = ""
    img_data = iter(image.getdata())

    while True:
        pixels = [
            value
            for value in img_data.__next__()[:3]
            + img_data.__next__()[:3]
            + img_data.__next__()[:3]
        ]
        # string of binary data
        binstr = ""

        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += "0"
            else:
                binstr += "1"

        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data.strip()


# Main Function
def main():
    a = int(input(":: Welcome to Steganography ::\n" "1. Encode\n 2. Decode\n"))
    if a == 1:
        encode()

    elif a == 2:
        print("Decoded word- " + decode())
    else:
        raise Exception("Enter correct input")


# Driver Code
if __name__ == "__main__":

    # Calling main function
    main()
