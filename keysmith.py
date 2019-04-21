#!/usr/bin/env python3

from sys import argv
from random import choice
from string import ascii_letters, digits, punctuation


def generate(length):
    """ Generate a complex password """

    characters = ascii_letters + digits + punctuation
    password = ""
    
    for i in range(int(length)): 
        password += choice(characters)

    return password


def help():
    """ Show the help dialog """

    print("")
    print("Basic Usage: ")
    print("    keysmith <action> [options]")
    print("")
    print("Available Actions: ")
    print("    -h  -  Show help dialog")
    print("    -g  -  Generate passphrase")
    print("")
    print("Available Options: ")
    print("    keysmith -g [length]")
    print("    length  -  Character length of the generated password. Default is 16")
    print("")

def get_action():
    """ Parse the command-line arguments and respond accordingly """

    if (len(argv) == 1):
        print("Too few arguments supplied. See keysmith -h for usage.")
        return
    if (argv[1] == "-h" or argv[1] == "--help"):
        help()
    elif (argv[1] == "-g" or argv[1] == "--generate"):
        if (len(argv) == 2): 
            print(generate(16))
        else: 
            print(generate(argv[2]))

get_action()



