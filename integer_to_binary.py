


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
        while integer > 0:
            if integer & 1:
              bin=bin+str(1)
            else:
                bin=bin+str(0)
            integer=integer >> 1

    print(bin)


integer = int(input("enter a number"))

int_to_bin(integer)


