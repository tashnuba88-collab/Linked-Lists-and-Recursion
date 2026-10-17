from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    roster = LinkedList()

    # 2) Insert some sample data
    for employee_id in [101, 102, 103, 104, 105]:
        roster.insert_at_end(employee_id)

    # 3) Display the list to verify insertion
    print("Employee roster:")
    roster.display()

    # 4) Recursive sum
    print(f"\nSum of all IDs: {roster.recursive_sum()}")

    # 5) Recursive search
    for target in (103, 999):
        found = "found" if roster.recursive_search(target) else "not found"
        print(f"Search for ID {target}: {found}")

    # 6) Recursive reverse, then display
    roster.recursive_reverse()
    print("\nRoster after reversing:")
    roster.display()
