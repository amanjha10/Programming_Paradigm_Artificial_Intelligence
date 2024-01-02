import random

# Greet the user with a friendly message
print("Hello! I'm here to assist you with your ailments.")

# Present a clear menu of available remedies
print("\nAvailable Remedies:")
print("- Digestive discomfort (पेट दुख्यो)")
print("- Hand injury (हात चिलियो)")
print("- Headache (टाउको दुख्यो)")
print("- Foot pain (खुट्टा दुख्यो)")


ailments = []

# Allow the user to select multiple remedies
while True:
    ailment = input("\nPlease select a remedy from the list above (or type 'done' to finish): ")
    if ailment.lower() == "done":
        break
    ailments.append(ailment)

# Construct a dictionary for ailments and their corresponding remedies
remedies = {
    "पेट दुख्यो": "Drink ginger tea or eat a light meal.",
    "हात चिलियो": "Apply a cold compress and elevate your hand.",
    "टाउको दुख्यो": "Rest in a dark, quiet room and consider taking pain relievers.",
    "खुट्टा दुख्यो": "Soak your feet in warm water and massage them gently."
}

# Provide personalized advice for each chosen ailment
for ailment in ailments:
    if ailment in remedies:
        print(f"\nFor {ailment}, try this: {remedies[ailment]}")
    else:
        print(f"\nSorry, I don't have a remedy for {ailment} yet.")

# Offer additional tips for general well-being
print("\nAdditional tips for overall health:")
print("- Get enough sleep.")
print("- Stay hydrated.")
print("- Eat a balanced diet.")
print("- Exercise regularly.")
print("- Manage stress.")

# Encourage further exploration
print("\nI hope these remedies help you feel better! If you have any other concerns, please consult a healthcare professional.")

# Offer a fun fact for a personalized touch
random_fact = random.choice([
    "Did you know that laughter can boost your immune system?",
    "Studies show that spending time in nature can reduce stress and improve mental health.",
    "Hydration is essential for every function in your body, so drink up!",
    "Even a short walk can make a difference in your physical and mental well-being."
])
print(f"\n{random_fact}")
