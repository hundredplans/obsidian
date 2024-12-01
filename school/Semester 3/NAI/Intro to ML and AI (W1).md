# Terms
Chinese Room -> A computer executing a program cannot have a mind or conciousness
Eliza Effect -> Tendency to project human traits onto inanimate objects
# Types of AI
Weak / Narrow AI (Slaba) -> Only narrow aspects of intelligence like chess bots
Strong AI (Silna) -> Acts in an intelligent manner but doesn't have a mind
Artifical General Intelligence -> Equal intelligence or slightly greater than a human
Artifical Superintelligence (ASI) -> Smarter than a human
# Definitions of AI
- Teaching a machine similar behaviours to a human
- Teaching a machine to do things that humans do better
# Machine Learning

## Supervised
- Regression -> User creates a graph based on an input and dependant (control) then model predicts the value, used for numeric values (SUPERVISED)
- Classification -> User categorizes objects / data into predefined classes then model predicts the class for new inputs, used for categories such as predicting if email is spam (SUPERVISED)

Decision tress are used for the two algorithms above
# Unsupervised
- Clustering -> Forms groups of data based on an algorithm provided, used for advertising (UNSUPERVISED)
- Association -> Counts frequency of unusual things that appear often using an algorithm (UNSUPERVISED)

# Confusion Matrix
(True | False) (Positive | Negative)
![[confusion_matrix.png]]


Precision -> The quality of a positive prediction
Negative Predictive Value -> The quality of a negative prediction
Sensitivity -> True positive rate
Specifity -> True negative rate
Accuracy -> How many predictions it makes correct
# Decision Tree
Data is recursively split by an algorithm into nodes, based on attributes (GI & IG) until either a maximum depth is reached or a minimum number of leaf nodes

Leaf Node -> A node with no more children, at the very end of a branch

Gini Impurity (GI) -> Probability that a split will incorrectly classify the data
Information Gain (IG) -> How effective an attribute is at splitting the data

Each node can have a function associated with it that decides whether to go left or right

GI and IG are used for attribute selection (choosing what function to put on a node)