def ask_question(question):
    response = input(question + " (Yes/No): ").strip().lower()
    while response not in ["yes", "no"]:
        print("Enter 'Yes' or 'No' only.")
        response = input(question + " (Yes/No): ").strip().lower()
    return response == "yes"

def collect_symptoms():
    print("Please answer the following questions about your symptoms (Yes/No):")
    symptoms = {}
    symptoms["fever"] = ask_question("Do you have a fever?")
    symptoms["cold"] = ask_question("Do you have a cold?")
    symptoms["sore_throat"] = ask_question("Do you have a sore throat?")
    symptoms["running_nose"] = ask_question("Do you have a running nose?")
    symptoms["body_ache"] = ask_question("Do you have body ache?")
    symptoms["cough"] = ask_question("Do you have a cough?")
    symptoms["fatigue"] = ask_question("Do you feel fatigue?")
    symptoms["headache"] = ask_question("Do you have a headache?")
    return symptoms

def evaluate(symptoms):
    if symptoms["fever"] and symptoms["cough"] and symptoms["fatigue"]:
        if symptoms["headache"] and symptoms["cold"]:
            return "You should visit a doctor."
        return "It is advised to see a doctor."
    elif symptoms["running_nose"] and symptoms["sore_throat"]:
        return "Take a good amount of rest."
    elif symptoms["body_ache"] and not symptoms["fever"]:
        return "Rest is necessary."
    else:
        return "Your symptoms are unidentifiable. You seem to be well."

def play():
    print("Welcome to the Flu Expert System. Let's evaluate your symptoms.")
    symptoms = collect_symptoms()
    diagnosis = evaluate(symptoms)
    print("\nDiagnosis:")
    print(diagnosis)

play()
