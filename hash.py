import os

goingtobehashed = input("enter your text: ")
hashedtext = hash(goingtobehashed)
os.system('cls' if os.name == 'nt' else 'clear')
print(f"text: {goingtobehashed}")
print(f"hashed: {hashedtext}")
