import cv2

ruidos=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camara=cv2.VideoCapture(0)

while True:
    respuesta,captura=camara.read()
    if respuesta==False:break
    grises=cv2.cvtColor(captura,cv2.COLOR_BGR2GRAY)
    idcaptura=captura.copy()
    cara=ruidos.detectMultiScale(grises,1.5,3)
    for(x,y,e1,e2) in cara:
        cv2.rectangle(captura,(x,y),(x+e1,y+e2),(113,204,46),4)
                      
    cv2.imshow("Resultado de rostro",captura)                  
    
    if cv2.waitKey(1)==ord('c'):
        break
    
camara.release()
cv2.destroyAllWindows()     