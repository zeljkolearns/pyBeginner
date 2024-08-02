# Exercise 2
## Objective: place all letters of "codeNIH is the best!" in an array AND print array elements 14 to 19


my_string = "codeNIH is the best!"

for i in range(14,19):
    print (my_string[i])


print(f"\n...OR...\n")
out = ""
for i in range(14,19):
    out = out + my_string[i]

print(out)