# A program that writes a file the nubers from 1  to 100
# displays their sqaures and squareroots
# Calculates the width of columns and use of app format options when writing the numbers.

#Step one: prompt user to enter the filename.
# open and write by printing number squared and sq.root. Use \t tab to create spaces btw the words.

def main():
    new_file = input("Enter the the filename to input values.")
    infile = open(new_file, "w")
    print("Processing ---")
    
    print("Number\tSquared\tSq.root", file = infile)
    print("------\t-------\t-------", file = infile)
#Step two add numbers from 1 to 100.
#Import math to calculate the sq,root.
#Store the details in the infile.
    for i in range(1, 100 +1):
        import math
        print(f"{i} \t {i**2} \t  {math.sqrt(i):.3f}", file = infile)

    infile.close()
    print("Assignment complete, GODAMN!")
        

    
main()
