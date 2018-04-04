#!/usr/bin/env python

"""
@author: Alexander D Leech
@date:   04/04/2018
@rev:    1
@lang:   Python 2.7
@deps:   <None>
@desc:   Main class file used when coding pretty much any python program
"""

# Your functions go here
# For example:

def helloWorld():
  print("Hello world!")



# Everything below this line goes at the bottom of your main file,
#  and should only be used to call the primary function your going
#  to use to execute the code, in this case, helloWorld. I'm 
#  introducing this early as its a good habbit to get into now
#  rather than have to relearn it later on.

def main():
    helloWorld()
    
if __name__ == '__main__': main()

# When using repl.it, replace line 29 with just main(). As its an
#  online IDE, it doesnt have the full functionality of normal python
