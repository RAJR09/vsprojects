class AnimalQuiz:
    def __init__(self):
        self.questions = [
            {"question": "What is the largest mammal?", "answer": "blue whale"},
            {"question": "Which animal is known as the 'king of the jungle'?", "answer": "lion"},
            {"question": "What is the only marsupial that lives in North America?", "answer": "opossum"}
        ]
        self.max_chances = 3
        self.score = 0

    def ask_question(self, question_data):
        print(question_data["question"])
        for chance in range(self.max_chances):
            user_answer = input("Your answer: ").lower()
            if user_answer == question_data["answer"]:
                print("Correct! You earned a point.")
                self.score += 1
                break
            else:
                remaining_chances = self.max_chances - (chance + 1)
                if remaining_chances > 0:
                    print(f"Incorrect! You have {remaining_chances} {'chances' if remaining_chances > 1 else 'chance'} left.")
                else:
                    print(f"Sorry, the correct answer is {question_data['answer']}.")

    def play_game(self):
        print("Welcome to the Animal Quiz Game!\n")
        for question_data in self.questions:
            self.ask_question(question_data)
            print()  

        print(f"Game Over! Your final score is: {self.score}/{len(self.questions)}")


animal_quiz_game = AnimalQuiz()
animal_quiz_game.play_game()
