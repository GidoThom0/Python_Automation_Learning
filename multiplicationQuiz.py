import pyinputplus as pyip, random, time

correctAnswers = 0
for questionNumber in range(10):
    num1 = random.int(0, 9)
    num2 = random.int(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # Brief pause to let user see the result.

print('Score: %s / 10' % correctAnswers)