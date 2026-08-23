import os 
import shutil
def create_folder(name):
	os.mkdir(f'{name}')

def organize_downloads(path):
	categories = {
		".pdf": "PDFs",
		".mp3": "Audio",
		".jpg": "Images",
		".jpeg": "Images",
		".mp4": "Videos",
		".inp": "Inpage",
		".py": "Python",
		".bat": "Batch",
	}
	files = os.listdir(path)
	for filename in files:
		_, ext = os.path.splitext(filename)
		folder_name = categories.get(ext.lower(), "Others")
		dest_folder = os.path.join(path, folder_name)
		os.makedirs(dest_folder, exist_ok=True)

		src = os.path.join(path, filename)
		dst = os.path.join(dest_folder, filename)

		if os.path.isfile(src):
			shutil.move(src,dst)
			print(f"Moved {filename} -> {folder_name}/")
