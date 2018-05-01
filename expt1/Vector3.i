%module Vector3

%{
#define SWIG_FILE_WITH_INIT
#include "Vector3.h"
%}


class Vector3 {
  public:
    float x, y, z;
    Vector3(float sx, float sy = 0.0, float sz = 0.0) :
        x(sx), y(sy), z(sz) { }
    Vector3() {}
    ~Vector3() {}
  %extend {
    char* __str__() {
        static char temp[256];
        sprintf(temp, "[ %g, %g, %g ]", $self->x, $self->y, $self->z);
        return &temp[0];
    }
  }
};
