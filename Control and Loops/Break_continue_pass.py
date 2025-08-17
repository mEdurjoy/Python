for i in range(5):
    if i == 2:
        break  # Breaks the loop when i is 2
    print(i)
print("Loop ended with break and i is", i)

# Example of continue
print("\nUsing continue:")
i=0
for i in range(5):
    if i == 2:
        continue  # Skips the rest of the loop when i is 2
    print(i)
print("i is", i)

# Example of pass
print("\nUsing pass:")
for i in range(5):
    if i == 2:
        pass  # Does nothing when i is 2, but allows the loop to continue
    print(i)