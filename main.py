from django.core.files.storage import FileSystemStorage

folder='my_folder/'
myfile = request.FILES['image']
fs = FileSystemStorage(location=folder)
filename = fs.save(myfile.name, myfile)
file_url = fs.url(filename)
