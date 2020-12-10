#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
   dirs = dir(hidden_4)
   dirs.sort()
   for d in dirs:
      if(d[0] != "_"):
          print(d)
