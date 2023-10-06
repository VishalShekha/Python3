firstRow = "qwertyuiop"
secondRow = "asdfghjkl"
thirdRow = "zxcvbnm"
rows = [firstRow,secondRow,thirdRow]
words = ["Hello","Alaska","Dad","Peace","cvm","8"]

def check_rows(row):
    for word in words:
        i =0 
        word = word.lower()
        for letters in word:
            for letter in row:
                if letter == letters:
                    i+=1
        if i == len(word):
            print(word)

for _ in rows:
    check_rows(_)