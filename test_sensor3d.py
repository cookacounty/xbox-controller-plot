import sensor3d

s3d = sensor3d.Sensor3D(0x60)

s3d.read_angle()

print(s3d)
