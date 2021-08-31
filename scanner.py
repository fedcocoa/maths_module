import sys

def printout(string):
    print(string)
    if len(sys.argv) == 4:
        out_file.write(string)

file_a = open(sys.argv[1],"r")
file_b = open(sys.argv[2],"r")

if len(sys.argv) == 4:
    out_file = open(sys.argv[3],"w")

lines_a = file_a.readlines()
lines_b = file_b.readlines()

differences = 0
for i in range(0,len(lines_a)):
    if lines_a[i].strip() != lines_b[i].strip():
        differences += 1
        printout(f"Difference on line {i+1}\n{lines_a[i]}{lines_b[i]}")
        contents_a = set(lines_a[i].strip().split())
        contents_b = set(lines_b[i].strip().split())
        if contents_a==contents_b:
            printout("Line has the same content.")
        if len(lines_a[i].strip()) != len(lines_b[i].strip()):
            printout(f"Length of a: {len(lines_a[i].strip())}\nLength of b: {len(lines_b[i].strip())}\n")
        else:
            printout("Length is the same.\n")

printout(f"Differences: {differences}")