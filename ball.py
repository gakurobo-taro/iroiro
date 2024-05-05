import cv2
import numpy as np
import random

times = int(input("何回?"))
for i in range(times):
    # 赤色と青色のボールの数
    red_count = 6
    blue_count = 6

    # 画像のサイズと各ボールのサイズ
    width = 500
    height = 200
    ball_size = 30

    # 赤色と青色のボールの色
    red_color = (0, 0, 255)  # BGR形式で指定
    blue_color = (255, 0, 0)  # BGR形式で指定

    # 画像の作成
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # ボールを配置する位置のリスト
    positions = [(x, y) for y in range(2) for x in range(6)]

    # 赤色のボールを配置
    for _ in range(red_count):
        pos_index = random.randint(0, len(positions) - 1)
        x, y = positions.pop(pos_index)
        cv2.circle(image, (x * 70 + 50, y * 100 + 50), ball_size, red_color, -1)

    # 青色のボールを配置
    for _ in range(blue_count):
        pos_index = random.randint(0, len(positions) - 1)
        x, y = positions.pop(pos_index)
        cv2.circle(image, (x * 70 + 50, y * 100 + 50), ball_size, blue_color, -1)

    # 画像を表示
    cv2.imshow('Balls', image)
    cv2.waitKey(0)

# 全ての画像を表示した後、ウィンドウを閉じる
cv2.destroyAllWindows()
