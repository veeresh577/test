


def int_to_bin(integer):
    bin=str()
    if integer is 0:
        print(integer,"'s binary format is 0")
    else:
        """#r=0
        #while integer != 0:

         #   bin=integer%2
          #  r=r+bin*10
          #  integer=int(integer/2)"""
        while integer > 0:                         # actual code is here
            if integer & 1:
              bin=str(1)+bin
            else:
              bin=str(0)+bin
            integer=integer >> 1

    return bin


integer = int(input("enter a number"))


z=int_to_bin(integer)
print(z)
try:
  f=open('binary.txt','w')            # simply opening file and writing binary vales into it
  f.write(z)
except IOError("problem in opening file") as e:
    print(e)
finally:
    f.close()


