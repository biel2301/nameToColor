import tkinter as tk
from tkinter import messagebox  # noqa: F401
root = tk.Tk()
root.geometry("300x300")
root.title("Your color")
def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'
alphabet = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,
            "g":7,"h":8,"i":9,"j":10,"k":11,"l":12,
            "m":13,"n":14,"o":15,"p":16,"q":17,"r":18,
            "s":19,"t":20,"u":21,"v":22,"w":23,"x":24,
            "y":25,"z":26}
print("Enter first name:")
firstName = input()
print("Enter middle name:")
midName = input()
print("Enter last name:")
lastName = input()
names = [firstName,midName,lastName]
red = 0
green = 0
blue = 0
for i in range(len(names)):
    for j in range(len(names[i])):
        if(i==0):
            red += alphabet[names[i][j].lower()]
        elif(i==1):
            green += alphabet[names[i][j].lower()]
        else:
            blue += alphabet[names[i][j].lower()]
# print(red,green,blue)
red *= 4
green*= 4
blue *= 4
# print(red,green,blue)

while(red>255):
    red-=256
while(green>255):
    green-=256
while(blue>255):
    blue-=256
print(f"Red = {red}, Green = {green}, Blue = {blue}")
print("Copy and paste version:")
print(f"{red},{green},{blue}")
root.configure(background = rgbtohex(red,green,blue))
root.mainloop()