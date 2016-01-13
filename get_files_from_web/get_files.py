import urllib.request
import re
import threading
import os

def get_file(base_url, filename, destination_directory):
    try:
        urllib.request.urlretrieve(base_url + filename, destination_directory + filename)
    except Exception as e:
        print('Error in ' + base_url + filename + ': ' + str(e))

        
def get_filenames(base_url, extension):
    try:
        data = urllib.request.urlopen(base_url)
    except Exception as e:
        print('Error in ' + base_url + ': ' + str(e))
        return []
    page = str(data.read())
    # avoid the parent directory link which contains space
    return re.findall('<a href="([^ ]*?\\.' + extension + ')', page)

    
def get_files(base_url, extension):
    directory_name = "downloads/"
    try:
        os.stat(directory_name)
    except:
        os.mkdir(directory_name)       
    
    filenames = get_filenames(base_url, extension)
    for filename in filenames:
        t = threading.Thread(target=get_file, args=[base_url, filename, directory_name])
        t.start()
    

if __name__ == '__main__':
    get_files("http://csitprof.com/music/Shedevry_Instrumental_Muziki/", "mp3")
    