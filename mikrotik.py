#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import os
import sys


def main():
    fecha = time.strftime("%Y%m%d-%S")
    routers = ['mks1', 'mks2',]

    if sys.platform == 'win32':
        ruta= ''
    else:
        ruta = '/home/procamora/mikrotik-backup/'# esto se pone asi por el cron y las variables relativas


    for router in routers:
        if not os.path.exists('%s%s'%(ruta, router)):
            os.mkdir('%s%s'%(ruta, router))
            
        mk = '%s.procamora.es'%router
        print(mk)

        if sys.platform == 'win32':
            comando = 'echo y | plink.exe -l admin -pw PASSWORD %s export > %s%s/%s-%s.rsc'%(mk, ruta, router, fecha, router)
        else:
            comando = 'echo y | plink -l admin -pw PASSWORD %s export > %s%s/%s-%s.rsc'%(mk, ruta, router, fecha, router)

        try:
            print(comando)
            os.system(comando)
        except Exception as e:
            print(('Error:' + mk))

    print('fin')


if __name__ == '__main__':
    main()