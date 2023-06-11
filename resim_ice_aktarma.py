import cv2

# Resmi İçeri Aktarma
img = cv2.imread('messi5.jpg', 0)


# Resmi Görselleştirme
cv2.imshow('ilk resim', img)

k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messi_gray.png', img)
    cv2.destroyAllWindows()
    

# İlk olarak, 'cv2' modülünü import ediyoruz. Bu modül, OpenCV işlevlerine erişim sağlar.

# Ardından, 'imread' fonksiyonunu kullanarak 'messi5.jpg' adlı bir resmi yüklüyoruz. İkinci parametre olarak 0 kullanarak, resmi siyah beyaz formatta yüklüyoruz. 'img' değişkenine resmi atıyoruz.

# 'imshow()' fonksiyonunu kullanarak 'ilk resim' adında bir pencere açıyoruz ve 'img' değişkenindeki resmi gösteriyoruz.

# 'waitKey(0)' fonksiyonu, bir tuşa basılmasını bekler. 0 parametresi, bir tuşa basılana kadar beklemek anlamına gelir. Kullanıcının bir tuşa basması durumunda, tuşun ASCII değerini döndürür.

# Eğer kullanıcı 'ESC' tuşuna (ASCII değeri 27) bastıysa, 'destroyAllWindows()' fonksiyonunu kulllanarak tüm pencereleri kapatır ve programı sonlandırır.

# Eğer kullanıcı 's' tuşuna (ASCII değeri ord('s')) bastıysa, 'imwrite()' fonksiyonunu kullanarak 'img' değişkenindeki resmi 'messi_gray.png' adıyla kaydeder.

# Son olarak 'destroyAllWindows()' fonksiyonunu kullanarak tüm pencereleri kapatır ve programı sonlandırır.