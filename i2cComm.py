#!/usr/bin/python3


# -*- coding: utf-8 -*-
# """
# Spyder Editor
#
# This is a temporary script file.
# """
import smbus
import time
# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04


def writeNumber(value=[0]):
    print(value)
    bus.write_i2c_block_data(4, 0, value)
    # bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1


def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number


while True:
    var = []
    var1 = input("Enter a comand fucntion 13: ")
    var.append(int(var1))
    var2 = input("enter the first data bit")
    var.append(int(var2))
    var.append(0)
    var.append(0)
    if not var:
        continue

    writeNumber(var)
    print("RPI: Hi Arduino, I sent you ", var)
    # sleep one second
    time.sleep(1)

    number = readNumber()
    print("Arduino: Hey RPI, I received a digit ", number)
    print()
