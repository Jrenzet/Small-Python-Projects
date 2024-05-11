import random
number_of_streaks = 0
total_experiments = [] #list to hold the lists of each 100 flip experiment
for experiment_number in range(10000): #for loop to run 100 coin flips 10000 times
    flips = [] #list to be filled with 100 flips then added to total_experiments
    for flip_number in range(100):
        flips.append(random.randint(0, 1)) # adds flip results to the list, 0 is heads, 1 is tails
    total_experiments.append(flips)

#we now have a list of 10,000 lists of 100 flip results

def checker(list):
    global number_of_streaks
    number_of_streaks = 0
    for s in range(len(total_experiments)):
        streak = 0
        for i in range(95):
            head_streak = 0
            tail_streak = 0
            for (x) in range(6):
                x += i
                if list[s][x] == 0:
                    head_streak += 1
                if list[s][x] == 1:
                    tail_streak += 1
                if head_streak == 6 or tail_streak == 6:
                    streak += 1
        if streak >= 1:
            number_of_streaks += 1

checker(total_experiments)
print('There is a ' + str(number_of_streaks/100) + '% chance of a streak.')
