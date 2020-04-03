def enlarge(i):
    return i * 100

#remove the below from global scope so the program doesn't try to test it when we run pytest 
if __name__ == "__main__":
    #only runs this code if invoked from command line but not if imported from another file
    my_number = float(input("Please enter a number: "))
    n = enlarge(my_number)
    print("Enlarging the number:", n)