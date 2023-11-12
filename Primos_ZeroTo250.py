
#Write a Python script to:
#Display all the prime numbers between 1 to 250.
#Store the results in a results.txt file.
#Test the script. Verify that it produced the expected results in the results.txt file.

primos = []

for i in range(1, 251):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            #print(i)
            primos.append(i)


with open("numeros.txt", "w") as file:
    file.write(str(primos))
