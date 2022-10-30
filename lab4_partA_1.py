# A program that writes a file the nubers from 1  to 100
# Displays their sqaures and squareroots in three decimal places

#Step one: prompt user to enter the filename.
#Open and write by printing number squared and sq.root. Use \t tab to create spaces btw the words.

def main():
    new_file = input("Enter the the filename to input values.")
    infile = open(new_file, "w")
    print("Processing ---")
    
    print("Number\tSquared\tSq.root", file = infile)
    print("------\t-------\t-------", file = infile)
#Step two add numbers from 1 to 100.
#Import math to calculate the sq,root.
#Store the details in the infile.
#close the infile.
    for i in range(1, 100 +1):
        import math
        print(f"{i} \t {i**2} \t  {math.sqrt(i):.3f}", file = infile)

    infile.close()
    print("Assignment complete, GODAMN!")
        
 
main()

# opening and reading the contents of file created above.

def read_numbers():
    my_file = open("number.txt", "r")
    content = my_file.read()
    print(content)

    my_file.close()

read_numbers ()

