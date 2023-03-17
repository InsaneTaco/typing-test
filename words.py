import time

text = "obese people are obese" # change to whatever you want
print(f'thing to type: "{text}"\n')
# stopwatch begins when the user hits enter
input("wpm is graded on accuracy. hit enter to begin test")
start_time = time.time()
test_input = input()
# stopwatch ends when user finishes typing and hits enter
end_time = time.time()

try:
    # gets elapsed time
    elapsed_time = end_time - start_time

    correct_count = len(text)

    # if input is less than text, missed characters are marked as wrong
    if len(test_input) < len(text):
        correct_count -= len(text) - len(test_input)

    # goes through each item in input
    for iteration in range(len(test_input)):
        # if user input is longer than text, everything higher is marked wrong
        if iteration > len(text)-1:
            correct_count -= 1
        elif text[iteration] != test_input[iteration]:
            correct_count -= 1

    # calculates accuracy
    if correct_count < 0:
        print("\nwoah there pal, we can't have none of that")
        quit()
    accuracy = correct_count/len(test_input)

    # calculates wpm
    word_count = correct_count/5
    wpm = 60*(word_count/elapsed_time)

    print(f"""\n    wpm: {round(wpm)}
    accuracy: {round(accuracy, 2)*100}%
    {correct_count} characters correct out of {len(test_input)} entered
    time typing: {round(elapsed_time, 2)} seconds\n""")

except:
    print("\nplease enter something. you are really not funny for doing this")