# Raspberry Pi XBOX Controller 2D plot
2D plot of an XBOX controller joystick using Python matplotlib and xboxdrv.
Run on a Raspberry Pi 3 Model B

Python class to control xbox was taken from https://github.com/FRC4564/Xbox and slightly modified to not crash all the time

#### Tested with python 2.7.9 on the Raspberry Pi Raspbian 8.0

# Usage
1) Install xboxdrv https://github.com/xboxdrv/xboxdrv
```
sudo apt-get install xboxdrv
```
2) Install python packages 
```
sudo apt-get install python-matplotlib
```
3) Setup your env to run Python 2.7
4) Clone this repository
```
cd
git clone https://github.com/cookacounty/xbox-controller-2D-plot.git
cd xbox-controller-2D-plot
```
5) Run the plot! (sudo is needed for xboxdrv)
```
sudo python plot_xbox.py
```
```
sudo python plot_dual.py
```


![](https://github.com/cookacounty/xbox-controller-2D-plot/blob/master/2016-05-10%2023_27_37-raspberrypi_0%20-%20VNC%20Viewer.png?raw=true)

## BinaryNum
binarynum is a python class to deal with binary numbers
* Bit selection
* Fixed point representation
* Concatination
* Signed/Unsigned conversion
The class was written to parse the pure interger data that an interface such as I2C returns

## Sensor 3D
A class written to collect data from a 3D sensor
