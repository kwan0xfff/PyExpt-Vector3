#!/usr/bin/env python3
# Test of Vector3 class

from Vector3 import Vector3

v = Vector3()
v[0] = 1.0
v[1] = 2.0
v[2] = 3.0

print(v[0], v[1], v[2])
print(v)

v1 = Vector3(1.1, 2.2, 3.3)
print(v1)

v2 = Vector3(1,2)
print(v2)

v2 = Vector3(1)
print(v2)
