# given/input
# countries=['India','USA', 'UK', 'UAE',.......]
# CAPITALS=['Delhi', 'Washington', 'London', 'Abu Dhabi',......]
# output
# enter a country name:India
# The capital city of India is Delhi

# Enter a country name: ABC
# ABC is not found
# HOW TO solve this?

# Given input
countries = ['India', 'USA', 'UK', 'UAE']
capitals = ['Delhi', 'Washington', 'London', 'Abu Dhabi']

# Function to get the capital of a country
def get_capital(country):
    index = countries.index(country) if country in countries else -1
    return capitals[index] if index != -1 else None

# Main program
while True:
    # User input
    country_name = input("Enter a country name: ")

    # Check if the user wants to exit
    if country_name.lower() == 'exit':
        print("Exiting the program.")
        break

    # Get the capital and display the result
    capital = get_capital(country_name)
    if capital:
        print(f"The capital city of {country_name} is {capital}")
    else:
        print(f"{country_name} is not found.")