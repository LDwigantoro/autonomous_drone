# import library
import cv2 as cv

# inisiasi variabel cap untuk video capture
cap = cv.VideoCapture(0)

# membuat cascade untuk wajah dan mata
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# looping selama camera berjalan
while True:
    # menerima input dari karema
    ret, frame = cap.read()

    # mengubah image ke grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # mendeteksi wajah di grayscale
    # 1.3 = scale factor, berguna untuk mendeteksi wajah yang berukuran kecil diframe
    # 5 = minNeigbhros, berguna untuk mendeteksi wajah yang overlapping
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # mencetak berapa jumlah wajah yang terdeteksi
    print(len(faces))

    # looping dalam koodinat x dan y dan juga weight dan height dalam faces
    for (x, y, w, h) in faces:
        # mendeteksi wajah dalam kotak yang diberi warna biru
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # mengubah mata dalam faces menjadi grey agar bisa dideteksi
        eye_gray = gray[y:y+h, x:x+w]

        # memotong hanya bagian mata dalam faces
        eye_color = frame[y:y+h, x:x+w]

        # mendeteksi mata dalam wajah
        eyes = eye_cascade.detectMultiScale(eye_gray)

        # looping dalam koodinat ex dan ey dan juga weight dan height dalam mata
        for (ex, ey, ew, eh) in eyes:
            # mendeteksi mata dalam kotak yang diberi warna hijau
            cv.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv.imshow('frame', frame)

    # tekan 'q' pada keyboard untuk menghentikan kamera
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
