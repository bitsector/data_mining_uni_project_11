import argparse
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.tree import export_graphviz
import pydotplus
from six import StringIO
from datetime import datetime

def visualise(clf, X, criterion):
    # Create DOT data
    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data, 
                    filled=True, rounded=True, special_characters=True, 
                    feature_names=list(X.columns), class_names=['0', '1'])

    # Draw graph
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  

    # Generate timestamp
    timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    # Save graph to a file with the criterion and timestamp in the filename
    filename = f"decision_tree_{criterion}_{timestamp}.png"
    graph.write_png(filename)
    print(f"The decision tree graph has been saved as '{filename}'")

# Set up argument parsing
parser = argparse.ArgumentParser(description='Train a decision tree classifier.')
parser.add_argument('-i', '--input', type=str, required=True, help='Path to the CSV file containing the data.')
parser.add_argument('-c', '--criterion', type=str, choices=['gini', 'entropy'], default='gini',
                    help='Criterion for the decision tree: "gini" or "entropy" (default: "gini").')
parser.add_argument('-v', '--visualise', action='store_true', help='Visualise the decision tree graphically.')
args = parser.parse_args()

# Load the data
data = pd.read_csv(args.input)

# Separate the target variable and features
y = data['COPD']  # Directly use the target column
X = data.drop(columns=['COPD'])  # Drop the target column from the feature set

# One-hot encode the categorical variables of the feature set
X_encoded = pd.get_dummies(X)

# Initialize and train the DecisionTreeClassifier with the specified criterion
clf = DecisionTreeClassifier(criterion=args.criterion)
clf.fit(X_encoded, y)

# Generate the textual representation
tree_rules = export_text(clf, feature_names=list(X_encoded.columns))
print(tree_rules)

# Visualise the decision tree if the visualise flag is set
if args.visualise:
    visualise(clf, X_encoded, args.criterion)