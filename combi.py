import itertools

ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

# Generate all combinations
combinations = list(itertools.product(ageList, genderList))

# Create a dictionary to store the mappings
combination_mapping = {}

# Populate the dictionary with mappings
for i, combination in enumerate(combinations, start=1):
    combination_mapping[i] = combination

# Print the combination mapping
for key, value in combination_mapping.items():
    print(f"{key}: {value}")
