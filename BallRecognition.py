import cv2
import numpy as np

# 导入图片
if __name__ == '__main__':
    img = cv2.imread(r"D:\ana\red_ball.png")

    # 设置函数展示图片
    def cv_show(name, img):
        cv2.imshow(name, img)
        cv2.waitKey(0)

    # 寻找图片中的红色区域
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([0, 43, 46])
    high_hsv = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)

    # 通过中值滤波除去噪音点
    median = cv2.medianBlur(mask, 5)

    # 绘制最小矩形区域
    contours, hierarchy = cv2.findContours(median, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = contours[0]
    x, y, w, h = cv2.boundingRect(cnt)
    img2 = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv_show('img', img2)