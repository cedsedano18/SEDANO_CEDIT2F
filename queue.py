# ASSESSMENT 3.2 - LINEAR DATA STRUCTURE
# 4. QUEUE (FIFO)
# Name: CED HILLARY M. SEDANO
#
# Based on Assessment 3.1:
# Enqueue S, E, D, A, N, O, then dequeue the front element.

from collections import deque

def display_queue(queue):
    print("Current Queue (front -> rear):", list(queue) if queue else "EMPTY")

def main():
    queue = deque()

    print("================================")
    print("       QUEUE DATA STRUCTURE")
    print("       FIFO: First In, First Out")
    print("================================")

    print("\nENQUEUING LETTERS")
    for letter in ["S", "E", "D", "A", "N", "O"]:
        queue.append(letter)
        print(f"Enqueued: {letter}")
        display_queue(queue)

    print("\nDEQUEUING LETTERS FROM THE FRONT")
    while len(queue) > 0:
        removed = queue.popleft()
        print(f"Dequeued: {removed}")
        display_queue(queue)

    print("\nQueue is now empty.")
    print("Program ended.")

if __name__ == "__main__":
    main()
