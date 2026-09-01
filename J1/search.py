import os

def search_google():
	search = input("What do you want to search? ").strip()
	if search:
		command = f"https://www.google.com/search?q={search}"
		print(f"{search} is searching...")
		os.system(f"start {command}")
	else:
		print("You did not enter anything to search.")