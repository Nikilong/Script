#!/usr/bin/python
#Filename:mymodule.py

def sayhi():
    print 'hello'
    if __name__ == '__main__':
        print 'sayhi is itself'
    else:
        print 'sayhi is imported'
version = '0.1'

#End of mydodule.py