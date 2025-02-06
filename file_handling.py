#Python one-liner challenge

#Challenge: Write a one-liner that will count the number of times the word "Python" appears in a file.
lst = "test.txt"
def process_list(lst):
    f = open(lst, "r")
    cnt =0
    for x in f:
        print("Reading Line", x)
        word = x.split()
        for ch in word:
            # if ch == "Python":
            #     cnt+=1
            if ch.lower() == "python":
                cnt+=1

    print("counts = ")
    print(cnt)
process_list(lst)


