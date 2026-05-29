import sys

# WELCOME
print("\n", "="*12, "FILE TYPE IDENTIFIER", "="*12,"\n")

# HELP OUTPUT PRINTS IF NO DIRECTORY IS SPECIFIED
if len(sys.argv) < 2:
	print(f"Usage: python3 {sys.argv[0]} <path_to_file>")
	sys.exit(1)


# GRABS LOCATION OF FILE SPECIFIED
target_file = sys.argv[1]


# SPECIFYING SIGNATURE DATABASE
signature_lib = {
	b'\x89PNG': "PNG Image",
	b'%PDF': "PDF Document"
}



# USING TRY AND EXCEPT TO INTERCEPT CRASH ERRORS
try:
	# OPENS AND READS BINARY DATA OF FIRST 4 BYTES OF FILE
	with open(target_file, 'rb') as file:
		file_header = file.read(4)

	# LOOKING THROUGH OUR SIGNATURE DATABASE
	for signature, file_type in signature_lib.items():
		if file_header.startswith(signature):
			print(f"FILE TYPE IDENTIFIED: {file_type}")
			break
		else:
			print("UNKOWN FILE DETECTED OR SIGNATURE IN DATABASE!")
			break


except FileNotFoundError:	# ADDRESSES FILE NOT FOUND ERRORS
	print(f"ERROR! FILE {target_file} NOT FOUND. CHECK PATH AND TRY AGAIN.")
except PermissionError:         # ADDRESSES UNREADABLE FILES
	print(f"ERROR! ACCESS DENIED!")
