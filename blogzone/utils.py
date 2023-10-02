import uuid

def get_filename(filename, request):
    # Generate a UUID
    unique_id = str(uuid.uuid4())

    # Get the file extension from the original filename
    file_extension = filename.split('.')[-1]
    filename1 = filename.split('.')[0]

    # Create a new filename using UUID and the original file extension
    new_filename = f"{filename1}_{unique_id}.{file_extension}"

    return new_filename.upper()
