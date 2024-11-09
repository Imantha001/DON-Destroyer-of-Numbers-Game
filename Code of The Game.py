import random
import datetime

def generate_life_score():
    # Generate a random life score between 1 and 50 for the users
    return random.randint(1, 50)

def generate_enemies(attempt):
    # Generate enemies based on the attempt number
    if attempt <= 5:
        return [random.randint(15, 100) for _ in range(5)]
    elif attempt <= 10:
        return [random.randint(250, 2000) for _ in range(5)]
    elif attempt <= 15:
        return [random.randint(3000, 10000) for _ in range(5)]
    else:
        return [random.randint(20000, 100000) for _ in range(5)]

def play_game():
    # Ask for player's name and initialize game variables
    player_name = input("Enter your name: ")
    life_score = generate_life_score()
    max_attempts = 20
    current_attempt = 0
    won = False
    enemies = []
    
    while current_attempt < max_attempts:
        current_attempt += 1
        print("Attempt:", current_attempt)
        print(player_name + "'s life score is:", life_score)
        
        enemies = generate_enemies(current_attempt)
        print("Enemies:", enemies)
        
        try:
            selected_number = int(input("Select a number to fight: "))
            if selected_number not in enemies:
                print("No such enemy")
                break
            elif selected_number <= life_score:
                print(player_name + " killed", selected_number)
                life_score += selected_number
            else:
                print(player_name + " was defeated!!!")
                break
        except ValueError:
            print("Invalid input. Game over.")
            break

    if current_attempt == max_attempts:
        # After the Game over, Display final statistics of game session
        print("*** Game status ***")
        print("Player name:", player_name)
        print("Total attempts:", current_attempt)
        print("Final score:", life_score)
        print(player_name + " won the game")
        won = True

    write_to_file(player_name, current_attempt, enemies, selected_number, won, life_score)

def write_to_file(player_name, attempts, enemies, selected_number, won, final_score):
    # Generate a unique filename based on current date, time, and a random number
    current_datetime = datetime.datetime.now()
    random_number = random.randint(0, 9999)
    filename = "{}_{:02d}_{:02d}_{:02d}_{:02d}_{:02d}_{:04d}.txt".format(
        current_datetime.year, current_datetime.month, current_datetime.day,
        current_datetime.hour, current_datetime.minute, current_datetime.second,
        random_number
    )
    
    with open(filename, "w") as file:
        # Write game details to the file
        file.write("Player name: {}\n".format(player_name))
        file.write("Attempt: {}\n".format(attempts))
        file.write("Presented enemies: {}\n".format(enemies))
        file.write("User input number: {}\n".format(selected_number))
        file.write("Won/Lost status: {}\n".format('Won' if won else 'Lost'))
        file.write("Life score: {}\n".format(final_score))
        file.write("*** End game statistics ***\n")

# Run the game
play_game()
