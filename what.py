import sys

# WELCOME
print("\n", "="*12, "FILE TYPE IDENTIFIER (Double D)", "="*12,"\n")

# HELP OUTPUT PRINTS IF NO DIRECTORY IS SPECIFIED
if len(sys.argv) < 2:
	print(f"Usage: python3 {sys.argv[0]} '<path_to_file>'")
	sys.exit(1)


# GRABS LOCATION OF FILE SPECIFIED
target_file = sys.argv[1]


# SPECIFYING SIGNATURE DATABASE
signature_lib = {
	# IMAGES
	b'\x89\x50\x4e\x47': "PNG Image",
	b'\xff\xd8\xff': "JPEG/JPG Image",
	b'\x47\x49\x46\x38': "GIF Image",

	# HEIC IMAGE (LOOKING PAST THE FIRST 4 BYTES)
	b'ftypheic': "HEIC Image",
	b'ftypmif1': "HEIC Image",

	# DOCUMENTS
	b'\x25\x50\x44\x46': "PDF Document",

	# ARCHIVES / COMPRESSED FILES
	b'\x50\x4b\x03\x04': "ZIP ARCHIVE (OR MODERN MICROSOFT OFFICE DOC: DOCX/XLSX/PPTX)",
	b'\x52\x61\x72\x21': "RAR ARCHIVE",
	b'\x1f\x8b': "GZIP COMPRESSED FILE",

	# EXECUTABLES / BINARIES
	b'\x4d\x5a': "WINDOWS EXECUTABLE (EXE/DLL)",
	b'\x7f\x45\x4c\x46': "LINUX EXECUTABLE (ELF)",

	# TEXT FILES (OPTIONAL BYTE ORDER MARKS)
    	b'\xef\xbb\xbf': "UTF-8 ENCODED TEXT FILE",
    	b'\xff\xfe': "UTF-16 (LE) ENCODED TEXT FILE",
    	b'\xfe\xff': "UTF-16 (BE) ENCODED TEXT FILE"
}



# USING TRY AND EXCEPT TO INTERCEPT CRASH ERRORS
try:
	# OPENS AND READS BINARY DATA OF FIRST 4 BYTES OF FILE
	with open(target_file, 'rb') as file:
		file_header = file.read(12)

	# LOOKING THROUGH OUR SIGNATURE DATABASE. THIS CHECKS THE FIRST 12 BYTES TO SEE WHETHER IT STARTS WITH ANYTHING IN SIGNATURE DATABASE OR PRESENT ANYWHERE IN HEADER
	for signature, file_type in signature_lib.items():
		if file_header.startswith(signature) or signature in file_header:
			print(f"FILE TYPE IDENTIFIED: {file_type}")
			break
	else:
		print("UNKOWN FILE DETECTED OR SIGNATURE NOT IN DATABASE!")


except FileNotFoundError:	# ADDRESSES FILE NOT FOUND ERRORS
	print(f"ERROR! FILE '{target_file}' NOT FOUND. CHECK PATH AND TRY AGAIN.")
except PermissionError:         # ADDRESSES UNREADABLE FILES
	print(f"ERROR! ACCESS DENIED!")
except IsADirectoryError:	# ADDRESSES DIRECTORY INPUT INSTEAD OF FILE INPUT ERRORS
	print(f"ERROR! '{target_file}' IS A DIRECTORY. PLEASE SPECIFY A FILE PATH.")
