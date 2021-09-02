# User Input
choice = int(input("Do you wan to convert string to binary[option:1] or binary to string[option:2]: "))

# Functions
def strToBin():
    query1 = str(input("Enter a string: "))
    resStrToBin = ''.join(format(ord(i), '08b') for i in query1)
    print("Our operators have done the job. Converted String to Binary, Result - " + resStrToBin + " .")

def binToStr():
    query2 = input("Enter a binary value: ")
    resBinToStr = ''.join(chr(int(query2[i*8:i*8+8], 2)) for i in range(len(query2)//8))
    print("Our operators have done the job. Converted Binary to String, Result - " + resBinToStr + " .")

if choice == 1:
    strToBin()

if choice == 2:
    binToStr()