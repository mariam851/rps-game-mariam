# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random 
class PRS_AI:
    def __init__(self):
        self.history = []
        self.patterns = {}

    def record_move(self, oppenent_move):
        self.history.append(oppenent_move)
        if len(self.history) >= 2:
            prev_move = self.history[-2]
            current_move = self.history[-1]
            if prev_move not in self.patterns:
                self.patterns[prev_move] = {}
            if current_move not in self.patterns[prev_move]:
                self.patterns[prev_move][current_move] = 0 
            self.patterns[prev_move][current_move] += 1

    def predict_move(self):
        if len(self.history) == 0:
            return random.choice(["rock", "paper", "scissors"])
        
        last_move = self.history[-1]
        if last_move in self.patterns:
            possibel_next_moves = self.patterns[last_move]
            if possibel_next_moves:
                predicted_oppenent_move = max(possibel_next_moves, key=possibel_next_moves.get)
                if possibel_next_moves == "rock":
                    return "paper"
                elif predicted_oppenent_move == "paper":
                    return "scissors"
                else:
                    return "rock"
                
        return random.choice(["rock", "paper", "scissors"])
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It is a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice=="rock") or (player_choice=="scissors" and computer_choice=="paper"):
        return "You win!"
    else:
        return "computer wins!"
    

ai_player = PRS_AI()
choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissors) or quit: ").lower()
    if user_choice == 'quit':
        break
    if user_choice not in choices:
        print('Inavalid choice. Please choose rock, paper, scissors')
        continue

    computer_choice = ai_player.predict_move()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    ai_player.record_move(user_choice)


            

        
        
    

    






    
