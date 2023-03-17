import time

input("hit enter to start test, type whatever you want, and then hit enter to end test ")
start_time = time.time()
test_ch = input()
end_time = time.time()

if " " not in test_ch or len(test_ch)<15:
    print("\nur selling. you need at least 15 characters and one space")
    quit()

elapsed_time = end_time - start_time
word_count = len(test_ch)/5
wpm = 60*(word_count/elapsed_time)

print("\nwords per minute: "+str(round(wpm)))
print("time typing: "+str(round(elapsed_time,3))+" seconds")
print("characters typed: "+str(len(test_ch)))   