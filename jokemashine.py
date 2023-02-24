import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the chicken cross the playground? To get to the other slide!",
    "Why don't dinosaurs drive cars? Because they're extinct!",
    "Why did the hipster burn his tongue? He drank his coffee before it was cool."
]

print("Welcome to the joke machine! Press enter to hear a joke, or type 'q' to quit.")

while True:
    input_str = input()
    if input_str.lower() == "q":
        break
    else:
        print(random.choice(jokes))
