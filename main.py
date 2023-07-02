from django.core.files.storage import FileSystemStorage
import uuid

folder='my_folder/'

myfile = request.FILES['image']

fs = FileSystemStorage(location=folder)

ext = myfile.name.split('.').pop()
new_filename =  str(uuid.uuid4())+'.'+ ext

filename = fs.save(new_filename, myfile)

file_url = filename
