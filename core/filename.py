import os
import datetime

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def profile_upload_image_path(instance, filename):
	new_filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return f'profile/{final_filename}'