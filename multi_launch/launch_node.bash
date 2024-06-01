gnome-terminal --tab -t "Tab 1" -- bash -c "ros2 run joy_linux joy_linux_node"
sleep 1
gnome-terminal --tab -t "Tab 2" -- bash -c "ros2 run joy_linux joy_linux_node --ros-args -p autorepeat_rate:=30.0 -p deadzone:=0.000 --remap joy:=joy_sub"

