import json

def load_knowledge_base(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def diagnose_car(knowledge_base):
    print("Car Diagnosis Expert System\n")
    print("Please answer the following questions with 'yes' or 'no'.\n")

    for rule in knowledge_base['rules']:
        if input(rule['question']).strip().lower() == "yes":
            for condition in rule['conditions']:
                if input(condition['question']).strip().lower() == condition['expected_answer']:
                    print(f"Problem: {condition['problem']} Solution: {condition['solution']}")
                    return
            print(rule['default_solution'])
            return
    print("Problem not identified. It is recommended to visit a mechanic.")

# Load knowledge base
knowledge_base = load_knowledge_base('knowledge_base.json')

# Run the expert system
diagnose_car(knowledge_base)
