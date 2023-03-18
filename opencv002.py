# -*- coding: utf-8 -*-
import cv2

# 画像の読み込み
img = cv2.imread("test.jpg", 1)

# ウィンドウの表示形式の設定
# 第一引数：ウィンドウを識別するための名前
# 第二引数：ウィンドウの表示形式
# cv2.WINDOW_AUTOSIZE：デフォルト。ウィンドウ固定表示
# cv2.WINDOW_NORMAL：ウィンドウのサイズを変更可能にする
cv2.namedWindow("img", cv2.WINDOW_NORMAL)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
#import cv2

# 画像の読み込み
#img = cv2.imread("test.jpg", 1)

# 読み込んだ画像の高さと幅を取得
#height = img.shape[0]
#width = img.shape[1]
#print height
#print width

# 画像のチャンネル数
#channel = img.shape[2]
#print channel # RGBで3

# width * height * channelの値
#size = img.size
#print size

# データ型
#dtype = img.dtype
#print dtype # uint (符号なし8bit整数：0 ~ 255)

# -*- coding: utf-8 -*-
#import cv2

# 画像の読み込み
#img = cv2.imread("test.jpg", 1)

# 読み込んだ画像の高さと幅を取得
#height = img.shape[0]
#width = img.shape[1]

# 画像のサイズを変更
# 第一引数：サイズを変更する画像
# 第二引数：変更後の幅
# 第三引数：変更後の高さ
#resized_img = cv2.resize(img,(width/2, height/2))

#cv2.imshow("img", resized_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()