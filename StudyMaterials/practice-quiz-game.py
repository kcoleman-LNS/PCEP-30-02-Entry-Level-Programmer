print('Welcome to my computer quiz!')

playing = input('Do you want to play a game? (y/n) ') # The space is so that when the users type it is propert punctuation...y

# We put in .lower for each answer so it converts it automatically
# If we wanted to store multiple valid answers, they would have to be inside a list or tuple and using the in eyword to check the users guess

if playing != 'y': # Conditionally check if true or false
    quit()

print("Great! Let's play!")

answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
else: # If the above is not true
    print('Incorrect.')

answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('Correct!')
else: # If the above is not true
    print('Incorrect.')

answer = input('Is Python a compiled language or interpreted language? ')
if answer.lower() == 'interpreted':
    print('Correct!')
else: # If the above is not true
    print('Incorrect.')

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit':
    print('Correct!')
else: # If the above is not true
    print('Incorrect.')