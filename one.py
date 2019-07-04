import cv2

im = cv2.imread('lena.jpg', 0)

print(im)

cv2.imshow('lena', im)
key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('lena_black.png', im)
    cv2.destroyAllWindows()