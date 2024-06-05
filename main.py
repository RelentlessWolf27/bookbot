def fileopener():
    with open('books/frankenstein.txt') as f:
        filecontents = f.read()
        return filecontents

def lettercounter(file):
        lower_file = file.lower()
        each_letter = {}
        for letter in lower_file:
            if letter in each_letter:
                each_letter[letter] += 1
            else:
                each_letter[letter] = 1
        return each_letter

def wordcounter(file):
    number_of_words = len(file.split())
    return number_of_words

def main():
    file = fileopener()
    number_of_words= wordcounter(file)
    number_of_letters = lettercounter(file)
    aggregatereporter(number_of_words,number_of_letters)

def sort_on(dict):
    return dict["num"]
def aggregatereporter(number_of_words,number_of_letters):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{number_of_words} words found in the document")
        #Doing the letter seggregation part
        list_of_letter = []
        for letter,times in number_of_letters.items():
             if letter.isalpha() is True:
                  list_of_letter.append({"letter":letter,"num":times})
        list_of_letter.sort(key=sort_on,reverse=True)
        for letter in list_of_letter:
            print(f"The {letter['letter']} was found {letter['num']} times")
        
main()