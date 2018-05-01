# Makefile for Vector3

CXXFLAGS=-g -fPIC -I/usr/include/python3.5

all : Vector3.py _Vector3.so

Vector3.py Vector3_wrap.cc : Vector3.h Vector3.i
	swig -python -c++ -o Vector3_wrap.cc Vector3.i

Vector3_wrap.o : Vector3_wrap.cc

Vector3.o : Vector3.cc

_Vector3.so : Vector3_wrap.o Vector3.o
	g++ -shared Vector3.o Vector3_wrap.o -o _Vector3.so

clean :
	rm -f Vector3_wrap.c Vector3_wrap.cc Vector3_wrap.o

test : _Vector3.so
	python3 run.py

