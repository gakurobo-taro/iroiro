import pyrealsense2 as rs

# パイプラインの設定
pipeline = rs.pipeline()
config = rs.config()

# 加速度センサーのストリームを有効にする
config.enable_stream(rs.stream.accel)

# ジャイロスコープのストリームも有効にする場合
config.enable_stream(rs.stream.gyro)

# ストリーミング開始
pipeline.start(config)

try:
    while True:
        # フレームセットを待機
        frames = pipeline.wait_for_frames()

        # 加速度センサーフレームを取得
        accel_frame = frames[0].as_motion_frame()
        if accel_frame:
            accel_data = accel_frame.get_motion_data()
            print("Accel:", accel_data.x, accel_data.y, accel_data.z)

        # ジャイロスコープフレームも取得する場合
        gyro_frame = frames[1].as_motion_frame()
        if gyro_frame:
            gyro_data = gyro_frame.get_motion_data()
            print("Gyro:", gyro_data.x, gyro_data.y, gyro_data.z)

finally:
    # ストリーミング停止
    pipeline.stop()