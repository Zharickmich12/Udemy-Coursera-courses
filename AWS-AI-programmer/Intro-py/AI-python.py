# PYTHON FOR AI PROGRAMMING

"""
WHAT IS AI PROGRAMMING?
AI programming = creating systems capable of performing tasks that normally require human intelligence.

Typical tasks:
    - understanding natural language
    - recognizing patterns
    - making decisions
    - learning from data
    - making predictions

Building algorithms that learn from data and produce classifications, decisions, or predictions.
"""

"""
WHY IS PYTHON USED IN AI?
Python is widely used in AI because:
    - it has simple syntax
    - it is easy to read
    - it is suitable for both beginners and experts
    - it has many specialized libraries

Important libraries:
    - TensorFlow
    - PyTorch
    - scikit-learn

Python makes it easier to write, understand, and maintain programs related to machine learning and deep learning.
"""

"""
IMPORTANT PYTHON FUNDAMENTALS FOR AI

DATA TYPES AND OPERATORS
Data types allow information to be represented. In AI, they are important for storing data, labels, and results.

Types:
    - list
    - dictionary
    - tuple

Conceptual example:
A dictionary can associate a file with its label.
"""

file_to_label = {
    "dog_001.jpg": "beagle",
    "dog_002.jpg": "poodle",
}

"""
key   -> file name / identifier
value -> label / classification
"""

"""
DATA STRUCTURES
Data structures help store and organize large amounts of information efficiently.

Key structures:
    - lists
    - dictionaries
    - sets

Uses in AI:
    - storing datasets
    - storing labels
    - recording classifications
    - comparing results
    - performing fast searches
"""

images = ["dog_001.jpg", "dog_002.jpg", "dog_003.jpg"]   # list
labels = {"dog_001.jpg": "beagle"}                       # dictionary
unique_breeds = {"beagle", "poodle", "husky"}             # set

# Dictionaries are especially useful when a data item needs to be mapped to its result or label.


"""
CONTROL FLOW
Control flow = mechanisms that control how a program executes.

Main elements:
    - loops
    - conditionals

In AI, they are used to:
    - iterate through data
    - process elements one by one
    - check results
    - make decisions based on conditions
"""

classifications = {
    "dog_001.jpg": "beagle",
    "dog_002.jpg": "poodle",
}

for file, breed in classifications.items():
    if breed == "beagle":
        pass
        # A specific action could be performed here

# Loops allow many data items to be processed.
# Conditionals allow decisions to be made based on the result.


"""
FUNCTIONS
A function encapsulates a specific task.

Advantages:
    - reusability
    - modularity
    - organization
    - easier maintenance

In AI, functions can be responsible for:
    - reading files
    - processing data
    - applying classification
    - evaluating results
"""


def example_processing_function(data):
    # A function receives data and returns a processed result.
    return data


# Breaking a large problem into smaller functions makes the system clearer and easier to maintain.


"""
OBJECT-ORIENTED PROGRAMMING (OOP)
OOP organizes code using:
    - classes
    - objects

It is useful for:
    - structuring complex systems
    - grouping related data and behavior
    - making code more maintainable

In AI, it can be used to represent:
    - models
    - preprocessing components
    - parts of a pipeline
"""


class AIModel:
    def __init__(self, name):
        self.name = name


# OOP is helpful when a project grows and requires better organization.


"""
SCRIPTING
Scripting = writing programs to automate tasks.

In AI, it is used to:
    - prepare data pipelines
    - automate training
    - automate evaluation
    - manage experiments

Conceptual example:
A script can execute several tasks in sequence:
    1. load data
    2. process it
    3. classify it
    4. measure results
"""