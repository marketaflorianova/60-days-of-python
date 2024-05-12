date = input("Enter today's date: ")
mood = input("How was your mood from 1 to 10? ")
thoughts = input("Share your thoughts: ")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)