# simple_interest.py
# Sample script to calculate simple interest
# Licensed under Apache License 2.0

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    Formula: SI = (P * R * T) / 100
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    P = 10000  # principal amount
    R = 5      # annual interest rate (%)
    T = 2      # time in years

    SI = calculate_simple_interest(P, R, T)
    print(f"Simple Interest = {SI}")
