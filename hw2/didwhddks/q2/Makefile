CXX := g++
PYBIND11_INC := $(shell python3 -c "import pybind11; print(pybind11.get_include())")
PYTHON_INC := $(shell python3-config --includes | awk '{print $1}' | sed 's/-I//')

# Manually specify framework linkage for macOS
PYTHON_LDFLAGS := -framework Python

CXXFLAGS := -O3 -Wall -shared -std=c++11 -fPIC -I$(PYBIND11_INC) -I$(PYTHON_INC)

all: calc_angle.so

calc_angle.so: bindings.cpp calc_angle.hpp
	${CXX} ${CXXFLAGS} ${PYTHON_LDFLAGS} bindings.cpp -o calc_angle$(shell python3-config --extension-suffix)

test: unit_test.py calc_angle.so
	python3 -m pytest -v unit_test.py

clean:
	rm -f calc_angle.so