#this file includes all the basic vector functions we'll use for the raytracer
import math

class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x,
                    self.y + other.y,
                    self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x,
                    self.y - other.y,
                    self.z - other.z)

    def __mul__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.x * t.x,
                        self.y * t.y,
                        self.z * t.z)
        return Vec3(self.x * t,
                    self.y * t,
                    self.z * t)

    def __truediv__(self, t):
        return self * (1 / t)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return math.sqrt(self.dot(self))

    def unit(self):
        return self / self.length()
