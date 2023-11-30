import random                                                    # Import the random module to generate random numbers
def random_birthdays(num_ppl):                                   # Define a function that can generate a list of the birthdays
    bdays = []                                                   # define the birthday as a list
    return [random.randint(1, 365) for x in range(num_ppl)]# this list can generate a random number in the range of "num_ppl"
def is_duplicated(birthday):                                     # This function can check if there are duplicated birthdays
    length_birthday = len(birthday)                              # name the length of the birthdays in 23 random people
    for a in range(length_birthday):                             # use the loop to compare each pair of the birthdays, "a" is the number that's comparing.
        for b in range(a + 1, length_birthday):                  # this loop can help to find the same birthday in the birthday list beside a.
            if birthday[a] == birthday[b]:                       # If there are a pair of birthday duplicated, return true
                return True
    return False                                                 # If it doesn't, return false
def birthday_counts(num_simulations, num_ppl):                   # This function can calculate out the times that the birthdays repeated.
    count_total = 0                                              # Set the original count as zero and add 1 after a birthday repeated.
    for x in range(num_simulations):                             # This loop can go through the specific times that the birthday paradox is going through
        random_list = random_birthdays(num_ppl)                  # name the random list of the birthdays for the random people
        if is_duplicated(random_list):
            count_total = count_total + 1                        # this loop can check if there are duplicated birthdays and can update the count number.
    percentage = count_total / num_simulations                   # this step can calculate the percentage of the probability based on the numbers we knew
    print(count_total)
    return percentage

def main():
    num_simulations = int(input("How many times would you like to simulate this problem? "))
                                                                 # Get the user's input of the times they want to simulate the code
    num_people = 23                                              # Set the number of the people
    probability = birthday_counts(num_simulations, 23)   # call the function to make num_simulations and num_ppl work
    print(f"After {num_simulations} times of rotate:")
    print(f"The probability of a birthday match in a group of {num_people} people is:")
    print(f"{probability:.0%}")                                  # This is the way to inserted value as a percentage(I searched on google).
if __name__ == "__main__":
    main()

