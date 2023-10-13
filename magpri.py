class PrimeNumber:
    def is_prime(self, num):
        # Check if a number is prime
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

class MagicalPrimeNumber(PrimeNumber):
    def is_magical(self, num):
        # Define your magical properties here
        return num % 10 == 7  # Example: Magical if it ends with 7

# Dynamic input
input_number = int(input("Enter a number: "))

# Create an instance of MagicalPrimeNumber
magical_prime = MagicalPrimeNumber()

if magical_prime.is_prime(input_number):
    if magical_prime.is_magical(input_number):
        print(f"{input_number} is a magical prime!")
    else:
        print(f"{input_number} is a prime number, but not magical.")
else:
    print(f"{input_number} is not a prime number.")
