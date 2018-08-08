import cv2
import numpy as np
import os


#указания пути для сети
net = cv2.dnn.readNetFromTensorflow(os.path.join("Business_logic",'models','gan','generator.pb'),
                                    os.path.join("Business_logic",'models','gan','generator.pbtxt'))


#Найстройка входных значений
def getFace():
    inp = np.random.uniform(low =-1.0, high = 1.0, size = [1, 64]).astype(np.float32)
    inpout = np.random.uniform(low =-1.0, high = 1.0, size = [1, 64]).astype(np.float32)

    #Настройка сети
    net.setInput(inp)
    out = net.forward()


    out = np.reshape(out, [3, 64, 64])
    out = np.transpose(out, [1, 2, 0])



    #Нормализация выхода
    out = out + 1
    out = out / 2
    np.clip(out, 0, 1)
    out = cv2.resize(out, (480, 480))
    out = cv2.cvtColor(out, cv2.COLOR_RGB2BGR)
    out = out*255
    cv2.imwrite('Test.png', out)
    out = cv2.imread('Test.png')
    return (out)

# a = getFace()
#
#
# cv2.imshow("lol", a)
# cv2.waitKey()
#Вывод "крайних" лиц

