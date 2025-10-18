# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

def get_rainfall_for_year():
    rainfall = []
    for m in MONTHS:
        while True:
            try:
                val = float(input(f"Enter total rainfall for {m} (in inches): "))
                if val < 0:
                    print("Rainfall cannot be negative. Try again.")
                    continue
                rainfall.append(val)
                break
            except ValueError:
                print("Please enter a valid number.")
    return rainfall

def summarize_rainfall(rainfall):
    total = sum(rainfall)
    avg = total / 12
    max_val = max(rainfall)
    min_val = min(rainfall)
    max_month = MONTHS[rainfall.index(max_val)]
    min_month = MONTHS[rainfall.index(min_val)]
    print("\n--- Rainfall Summary ---")
    print(f"Total rainfall: {total:.2f} inches")
    print(f"Average monthly rainfall: {avg:.2f} inches")
    print(f"Highest month: {max_month} ({max_val:.2f} inches)")
    print(f"Lowest month: {min_month} ({min_val:.2f} inches)")

def main():
    rainfall = get_rainfall_for_year()
    summarize_rainfall(rainfall)

if __name__ == "__main__":
    main()
