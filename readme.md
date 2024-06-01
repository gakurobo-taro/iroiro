# きどうのしかた

## はじめにちゅうい！
同一ネットワーク上で自動機と手動機を動かしたいときは、いろいろ名前が被らないように
全ターミナルで「ROS_DOMAIN_ID」を設定してね！

```sh
export ROS_DOMAIN_ID={好きな数字(100くらいまでにしようね)}
```

## ろぼっとがわPC
```sh
source install/setup.bash (Robohand_msgにパスを通す)
cd refactored_manual_machine/refactored_manual_machine/
python3 refactored_manual_machine.py
```

## めいんこんとろーら
```sh
source install/setup.bash (Robohand_msgにパスを通す)
cd main_controller/main_controller/
python3 main_controller.py
```
```sh
ros2 run joy_linux joy_linux_node --ros-args -p autorepeat_rate:=30.0 -p deadzone:=0.000
```

## さぶこんとろーら
```sh
source install/setup.bash (Robohand_msgにパスを通す)
cd sub_comtroller/sub_comtroller/
python3 sub_comtroller.py
```
```sh
ros2 run joy_linux joy_linux_node --ros-args -p autorepeat_rate:=30.0 -p deadzone:=0.000 --remap joy:=joy_sub
```

# かんきょう
```sh
git clone https://github.com/gakurobo-taro/python_common_lib.git
git clone https://github.com/gakurobo-taro/refactored_manual_machine.git
git clone https://github.com/gakurobo-taro/sub_comtroller.git
git clone https://github.com/gakurobo-taro/main_controller.git
colcon build
source install/setup.bash
cd python_common_lib/
pip install -e .
```

# 使ってるpythonライブラリ(標準ライブラリ込み)
```txt
ros2周り全部
python-can
pyserial
numpy
customtkinter
tkinter
enum
typing
struct
random
itertools
math

```