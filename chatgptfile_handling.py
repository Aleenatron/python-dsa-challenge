lst = "test.txt"

def process_list(lst):
    with open(lst, "r") as f:
        cnt = sum(word.lower() == "python" for line in f for word in line.split())
    
    print("Counts =", cnt)

process_list(lst)
