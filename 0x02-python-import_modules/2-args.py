#!/usr/bin/python3
if __name__ == "__main__":
 import sys
 if len(sys.argv) == 1:
  print("0 arguments.")
 elif len(sys.argv) == 2:
  print("1 argument:")
 elif len(sys.argv) > 2:
  print("{} arguments:".format(len(sys.argv) - 1))
  for i in range(len(sys.argv)):
   if i > 0:
    print("{}:".format(i), str(sys.argv[i]))
    i = i + 1
   
