# ASSESSMENT 3.2 - LINEAR DATA STRUCTURE
# 3. STACK (LIFO)
# Name: CED HILLARY M. SEDANO
#
# Based on Assessment 3.1:
# Push S, E, D, A, N, O, then pop the top element.

def display_stack(stack):
    print("Current Stack (bottom -> top):", stack if stack else "EMPTY")

def main():
    stack = []

    print("================================")
    print("       STACK DATA STRUCTURE")
    print("       LIFO: Last In, First Out")
    print("================================")

    print("\nPUSHING LETTERS")
    for letter in ["S", "E", "D", "A", "N", "O"]:
        stack.append(letter)
        print(f"Pushed: {letter}")
        display_stack(stack)

    print("\nPOPPING LETTERS FROM THE TOP")
    while len(stack) > 0:
        removed = stack.pop()
        print(f"Popped: {removed}")
        display_stack(stack)

    print("\nStack is now empty.")
    print("Program ended.")

if __name__ == "__main__":
    main()
