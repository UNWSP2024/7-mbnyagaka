# Program #4: Coordinates
import math

# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
def distance(point1, point2):
    (x1, y1, z1) = point1
    (x2, y2, z2) = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
def main():
    try:
        # Get first point
        point1_str = input("Enter the first point as x,y,z (example: 1,2,3): ")
        x1, y1, z1 = [float(val.strip()) for val in point1_str.split(",")]
        point1 = (x1, y1, z1)

        # Get second point
        point2_str = input("Enter the second point as x,y,z (example: 4,5,6): ")
        x2, y2, z2 = [float(val.strip()) for val in point2_str.split(",")]
        point2 = (x2, y2, z2)

        # Call distance function
        d = distance(point1, point2)
        print(f"The distance between {point1} and {point2} is {d:.4f}")

    except Exception as e:
        print("Error: Please enter valid numeric coordinates in the correct format.")
# Call the main function
if __name__ == "__main__":
    main()