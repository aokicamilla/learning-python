#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini

#ESTUDAR MELHOR O READLINE
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    #write is w
    # myfile =open("textfile.txt", "w+")
    
    # Open the file for appending text to the end
    #add is a
    # myfile =open("textfile.txt", "a+")

    # # write some lines of data to the file
    # for i in range (10):
    #     myfile.write("this is some new text\n")
    
    # # close the file when done
    # myfile.close()
    
    # Open the file back up and read the contents
    myfile =open("textfile.txt", "r")
    if myfile.mode == "r":
        # contents = myfile.read()
        # print(contents)
        fileLine = myfile.readlines()
        for x in fileLine:
            print(x)
    
if __name__ == "__main__":
    main()
