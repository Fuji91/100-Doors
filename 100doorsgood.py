# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:44:13 2016

@author: fruzsi
"""

doors = 100


def number_of_doors():

    doors_list = [False]*int(doors)

    for n in range(0, int(doors)):
        for k in range(n, int(doors), n+1):
            if doors_list[k] is False:
                doors_list[k] = True
            elif doors_list[k] is True:
                doors_list[k] = False

    return doors_list                


def number_of_doors_print(doors_list):

    opened = []
    for x in range(0, int(doors)):
        if doors_list[x] is True:
            opened.append(x+1)

    print("The following doors are open: ", end='')
    print(*opened, sep=', ')

final_list = number_of_doors() 
number_of_doors_print(final_list)