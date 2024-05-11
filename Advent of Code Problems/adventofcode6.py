
def main():
    input = get_input('c:/pythoncode/adventofcode6.txt')
    answer = find_marker(input)
    print(answer)
    

#read file and return string
def get_input(file):
    open_file = open(file)
    input_string = open_file.read()
    return input_string

#detect first set of four characters of unique letters
def find_marker(string):
    for i in range(len(string)):
        if string[i] not in [string[i+1], string[i+2], string[i+3]] and string[i+1] not in [string[i+2], string[i+3]] and string[i+2] not in [string[i+3]]:
            answer = i+4
            return answer

#return index of last character

if __name__ == '__main__':
    main()