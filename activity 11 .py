count = int(input("How many numbers to convert? "))

for _ in range(count):
    num = int(input("Enter a decimal number: "))
    binary = ""
    
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    print("Binary:", binary)
