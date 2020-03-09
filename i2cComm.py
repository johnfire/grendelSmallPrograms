#!/usr/bin/python3
# i2c commmmprogram
#  chris rehm  7 marhc 2020
#
#

import smbus
import time

# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04


def writeNumber(value):
    print(value)
    bus.write_i2c_block_data(4, 0, value)
    # bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1


def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number


def getUserInput(msg):
    while True:
        try:
            answer = int(input(msg))
        except ValueError:
            print("not an integer, try again")
            continue
        if answer < 1 or answer > 255:
            print("Must be a number between 0 and 255")
            continue
        return answer


if __name__ == "__main__":
    # test mode we are testing the arduino communications system.
    # otherwise just call the functions above
    while True:
        var = []
        var1 = getUserInput("Enter a command function: ")
        var.append(var1)
        var2 = getUserInput("Enter the first data bit ")
        var.append(var2)
        var.append(0)
        var.append(0)
        if var1 == 999:
            break

        writeNumber(var)
        print("RPI: Hi Arduino, I sent you ", var)
        # sleep one second
        time.sleep(1)

        number = readNumber()
        print("Arduino: Hey RPI, I received a digit ", number)
        print()
