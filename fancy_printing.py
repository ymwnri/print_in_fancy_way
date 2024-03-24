# Ask for name, last name and dream job
# Display the user info in a fancy way
# Print a progress bar while the program is loading

# Ask for user input
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
dream_job = input("Enter your Dream Job: ") 

# Print initializing bar
print("\nInitializing . . . . .")

def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

for i in range(101):
    progress(i)
    sleep(0.1)