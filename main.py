# Importing essentials modules ::
import random

#Defining Nouns & Adjectives Lists ::
adjectives = ['Cool', 'Happy', 'Brave', 'Swift', 'Gentle']
nouns = ['Tiger', 'Dragon', 'Phoenix', 'Eagle', 'Wolf']

#Creating a function for User Preferences ::
def get_user_preferences():
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    return include_numbers, include_special_chars

#Defining functions for creating usernames ::
def generate_username(include_numbers, include_special_chars):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    if include_numbers:
        number = str(random.randint(0, 999))
        username += number

    if include_special_chars:
        special_chars = '!@#$%^&*()-_'
        username += random.choice(special_chars)

    return username

#Saving Usernames to a file
def save_usernames_to_file(usernames):
    with open('usernames.txt', 'w') as file:
        for username in usernames:
            file.write(username + '\n')
    print("Usernames successfully saved to 'usernames.txt'.")


#Combining above two function into main function ::
def main():
    print("Welcome to the Random Username Generator!")
    include_numbers, include_special_chars = get_user_preferences()

    num_usernames = int(input("How many usernames would you like to generate? "))

    usernames = []
    for _ in range(num_usernames):
        username = generate_username(include_numbers, include_special_chars)
        usernames.append(username)

    print("\nGenerated Usernames:")
    for uname in usernames:
        print(uname)

    save_option = input("Would you like to save these usernames to a file? (y/n): ").strip().lower()
    if save_option == 'y':
        save_usernames_to_file(usernames)
    else:
        print("Usernames not saved.")


if __name__ == '__main__':
    main()

