from time import time, sleep
  
print("The test will start in:")
for i in range(5, 0, -1):   
    print(i)
    sleep(1)
print("Start typing...\n")


text = []

start = time()

while True:
    line = input()
    if not line:
        break

    text.append(line)
    end = time()
    elapsed_time = (end - start) / 60
    chart_count = sum(len(item) for item in text)
    word_count = chart_count /5
    wpm = round(word_count / elapsed_time)
    print(" your avrage type spedin ", wpm)

    if wpm < 30:
        print(" you are below avrage ")
    elif wpm < 40:
        print(" you are avrage ")
    elif wpm < 50:
        print(" you are above avrage")
    elif wpm < 60:
        print(" you typin speed is good")
