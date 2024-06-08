import requests
import html

# Fetch the quiz data
response = requests.get("https://opentdb.com/api.php?amount=10&category=32&type=boolean")

if response.status_code == 200:
    quiz_data = response.json()["results"]
    length = len(quiz_data)
    score = 0

    # Iterate through each question
    for i in range(length):
        question = html.unescape(quiz_data[i]["question"])
        correct_answer = quiz_data[i]["correct_answer"]

        print(f"{i + 1}) {question}")
        user_answer = input("True or False: ").capitalize()

        if user_answer == correct_answer:
            print("Correct\n")
            score += 1
        else:
            print("Incorrect\n")

    # Print the final score
    print(f"You scored {score} out of {length}")
else:
    print("An error has occurred")



# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments

