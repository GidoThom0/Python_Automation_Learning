import random, time

correctNum = 0
for i in range(10):
    retries = 0
    tooManyRetries = False
    start_time = time.time()
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    timesUp = False

    while not tooManyRetries: 

        if retries >= 3:
            print('Too many retries!')
            tooManyRetries = True
            break

        answer = input(str(number1) + ' x ' + str(number2) + '= ')

        try:
            intAnswer = int(answer)
        except ValueError:
            print('Please input a positive integer.')
            retries += 1
            continue

        # Check if the answer is correct
        if intAnswer == number1 * number2:
            if time.time() - start_time < 8:  # Check if time has not run out
                correctNum += 1
                print('Correct!')
                break  # Exit the while loop after a correct answer
            else:  # Times up scenario
                print('Times up!') 
                break  # Exit the while loop if time runs out
        else:
            print('Wrong.')
            retries += 1

print('Your score is ' + str(correctNum) + '/10')