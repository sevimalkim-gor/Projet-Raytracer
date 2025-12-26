#we test the vec3 file to make sure the functions work
from vec3 import Vec3

v1 = Vec3(1, 2, 3)
v2 = Vec3(4, 5, 6)

v3 = v1 + v2
print(v3.x, v3.y, v3.z)
