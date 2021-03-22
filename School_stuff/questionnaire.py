questions = [
    "Is the project broken down into work packages and Tasks? ",
    "Is the structure defined? ",
    "Has The work packages and the tasks been assigned in the project structure plan? ",
    "Has the tasks and work packages been coded? ",
    "Has the completeness been checked? "
]

question_answer = {}


def questionnaireFunc(q_list, q_a_list):
    print("Answer the questions with yes or no.")
    for i in q_list:
        answer = input(i).lower()
        #assaining list item as key and item input as value
        q_a_list[i] = answer


questionnaireFunc(questions, question_answer)


def checkAnswers(q_a_list):
    if any("no" in value for value in q_a_list.items()):
        print(
            "For the following questions, work steps are apparently still pending in the planning:"
        )
        for key, value in q_a_list.items():
            if "no" == value:
                print(key)

    elif all("yes" in value for value in q_a_list.items()):
        print(
            "You have done a good job and can continue with the timing as planned."
        )


checkAnswers(question_answer)
