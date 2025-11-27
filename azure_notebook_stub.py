# Azure Notebook Stub for ResQ-AI
# This is a simple demonstration of how the prompt workflow would be tested.

prompt = open("prompt.txt").read()

dispatcher_input = """
Industrial warehouse fire at 5000 Fulton Industrial Blvd SW.
Heavy smoke showing. 10 workers trapped inside main structure,
3 more seen in hallway near exit.
"""

print("=== INPUT ===")
print(dispatcher_input)

print("\n=== PROMPT USED ===")
print(prompt)

print("\n=== EXPECTED OUTPUT (3–5 bullet hazards) ===")
print("- Warehouse fire")
print("- Alcohol / chemical storage risk")
print("- 13 occupants involved")
print("- Heavy smoke and structural hazard")
