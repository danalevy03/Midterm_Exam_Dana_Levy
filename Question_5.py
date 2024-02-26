#Write a function that finds all the occurrences of a certain pattern,that starts with “un” has unlimited number of letters and ends with “an”
# The function takes 1 parameter: the text to look into and returns the number of matches
def find_pattern(text): #This function finds all the occurrences of a certain pattern,that starts with “un” has unlimited number of letters and ends with “an”
    matches = 0 #initializing a variable to store the number of matches
    for i in range(len(text) - 4): #looping through the text
        if text[i:i+2] == "un" and text[i+2:i+4] != "an": #checking if the current index and the next index is "un" and the next two indexes are not "an"
            matches += 1 #incrementing the number of matches
    return matches #returning the number of matches

print(find_pattern("unman unman unman")) #3
print(find_pattern("unwanted unman hello")) #2
print(find_pattern("unwanted unman hello unman")) #3