# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    while True:
        year_str = input("Enter year (or press Enter to stop): ").strip()
        if year_str == "":
            break
        state = input("Enter state name: ").strip()
        pop_str = input("Enter population: ").strip()
        try:
            year = int(year_str)
            population = int(pop_str)
            all_entered_values.append([year, state, population])
        except ValueError:
            print("Invalid input. Year and population must be numbers.")
            continue
    # Now have the user enter a year. 
    try:
        year_to_sum = int(input("Enter a year to total populations for: "))
        sum_population_for_year(all_entered_values, year_to_sum)
    except ValueError:
        print("Invalid year entered.")
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    total = 0
    for record in all_entered_values:
        if record[0] == year_to_sum:
            total += record[2]
    # print the totalled population
    print(f"Total population for {year_to_sum}: {total}")

# Call the main function.
if __name__ == '__main__':
    main()