import pyrecover

disk_path+r"\\.\C:"
ntfs=pyrecover.NTFS(disk_path)
deleted_files+ntfs.find_deleted_files()
for deleted_file in deleted_files:
	print(deleted_file.filename)
