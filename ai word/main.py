import random
import numpy
import turtle
screen = turtle.Screen()
turtle = turtle.Turtle()


file = open("wieghts.txt", "r")
wieghts = file.read()
wieghts = wieghts.split()
file.close()
file = open("wordlist.10000.txt", "r")
words = file.read()
words = words.split()
file.close()

populaition1 = []
populaition2 = []
populaition3 = []
populaition4 = []
realpop = []
populaition6 = []
populaition7 = []
populaition9 = []
populaition10 = []

fake_wieghts = []
response = ""
real_wieght = wieghts

def random_mem():
    global wieghts
    global real_wieght
    global fake_wieghts
    fake_wieghts = real_wieght
    for i in fake_wieghts:
        fake_wieghts[i] = random.uniform(0, 1)
    wieghts = fake_wieghts


inputt = "hello"




def brainstorm():
    global wieghts
    global words
    global response
    global inputt
    global turtle
    response = ""
    input_words = inputt.split(" ")
    for i in input_words:
        if words.__contains__(i):
            pass
        else:
            print("error")
            break
        if len(input_words) > 10000:
            print("error")
            break
        conts = 10000 - len(input_words)
    wieght_index = 0
    final = []
    temp_final = []
    calculaitions = []

    for i in range(0, 1001):
        calculaitions = []
        turtle._tracer(0, 0)
        for j in range(0, 10001):
            skip = "false"
            if j + 1 > len(input_words):
                skip = "true"
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            if skip == "true":
                x = 0
            else:
                x = words.index(input_words[j]) + 1
            turtle.forward(1)
            y = float(x) * float(wieghts[wieght_index])
            calculaitions.append(y)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
        turtle._update()
    print("loading1")
    for i in range(0, 10000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    print("loading2")
    for i in range(0, 110000):
        calculaitions = []
        turtle._tracer(0, 0)
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
        turtle._update()
    final = []
    print("loading3")
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        turtle._tracer(0,0)
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
        turtle._update()
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 12000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    prev_high_index = 0
    prev_high_sum = 0
    current_index = 0
    current_high = 0
    for i in range(0, 10001):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
        if current_index == 0:
            current_high = final[0]
            prev_high_index = 0
            current_index += 1
        else:
            if final[current_index] > current_high:
                current_high = final[current_index]
                prev_high_index = current_index
                current_index += 1
    if prev_high_index == 10000:
        quit()
    else:
        wordAdd = words.index(input_words[prev_high_index])
        wordAdd = words[wordAdd]
        response = response + str(wordAdd) + " "
    temp_final = []
    for i in range(0, 100000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        temp_final.append(sum(calculaitions))
    final = []
    for i in range(1, 120000):
        calculaitions = []
        for j in temp_final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
            wieght_index += 1
        final.append(sum(calculaitions))
    temp_final = []
    for i in range(1, 50000):
        calculaitions = []
        for j in final:
            if wieght_index >= len(wieghts):
                wieghts.append(random.uniform(0.0, 1.0))
            x = float(j) * float(wieghts[wieght_index])
            calculaitions.append(x)
        temp_final.append(sum(calculaitions))
    final = []
    









while True:
    random_mem()
    populaition1 = wieghts
    random_mem()
    populaition2 = wieghts
    random_mem()
    populaition3 = wieghts
    random_mem()
    populaition4 = wieghts
    realpop = real_wieght
    random_mem()
    populaition6 = wieghts
    random_mem()
    populaition7 = wieghts
    random_mem()
    populaition8 = wieghts
    random_mem()
    populaition9 = wieghts
    random_mem()
    populaition10 = wieghts

    #run 1
    wieghts = populaition1
    inputt = input("ask the ai something")
    print("loading")
    brainstorm()
    print("loading")
    print(response)
    #run 2
    wieghts = populaition2
    brainstorm()
    print(response)
    #run 3
    wieghts = populaition3
    brainstorm()
    print(response)
    #run 4
    wieghts = populaition4
    brainstorm()
    print(response)
    #real run
    wieghts = real_wieght
    brainstorm()
    print(response)
    #run 6
    wieghts = populaition6
    brainstorm()
    print(response)
    #run 7 
    wieghts = populaition7
    brainstorm()
    print(response)
    #run 8 
    wieghts = populaition8
    brainstorm()
    print(response)
    #run 9
    wieghts = populaition9
    brainstorm()
    print(response)
    #run10
    wieghts = populaition10
    brainstorm()
    print(response)

    a = int(input("what number response whas best"))

    if a == 1:
        real_wieghts = populaition1
    elif a == 2:
        real_wieghts = populaition2
    elif a == 3:
        real_wieghts = populaition3
    elif a == 4:
        real_wieghts = populaition4
    elif a == 5:
        pass
    elif a == 6:
        real_wieghts = populaition6
    elif a == 7:
        real_wieghts = populaition7
    elif a == 8:
        real_wieghts = populaition8
    elif a == 9:
        real_wieghts = populaition9
    else:
        real_wieghts = populaition10

    file = open("wieghts.txt", "w")
    for i in real_wieghts:
        file.write(str(i) + "\n")








