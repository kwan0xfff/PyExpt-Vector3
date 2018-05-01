// Vector3

#ifndef _Vector3_h_
#define _Vector3_h_

class Vector3 {
  public:
    float x, y, z;
    Vector3 (float sx, float sy = 0.0, float sz = 0.0) :
        x(sx), y(sy), z(sz) { }
    Vector3() {}
    ~Vector3() {}
};

#endif // _Vector3_h_
