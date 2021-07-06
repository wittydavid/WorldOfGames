from Live import load_game, welcome

print(welcome("David"))
if load_game():
    print("Congratulations! you won!")
else:
    print("Sorry, you lost. Try again maybe?")
