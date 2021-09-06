import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
webcam.set(3, 1280)
webcam.set(4, 720)

det = HandDetector(detectionCon=0.65)

# img = cv2.imread(caminho da imagem) Nesse caso para imagens JPG
img = cv2.imread("Imagens/relogio.png", cv2.IMREAD_UNCHANGED) # Aqui para imagens em PNG
ox, oy = 200, 200

if webcam.isOpened():
    status, frame = webcam.read()
    while status:
        status, frame = webcam.read()
        frame = cv2.flip(frame, 1)
        mao, frame = det.findHands(frame, flipType=False)

        if mao:
            lmList = mao[0]['lmList'] # pegar as marcações dos pontos na mão
            # verificar se está clicado
            distancia, info, frame = det.findDistance(lmList[8], lmList[12], frame)
            print(distancia)
            if distancia < 60:
                cursor = lmList[8]
                if ox < cursor[0] < ox + w and oy < cursor[1] < oy + h:
                    ox, oy = cursor[0]-w//2, cursor[1]-h//2

        try:
            h, w, _ = img.shape
            # desenhar imagens em JPG
            # frame[oy:oy+h, ox:ox+w] = img

            # caso a imagem seja em PNG
            frame = cvzone.overlayPNG(frame, img, [ox, oy])

        except:
            pass
        cv2.imshow("webcam", frame)
        key = cv2.waitKey(1)

        if key == 27:
            break

webcam.release()
cv2.destroyAllWindows()