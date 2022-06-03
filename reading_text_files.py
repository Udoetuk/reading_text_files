# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    open_file = open( "C:/Users/USER/Desktop/Full stack code projects/Python_code_projects/reading-text-files-project/story.txt","r")
    read_file = open_file.read()
    open_file.close()
    
    return (read_file)
    #return "Hello World"

print(read_file_content("filename"))


def count_words():
   # [assignment] Add your code here
    text = read_file_content("filename")
    text_split = text.split()
    count = {}
    for i in text_split:
        if i in count:
            count[i] +=1
        else:
            count[i] =1
    return count            

    #return {"as": 10, "would": 20}
print(count_words())



