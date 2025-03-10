from pathlib import Path
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 
    'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 
    'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 
    'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
    'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

for quizNum in range(35):
    # Define directory and ensure it exists
    quizDirectory = Path('../TextFiles/RandomQuizzes')
    quizDirectory.mkdir(parents=True, exist_ok=True)

    # Set files Paths
    quizFilePath = Path(quizDirectory, 'quiz' + str(quizNum+1))    
    answerKeyFilePath = Path(quizDirectory, 'answers' + str(quizNum+1))

     # Open quiz and answer key files using 'with' to handle closing properly
    with open(quizFilePath, 'w') as quizFile, open(answerKeyFilePath, 'w') as answerKeyFile:
        # Write quiz header
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})\n\n')

        # Shuffle the order of the states
        states = list(capitals.keys())
        random.shuffle(states)

        for questionNum in range(50):
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            wrongAnswers.remove(correctAnswer)
            wrongAnswers = random.sample(wrongAnswers, 3)  # Select 3 incorrect answers
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)  # Shuffle answer choices

            # Write the question
            quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')

            # Write the multiple-choice options
            for i in range(4):
                quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n")
            quizFile.write('\n')

            # Write the correct answer to the answer key
            answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")

print("35 quiz files and answer keys have been successfully created!")
        
        

        






