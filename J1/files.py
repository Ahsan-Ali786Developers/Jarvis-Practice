import os 
import shutil

def create_new_folder():
	folder_name = input("Enter your folder name : ").strip()

	if not folder_name:
		print("Folder name cannot be empty.")
		return
	if os.path.exists(folder_name):
		print("This folder already exists.")
		return
	
	os.mkdir(folder_name)
	print(f"Folder '{folder_name}' was created successfully!")

def organize_user_folder():
	path = input("Enter your folder address : ").strip()
	if not path:
		print("Folder path cannot be empty.")
		return
	if not os.path.isdir(path):
		print("Invalid folder path.")
		return

	categories = {
		".pdf": "PDFs",
		".mp3": "Audio",
		".jpg": "Images",
		".jpeg": "Images",
		".png": "Images",
		".mp4": "Videos",
		".inp": "Inpage",
		".py": "Python",
		".bat": "Batch",
	}
	files = os.listdir(path)

	for filename in files:
		src = os.path.join(path, filename)

		# skip folders
		if not os.path.isfile(src):
			continue
		
		_,ext = os.path.splitext(filename)
	
		folder_name = categories.get(
				ext.lower(),"others")

		dest_folder = os.path.join(path, folder_name)

		os.makedirs(dest_folder, exist_ok =True)

		dst = os.path.join(dest_folder, filename)
	
		shutil.move(src,dst)

		print(f"Moved {filename} -> {folder_name}\n")

		
