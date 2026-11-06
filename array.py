# ASSESSMENT 3.2 - LINEAR DATA STRUCTURE
# 1. ARRAY
# Name: CED HILLARY M. SEDANO
#
# Based on Assessment 3.1:
# Add S, E, D, A, N, O, then remove from the last index.

def display_array(array):
    print("Current Array:", array if array else "EMPTY")

def main():
    array = []

    print("================================")
    print("       ARRAY DATA STRUCTURE")
    print("================================")

    print("\nADDING LETTERS")
    for letter in ["S", "E", "D", "A", "N", "O"]:
        array.append(letter)
        print(f"Added: {letter}")
        display_array(array)

    print("\nREMOVING LETTERS (LAST INDEX)")
    while len(array) > 0:
        removed = array.pop()
        print(f"Removed: {removed}")
        display_array(array)

    print("\nArray is now empty.")
    print("Program ended.")

if __name__ == "__main__":
    main()
