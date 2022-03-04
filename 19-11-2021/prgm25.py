#Accept a file name from user and print extension of that.
name= []
fname = input("Enter the filename:")
name = fname.split(".")
extension = name[1]
print("The extension of the file is : .",extension)
