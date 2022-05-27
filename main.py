# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string

def read_file_content(filename):
    # [assignment] Add your code here
    filename = open("story.txt", "r")
    print(filename.read())
    filename.close()
    
    
    return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    
    #open the file in read mode
    text = open("story.txt", "r")

    #create an empty dictionary
    d = dict()

    #loop through each line of the file
    for line in text:
        #remove spaces and newline characters
        line = line.strip()

        #convert characters to lowercase to avoid mismatch
        line = line.lower()

        #remove the punctuation mark
        line = line.translate(line.maketrans("", "", string.punctuation))

        #split the line into words
        words = line.split(" ")

        #iterate over each word
        for word in words:
            #check if word is already in dictionary
            if word in d:
            #increament count of word by 1
                d[word] = d[word]+1
            else:
                #Add to dictionary
                d[word] = 1

    #print the contents of dictionary
    for key in list(d.keys()):
        print(key, ":", d[key])
            

    return {"as": 10, "would": 20}


read_file_content("story.txt")
count_words()
