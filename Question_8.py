#Write a function that checks if the passed parameter is a valid URL or not.

# lease also explain your reasoning.

def is_valid_url(url): #This function checks if the passed parameter is a valid URL or not.
    if url.startswith("http://") or url.startswith("https://"): #checking if the passed parameter starts with "http://" or "https://"
        return True #returning True if the passed parameter starts with "http://" or "https://"
    else: #if the passed parameter does not start with "http://" or "https://"
        return False #returning False

print(is_valid_url("http://www.prada.com")) #True
print(is_valid_url("https://www.prada.com")) #True
print(is_valid_url("www.prada.com")) #False
print(is_valid_url("prada.com")) #False

