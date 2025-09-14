import os
import random  # We will use this for the bonus challenges later

# --- 1. Set Up The World ---
# The maze is a 2D list where each inner list is a row.
# Feel free to design your own maze!
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#", "E", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]

# --- 2. Find the Starting Line ---
# We need to find the 'S' to know where our player starts.
# We'll use variables to store the player's coordinates (row and column).
player_row = 0
player_col = 0

# Loop through each row in the maze
for r_index, row in enumerate(maze):
    # Loop through each character (column) in the current row
    for c_index, char in enumerate(row):
        # If we find the start character 'S'
        if char == "S":
            player_row = r_index
            player_col = c_index
            # Exit the loops since we found our starting point
            break
    else:
        continue
    break

# --- 3. Build the Main Game Loop ---
# This loop will run forever until the player wins or quits.
while True:
    # --- DISPLAY LOGIC (moved from function) ---
    # Clear the console screen (works on Windows, Mac, and Linux)
    os.system("cls" if os.name == "nt" else "clear")

    print("--- The Labyrinth of ASCII ---")
    print("Use w/a/s/d to move. Find the exit (E)!")
    print("-" * 30)

    # Create a temporary copy of the maze to modify for display
    display_copy = [list(row) for row in maze]

    # Place the player 'P' on our temporary copy
    # We don't want to permanently change the 'S' or ' ' in the original maze
    if display_copy[player_row][player_col] != "E":
        display_copy[player_row][player_col] = "P"

    # Loop through the rows of the temporary maze and print them
    for row in display_copy:
        # The .join() method creates a string from the list of characters
        print(" ".join(row))
    print("-" * 30)
    # --- END DISPLAY LOGIC ---

    # --- Check for Win Condition ---
    # Has the player reached the exit 'E'?
    if maze[player_row][player_col] == "E":
        print("🎉 You found the exit! You have escaped the labyrinth! 🎉")
        break  # Exit the while loop to end the game

    # --- Handle Player Input ---
    move = input("Enter your move (w/a/s/d): ").lower()

    # Calculate the potential next position based on input
    next_row, next_col = player_row, player_col

    # --- Code the Movement Logic ---
    if move == "w":  # Up
        next_row -= 1
    elif move == "s":  # Down
        next_row += 1
    elif move == "a":  # Left
        next_col -= 1
    elif move == "d":  # Right
        next_col += 1
    else:
        print("Invalid move! Please use w, a, s, or d.")
        input("Press Enter to continue...")  # Pause for user to read
        continue  # Skip the rest of the loop and start from the top

    # --- Implement Collision Detection ---
    # Check if the next move is within the maze boundaries and not a wall
    if (
        0 <= next_row < len(maze)
        and 0 <= next_col < len(maze[0])
        and maze[next_row][next_col] != "#"
    ):
        # If the move is valid, update the player's position
        player_row = next_row
        player_col = next_col
    else:
        # If the move is invalid (hits a wall or goes off-map)
        print("🚫 You can't go there! 🚫")
        input("Press Enter to continue...")  # Pause for user to read

# This line will be printed after the loop ends
print("\nThanks for playing!")