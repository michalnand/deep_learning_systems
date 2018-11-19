LIBS_RYSY_PATH=$(HOME)/libs/rysy
export LIBS_RYSY_PATH

all:
	cd 01_classification_cpp && make -j4
	cd 02_classification_mnist_cpp && make -j4
	cd 03_regression_cpp && make -j4

clean:
	cd 01_classification_cpp && make clean
	cd 02_classification_mnist_cpp && make clean
	cd 03_regression_cpp && make clean
