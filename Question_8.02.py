#also add the .com or .org or .net or .gov or .edu or .mil or .int at the end of the URL
#also check if the URL contains any spaces or not

def is_valid_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        if url.endswith(".com") or url.endswith(".org") or url.endswith(".net") or url.endswith(".gov") or url.endswith(".edu") or url.endswith(".mil") or url.endswith(".int"):
            if " " in url:
                return False
            else:
                return True
        else:
            return False
    else:
        return False

print(is_valid_url("http://www.prada.com")) #True
print(is_valid_url("https://www.prada.com")) #True
print(is_valid_url("www.prada.com")) #False
print(is_valid_url("prada.com")) #False
print(is_valid_url("http://www.prada.com ")) #False
print(is_valid_url("http://www.prada.pe")) #False
print(is_valid_url("http://www.prada.com.pe")) #False
print(is_valid_url("http://www.zara.com")) #True
