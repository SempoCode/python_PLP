
#reading the file
def reading(filename):
    with open(filename, "r") as file:
        data = file.read()
        print(f"File content:\n\t{data}")

#writing to the file and then read it
def writing(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    reading(filename)

#Error handling   
try:
    filename = input("Enter the file name: ")
    reading(filename)
    content = input("Write new content:\n")
    writing(filename,content)
        
except FileNotFoundError:
    print("File not found")

