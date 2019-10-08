lib:
	gcc -Wall -shared -o spatialfilter.so -fPIC spatialfilter.c

test:
	gcc -Wall -shared -o test.so -fPIC test.c
	python test.py

