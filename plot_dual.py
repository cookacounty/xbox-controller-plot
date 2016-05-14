"""
Plot Controller and 3D Sensor Data
"""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
import sensor3d as s3d
import xbox



class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        fig = plt.figure(figsize=(10,4))
        a1_z   = fig.add_subplot(1, 11, 1)
        a1_xy = fig.add_subplot(1, 11, (2, 6))
        a2_z   = fig.add_subplot(1, 11, 7)
        a2_xy = fig.add_subplot(1, 11, (8, 12))
        plt.tight_layout()
        fig.suptitle("3D Sensor and Xbox Controller Demo", fontsize=18)

        
        plt.setp(a1_z.get_xticklabels(), visible=False)
        plt.setp(a2_z.get_xticklabels(), visible=False)

        
        a1_z.set_title('3D Sensor Z')
        a2_z.set_title('Xbox L Z')
        
        a1_xy.set_title('3D Sensor XY')
        a2_xy.set_title('Xbox L XY')

        # Joy 1 Z
        a1_z.set_ylabel('z')
        self.line_z1 = Line2D([], [], color='blue', linewidth=20)
        a1_z.add_line(self.line_z1)
        a1_z.set_xlim(-1, 1)
        a1_z.set_ylim(-1, 1)

        # Joy 1 XY
        a1_xy.set_xlabel('x')
        a1_xy.set_ylabel('y')
        self.line_xy1 = Line2D([], [], color='green', linewidth=3)
        a1_xy.add_line(self.line_xy1)
        a1_xy.set_xlim(-1, 1)
        a1_xy.set_ylim(-1, 1)
        
        # Joy 2 Z
        a2_z.set_ylabel('z')
        self.line_z2 = Line2D([], [], color='blue', linewidth=20)
        a2_z.add_line(self.line_z2)
        a2_z.set_xlim(-1, 1)
        a2_z.set_ylim(0, 1)
        # Joy 2 XY
        a2_xy.set_xlabel('x')
        a2_xy.set_ylabel('y')
        self.line_xy2 = Line2D([], [], color='green', linewidth=3)
        a2_xy.add_line(self.line_xy2)
        a2_xy.set_xlim(-1, 1)
        a2_xy.set_ylim(-1, 1)

        animation.TimedAnimation.__init__(self, fig, interval=50, blit=True)

    def _draw_frame(self, framedata):
        joy1.read_angle()
        x1=[0, joy1.x*2]
        y1=[0, joy1.y*2]
        z1x=[0, 0]
        z1y=[0, joy1.z]
        
        x2=[0, joy2.leftX()]
        y2=[0, joy2.leftY()]
        z2 = joy2.leftThumbstick()
        z2x=[0, 0]
        z2y=[0, z2]
        
        self.line_z1.set_data(z1x, z1y)
        self.line_xy1.set_data(x1, y1)
        self.line_z2.set_data(z2x, z2y)
        self.line_xy2.set_data(x2, y2)


        self._drawn_artists = [self.line_z1, self.line_xy1, self.line_z2, self.line_xy2]

    def new_frame_seq(self):
        return iter(range(1))

    def _init_draw(self):
        lines = [self.line_z1, self.line_xy1, self.line_z2, self.line_xy2]
        for l in lines:
            l.set_data([], [])

ani = SubplotAnimation()

# Setup joystick 1
i2c_addr = 0x60
joy1 = s3d.Sensor3D(i2c_addr)
# Setup joystick 2
joy2 = xbox.Joystick()

# Fullsecreen
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())
#mng.full_screen_toggle()

# Show the plot, close the joystick if something goes wrong
try:
    plt.show()
finally:
    joy2.close()
