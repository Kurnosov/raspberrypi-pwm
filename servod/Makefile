#CROSS_OPTS := CROSS_COMPILE=/usr/bin/arm-linux-gnueabi- ARCH=arm
CROSS_OPTS :=

all:	servod

servod:	servod.c
	gcc -Wall -g -O2 -o servod servod.c
	@echo "	modprobe -r servoblaster"

clean:
	rm -f servod servodemo

