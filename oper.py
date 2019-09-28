
from matplotlib import pyplot as plt
import numpy as np
import cv2

def imag():
    image = np.zeros((512, 912, 3), np.uint8)

    cv2.line(image, (580, 350), (610, 290), (0, 255, 0), 4)
    cv2.line(image, (610, 290), (650, 350), (0, 255, 0), 4)

    cv2.rectangle(image, (180, 480), (200, 350), (0, 255, 0), 4)

    cv2.rectangle(image, (580, 480), (780, 350), (0, 255, 0), 4)# parede

    cv2.rectangle(image, (680, 390), (730, 430), (0, 255, 0), 4)# janela
    cv2.rectangle(image, (610, 400), (630, 480),(0, 255, 0), 4)  # porta
                    # esquer, cima,


    cv2.circle(image, (150, 350), 10, (0, 255, 0), 4)
    cv2.circle(image, (160, 340), 20, (0, 255, 0), 4)
    cv2.circle(image, (170, 360), 20, (0, 255, 0), 4)
    cv2.circle(image, (180, 350), 10, (0, 255, 0), 4)
    cv2.circle(image, (150, 240), 20, (0, 255, 0), 4)
    cv2.circle(image, (130, 270), 10, (0, 255, 0), 4)
    cv2.circle(image, (170, 260), 20, (0, 255, 0), 4)
    cv2.circle(image, (190, 250), 10, (0, 255, 0), 4)
    cv2.circle(image, (240, 280), 20, (0, 255, 0), 4)
    cv2.circle(image, (220, 270), 10, (0, 255, 0), 4)
    cv2.circle(image, (230, 260), 20, (0, 255, 0), 4)
    cv2.circle(image, (210, 250), 10, (0, 255, 0), 4)
    cv2.circle(image, (240, 345), 20, (0, 255, 0), 4)
    cv2.circle(image, (220, 370), 10, (0, 255, 0), 4)
    cv2.circle(image, (230, 365), 20, (0, 255, 0), 4)
    cv2.circle(image, (210, 350), 20, (0, 255, 0), 4)
    cv2.circle(image, (130, 300), 10, (0, 255, 0), 4)
    cv2.circle(image, (110, 320), 20, (0, 255, 0), 4)
    cv2.circle(image, (110, 300), 20, (0, 255, 0), 4)
    cv2.circle(image, (120, 340), 20, (0, 255, 0), 4)
    cv2.circle(image, (140, 360), 10, (0, 255, 0), 4)
    cv2.circle(image, (175, 300), 10, (0, 255, 0), 4)
    cv2.circle(image, (195, 320), 20, (0, 255, 0), 4)
    cv2.circle(image, (180, 300), 10, (0, 255, 0), 4)
    cv2.circle(image, (175, 340), 20, (0, 255, 0), 4)
    cv2.circle(image, (160, 360), 10, (0, 255, 0), 4)
    cv2.circle(image, (165, 270), 10, (0, 255, 0), 4)
    cv2.circle(image, (185, 275), 20, (0, 255, 0), 4)
    cv2.circle(image, (170, 265), 10, (0, 255, 0), 4)
    cv2.circle(image, (165, 285), 20, (0, 255, 0), 4)
    cv2.circle(image, (160, 300), 10, (0, 255, 0), 4)
    cv2.circle(image, (265, 290), 10, (0, 255, 0), 4)
    cv2.circle(image, (265, 255), 10, (0, 255, 0), 4)
    cv2.circle(image, (265, 325), 10, (0, 255, 0), 4)
    cv2.circle(image, (265, 315), 20, (0, 255, 0), 4)
    cv2.circle(image, (265, 310), 10, (0, 255, 0), 4)


    #mytext = "Hello World"
    #cv2.putText(image, mytext, (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

    cv2.imwrite("saida.jpg", image)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def histo():
    img = cv2.imread('saida.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converte P&B
    # Função calcular o hisograma da imagem
    h = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.figure()
    plt.title("Histograma")
    plt.xlabel("Intensidade")
    plt.ylabel("Qtde de Pixels")
    # plt.plot(h)
    # plt.xlim([0, 256])
    # plt.show()
    # cv2.waitKey(0)

    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()
