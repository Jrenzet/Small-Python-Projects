#This program takes in a text file with 9 columns of crates (each crate
#is assigned its own letter) and a list of instructions. Each instruction 
#represents one movement of a certain amount of crates from one stack to another. 
#The program determines which letter will be associated with the crate on top of
#each stack (after all the instructions have been executed), and returns a string
#containing these letters

import pprint, re
def main():
    crate_formation = get_input('C:/pythoncode/adventofcode5.txt')
    crate_moves = get_moves('C:/pythoncode/adventofcode5.txt')
    final_formation = move_crates(crate_formation, crate_moves)
    top_crate_string = crate_string(final_formation)
    print(top_crate_string)

#input crates and stacks as list, each stack being its own
#respective list so that crates can be moved with append function
def get_input(file):
    #open file
    file_open = open(file)
    file_str = file_open.read()
    #create a list of crates from left to right
    crate_regex = re.compile(r'(\[\w\])|\s{4}')
    crates = crate_regex.findall(file_str)
    rows = [[],[],[],[],[],[],[],[],[]]
    counter = 0
    #rearrange crate lists so that each list represents a column
    for i in crates:
        if i != '':
            rows[counter].insert(0,i)
        counter += 1
        if counter == 9:
            counter = 0
    file_open.close()
    return rows

#get list of crate movement instructions
def get_moves(file):
    file_open = open(file)
    file_str = ''.join(file_open.readlines())
    #identify numbers in the instructions
    move_regex = re.compile(r'move (\d{1,2}) from (\d) to (\d)')
    moves = move_regex.findall(file_str)
    #convert instructions to integers
    moves_int = []
    for i in moves:
        moves_int.append(list(map(int, i)))
    file_open.close()
    return moves_int

#complete movement of crates
def move_crates(crate_list, moves):
    for i in moves:
        #slice crates to be moved
        crates_moved = crate_list[i[1] - 1][-i[0]:]
        #put the first crate moved on the bottom, second on top of that, and so on
        #crates_moved.reverse()
        #add crates to be moved to the new column
        crate_list[i[2] - 1].extend(crates_moved)
        #remove crates being moved from the old column
        del crate_list[i[1] - 1][-i[0]:]
    return crate_list

#read top crates and return single string
def crate_string(crate_formation):
    top_crates = []
    for i in crate_formation:
            if len(i) > 0:
                    top_crates.append(i[-1])
            else:
                    top_crates.append(' ')
    answer = ''
    for i in top_crates:
        answer += i
    return answer


if __name__ == '__main__':
    main()