#colorama used for more color variation 
import colorama

#random and os used for random functionality and os for clear screen 
import random, os

#login.py imported for user integration
import login

#gspread used for spreadsheet data handling
import gspread

#rand-word.py list imported to be utilised in game
from rand_word import word_choice

#imported specific aspects for data handle, color and titles
from google.oauth2.service_account import Credentials
from colorama import Fore, Back
from hangman_titles import title, gbye, gover, hangman_lives_dict

#scope used for data handling - credit love sandwich
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p_users')

#colorama init used as per colorama manual - see readme
colorama.init(autoreset = True)

#basic set variables to be used in functions 
# choices = random.choice(word_choice).upper()
# lives = 7
# show = list(len(choices)*'_')
# game_complete = False

# def c_letter(digit, choices):
#     '''
#     This functions checks if a specific letter is in random word
#     '''
#     for i in range(0, len(choices)):
#         digit = choices[i]
#         if uguess == digit:
#             show[i] = uguess
#     if '_' not in show:
#         return True
#     else:
#         return False



# def show_stats():
#     '''
#     Shows the status of your word
#     '''
#     os.system('clear')
#     print(hangman_lives_dict[7-lives])
#     print(show)
#     print(Fore.YELLOW + "You currently have",lives,"left!")

def generate_word():
    choices = random.choice(word_choice).upper()
    return choices

def game_body(choices):
    '''
    This function holds the majority of the functionality of hangman.
    from lives lost to letters being shown to the end game. To storing 
    guessed letters and number"
    '''
    lives = 7
    show = list(len(choices)*'_')
    guessed_letter = []
    guessed_word = []
    game_complete = False

    while game_complete == False and lives > 0:
        
        uguess = input(Fore.GREEN + "Please enter a letter!\n")
        uguess = uguess.upper()
        if len(uguess) == 1 and uguess.isalpha():
            
            if uguess in guessed_letter:
                print(Fore.RED + "You've already used",uguess,"! Be careful..")
            
            elif uguess not in choices:
                print(Fore.RED + uguess, "Is not in the word!")
                lives -= 1
                guessed_letter.append(uguess)
            
            else:
                print(Fore.GREEN + uguess, "is in the word! Keep it up!")
                guessed_letter.append(uguess)
                c_letter(digit, choices)
                game_complete = True

        elif len(uguess) == len(choices) and uguess.isalpha():
            
            if uguess in guessed_word:
                print('You already guessed the word')
            
            elif uguess != choices:
                print(Fore.RED + uguess, "Is not the word!")
                lives -= 1
                guessed_word.append(uguess)
            else:
                game_complete = True

        else:
            print(Fore.RED + "This is not a valid guess! Please try again...")
            show_stats()

game_body()

    #     if uguess == choices:
    #         game_complete = True
    #         show = choices
    #     if len(uguess) == 1 and uguess in choices:
    #         game_complete = c_letter(uguess, choices)

    #     else:
    #         lives -= 1
    #     show_stats()

    # if game_complete:
    #     print(Fore.YELLOW + "Congratulations, your guessing skills are most impressive")
    # else:
    #     print(Fore.RED + gover)
    #     print(Fore.RED + "The word was:", choices)

# def game_restart():
#     '''
#     Allows user to restart the game 
#     '''
    







# def main():
#     '''
#     Calls on all major functions
#     '''
#     y_n_prompt = login.user_login()
#     login.c_login(y_n_prompt)
#     title_intro()
#     game_body(choices)
    

# main()