import hashlib
original_url = input("short the url")
def shorten_url(newurl):
    result = hashlib.md5(newurl.encode())
    a = result.hexdigest()
    b = list(a)
    return "".join(b[:7])
r = shorten_url(original_url)
print("short url is \n https://bit.ly/" + r)
short_url = input(" url to find original:")
def get_original_url(m,n):
    newresult = hashlib.md5(n.encode())
    u = newresult.hexdigest()
    v = list(u)
    y="https://bit.ly/" + "".join(v[:7])
    if(y == m):
        return n
    else :
        return "404 not found"
print(get_original_url(short_url,original_url))
