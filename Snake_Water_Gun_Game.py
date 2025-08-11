import random

OPTIONS = ["snake", "water", "gun"]
SHORTCUTS = {"s": "snake", "w": "water", "g": "gun"}


def decide_round(user, comp):
    if user == comp:
        return "tie"
    wins = {("snake", "water"), ("water", "gun"), ("gun", "snake")}
    if (user, comp) in wins:
        return "user"
    else:
        return "comp"


def get_user_choice():
    prompt = "Choose (snake/s or water/w or gun/g) or 'q' to quit: "
    while True:
        raw = input(prompt).strip().lower()
        if raw == "q":
            return "q"
        if raw in SHORTCUTS:
            return SHORTCUTS[raw]
        if raw in OPTIONS:
            return raw
        print("Invalid input — try again (snake/s, water/w, gun/g or q).")


def play_round(round_no):
    print(f"\n--- Round {round_no} ---")
    user = get_user_choice()
    if user == "q":
        return None, None
    comp = random.choice(OPTIONS)
    print(f"You chose:  {user}")
    print(f"Computer chose: {comp}")
    result = decide_round(user, comp)
    if result == "tie":
        print("Result: It's a tie!")
    elif result == "user":
        print("Result: You win this round!")
    else:
        print("Result: Computer wins this round.")
    return result, (user, comp)


def main():
    print("Welcome to Snake, Water, Gun!")
    rounds_input = input("Rounds (leave blank for infinite / manual quit): ").strip()
    rounds = None
    if rounds_input:
        try:
            rounds = int(rounds_input)
            if rounds <= 0:
                print("Rounds should be positive. Starting infinite mode instead.")
                rounds = None
        except ValueError:
            print("Couldn't parse rounds. Starting infinite mode instead.")
            rounds = None

    
    user_score = 0
    comp_score = 0
    ties = 0
    round_no = 1

    
    while True:
        if rounds is not None and round_no > rounds:
            break
        result, _ = play_round(round_no)
        if result is None:
            print("\nYou chose to quit the game.")
            break
        if result == "user":
            user_score += 1
        elif result == "comp":
            comp_score += 1
        else:
            ties += 1
        round_no += 1

    
    played = (round_no - 1) if rounds is None else min(round_no - 1, rounds)
    print("\n=== Game Over ===")
    print(f"Rounds played: {played}")
    print(f"You: {user_score} | Computer: {comp_score} | Ties: {ties}")
    if user_score > comp_score:
        print("Overall: You won the game!")
    elif comp_score > user_score:
        print("Overall: Computer won the game. Better luck next time!")
    else:
        print("Overall: It's a tie overall!")


if __name__ == "__main__":
    main()
