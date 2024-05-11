while True:
    string = input("Please enter a string: ")
    def ispalindrome(word):
        word = word.lower()
        for i in range(len(word)):
            if word[0+i] == word [-1-i]:
                continue
            else:
                return False
        return True



    print(ispalindrome(string))
