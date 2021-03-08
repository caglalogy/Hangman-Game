from random import choice 

# read word list from words.txt 
def readFile(file_name):
    wordList = []
    with open(file_name, 'r', encoding='utf8') as myFile:
        for row in myFile:
            data=row.rstrip('\n')
            wordList.append(data)
        
    return wordList   

# to find given letter in the map and return map back to main
def findCharacter(word,letter,map):
    for i in range(len(word)):
        if word[i] == letter:   map[i] = letter
    return map
            
    
def main():
    usedLetters = list()
    fileName = "words.txt"
    wordList = readFile(fileName)
    word = choice(wordList).lower()
    wordLen = len(word)

    # conflicts in team
    if wordLen < 5:     lives = 5
    else:               lives = wordLen

    map = list([])

    for _ in range(wordLen):
        map.append('_')

    mapStr = ' '.join(map)
    print(mapStr)

    while (mapStr[0::2] != word) and lives > 0:
        
        letter = input("give me a letter: ").lower()

        if len(letter) != 1:
            print("LETTER PLEASE")
            continue

        while letter in usedLetters:
            print("this letter has already used.")
            letter = input("give me another letter:")
        
        usedLetters.append(letter)

        # compare the before and after versions of maps
        map1 = list(map)
        map = findCharacter(word,letter,map)
        map2 = list(map)

        if(map1 == map2):
            lives -=1
            print("WRONG GUESS!")
            print("{} lives left.".format(lives))
        
        mapStr = ' '.join(map)
        print(mapStr)
        print("........................................................")
    # end of while

    # end of the game..
    if lives > 0:  print("you won!!!unlem1!")
    else:          print("you have no more lives")
    print("the word was.." , word)

main()