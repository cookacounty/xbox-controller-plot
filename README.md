# Raspberry Pi XBOX Controller 2D plot
2D plot of an XBOX controller joystick using Python matplotlib and xboxdrv.
Run on a Raspberry Pi 3 Model B

Python class to control xbox was taken from https://github.com/FRC4564/Xbox

# Usage
1) Install these python packages
```
sudo apt-get install python-matplotlib
```
2) Edit the path in [xbox.py](xbox.py#L37) with your own path to xboxdrv (type which xboxdrv)

3) Run the plot (sudo is needed for xboxdrv)
```
sudo python plot_xbox.py
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
