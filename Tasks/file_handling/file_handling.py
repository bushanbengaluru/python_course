#file handling
#r - Read
#w - write
#a - append
#remove function to delete
import os
if os.path.exists("/Users/bushan/bushan_git_projects/python_course/Tasks/file_handling"):
    os.remove("/Users/bushan/bushan_git_projects/python_course/Tasks/file_handling")
else:
    print("The file does not exist")
# Create a new file
# f = open("/Users/bushan/bushan_git_projects/python_course/Tasks/file_handling", "w")
# # Write to the file
# f.write("Hello World\n")
# f.write("This is a test file\n")
# f.write("Python file handling\n")
# Close the file
f.close()
