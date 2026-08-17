def calculate_area(length,width):
    return length*width

print(calculate_area(4,5))
print(calculate_area(4,25))



with open("notes.txt",'w') as f:
    f.write("Learning Python\nDay-3 File Handling")
with open("notes.txt",'r') as f:
    r=f.read()
    print(r)

try:
    n=int(input("Enter a number: "))
    d=100/n
    print(d)

except (ZeroDivisionError, ValueError) as e:
    print('write a number',e)


