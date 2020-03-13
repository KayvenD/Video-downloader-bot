#!/usr/bin/env python

from os import path

class fileoperation:
    def create_file(filename:str):
        if not path.exists(filename):
            __fhndl = open(filename,"x")
            __fhndl.close()
            print(filename + " is created!")
        else:
            print("File is present!")

    def save_data(filename, data:str):
        if(data):
            data = data + "\n"
            __fhndl = open(filename,"a+")
            __fhndl.write(data)
            __fhndl.close()


class list_transfer:
    def addlist2file(filename:str,list):
        for i in list:
            fileoperation.save_data(filename,i)
            print(i + " successfully added!")


class collection_management:

    def getlist_from_a_file(__fpath):
        with open(__fpath, "r+") as __f:
            __list = list(__f)
        return __list
    def poplist(__list):
        __item = __list.pop()
        return __item





