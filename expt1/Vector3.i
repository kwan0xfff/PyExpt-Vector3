%module Vector3

%{
#define SWIG_FILE_WITH_INIT
#include "Vector3.h"
%}

class Vector3 {
  public:
    float x, y, z;
};

