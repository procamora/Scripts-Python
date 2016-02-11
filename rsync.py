#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################################################################
# Copyright (c) 2013 Pablo Rocamora <pablojoserocamora@gmail.com>          #
#                                                                          #
# Permission to use, copy, modify, and distribute this software for any    #
# purpose with or without fee is hereby granted, provided that the above   #
# copyright notice and this permission notice appear in all copies.        #
#                                                                          #
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES #
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF         #
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR  #
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES   #
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN    #
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF  #
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.           #
############################################################################


import os

def main():
    while True:
        print("1 - Hacer BackUp de debian desde kali (PORTATIL)")
        print("2 - Hacer BackUp de windows 8 desde kali o Debian7 (PORTATIL)")
        print("3 - Hacer BackUp de kali desde Debian7 (PORTATIL)")
        print("4 - Hacer BackUp de windows 7 desde kali (TORRE)")
        print("5 - Hacer BackUp de kali (TORRE)")
        print("6 - Salir")
        opc=eval(input ("Seleccione una Opcion :"))

        if opc==1:
            os.system("clear")
            os.system("echo 'Hacer BackUp desde kali'")
            os.system("sleep 3")
            os.system("rsync -av --delete /media/raiz/* /media/2TB/BackUp/portatil/debian7")
            os.system("rsync -av --delete /media/home/* /media/2TB/BackUp/portatil/debian7/home")
            os.system("clear")

        elif opc==2:
            os.system("clear")
            os.system("echo 'Hacer BackUp desde kali o Debian7'")
            os.system("sleep 3")
            os.system("rsync -av --delete /media/win8/* /media/2TB/BackUp/portatil/windows8")
            os.system("clear")

        elif opc==3:
            os.system("clear")
            os.system("echo 'Hacer BackUp desde Debian7'")
            os.system("sleep 3")
            os.system("rsync -av --delete /media/kali/* /media/2TB/BackUp/portatil/kali")
            os.system("clear")

        elif opc==4:
            os.system("clear")
            os.system("echo 'Hacer BackUp desde kali'")
            os.system("sleep 3")
            os.system("rsync -av --delete /media/win7/* /media/2TB/BackUp/torre/windows7")
            os.system("clear")

        elif opc==5:
            os.system("clear")
            os.system("echo 'Hacer BackUp desde kali'")
            os.system("sleep 3")
            os.system("rsync -av --delete /home/rocky/* /media/2TB/BackUp/torre/kali/home")
            os.system("clear")

        elif opc==6:
            os.system("clear")
            exit();

        else:
            os.system("clear")
            print("Opcion Invalida y/o Incorrecta.")


if __name__ == '__main__':
    main()