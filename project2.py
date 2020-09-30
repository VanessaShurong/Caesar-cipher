#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project 2 - Secret Code - Fall 2020
Author: <your name and VT pid here>

<describe the program here>

I have nither given or received unauthorized assistance on this assignment.
Signed: <type youe name here>
"""
import string
             
def get_shift_factor():
#This function should accept no parameters and should return a valid shift factor
#by the user. It should promot for and read the shift factor, then performace
#input validation, issuing an error message and rereading the sfift factor 
#until the user input is valid.
     shift = 0
     shift = int(input('Shift factor?'))
     while True:
         if (shift >= 1):
             return shift
         else:
             print("Error-Shift Factor must be greater than 0.")
             shift = input("Reenter Shift Factor?")
         
def encrypt(mode,plain_text,shift):
#This function should accept a string to encrypt and the shift factor to use.
#It should construct and return the corresponding encrypted message. 
    if mode == "E":
        encrypted = " "
        print()
        for c in plain_text:
                c_shifted = (ord(c) - ord(' ') + shift) % 95
                c_new = chr(ord(' ') + c_shifted)
                encrypted += c_new
        print("Encrypted Message:",encrypted)

def decrypt(mode,ciphertext,shift):
    if mode == "D":
        decrypted = " "
        print()
        for c in ciphertext:
                c_shifted = (ord(c) - ord(' ') - shift) % 95
                c_og = chr(ord(' ') + c_shifted)
                decrypted += c_og
        print("Original Message:",decrypted)

def main():
  print("Welcome to Cryptic2020!")
  print()
  mode = input("Encrypt(E),Decrypt(D),or Quit(Q)?")
  while mode in ["Encrypt","E","Decrypt","D"]:
      if mode == "E":
              plain_text = input("Original Message?")
              shift = get_shift_factor()
              encrypt(mode,plain_text,shift)
              print()
              mode = input("Encrypt(E),Decrypt(D),or Quit(Q)?")
      else:
              ciphertext = input('Encrypted Message?')
              shift = get_shift_factor()
              decrypt(mode,ciphertext,shift)
              print()
              mode = input("Encrypt(E),Decrypt(D),or Quit(Q)?")
  else:
      print()
      print("Thanks for using Cryptic2020!")

if __name__ == "__main__":
  main()

