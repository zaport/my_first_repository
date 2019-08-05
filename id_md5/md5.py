import hashlib
import urllib.request

'''md5 для файла на компьютере'''
def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

print(get_hash_md5('lck.txt'))


'''md5 для файла из интернета'''
def get_hash_md5_url_cont(content):
    m = hashlib.md5()
    while True:
        data = content.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()

url = 'http://tululu.org/txt.php?id=19200'
resource = urllib.request.urlopen(url)
print(get_hash_md5_url_cont(resource))
