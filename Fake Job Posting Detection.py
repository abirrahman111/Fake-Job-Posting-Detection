# -*- coding: utf-8 -*-
"""Fake Job Posting Detection Using Machine Learning .ipynb


# IMPORT REQUIRED LIBRARIES
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd               #Allows easy large data manipulation in spreadsheet type format.
import numpy as np                #Provides array interface which is fast, efficient, compact and better suited for large scientific data calculations
import matplotlib.pyplot as plt
# %matplotlib inline                #Displays matplotlib graphs in the same window. Otherwise it would've been in separate tab or window.
import seaborn as sns             #matplotlib and seaborn for drawing the graphs

"""#  IMPORT DATASET"""

fake_jobs_df=pd.read_csv('fake_job_postings.csv')

fake_jobs_df

"""# Dataset Preprocessing

Null Values
"""

#Null values
fake_jobs_df.isnull().sum()

#Heatmap of Null values
sns.heatmap(fake_jobs_df.isnull(), yticklabels = False, cbar = False, cmap = "Blues")
plt.show()

"""Imputation"""

#Imputaion: Filling up null values with estimated values to avoid biasness
new_dataset = fake_jobs_df.fillna(method = "bfill")

new_dataset = new_dataset.fillna({
    'salary_range': '20000-28000',
    'benefits': 'Full Benefits Offered',            #Imputation
    'required_education': "Bachelor's Degree"
})

new_dataset

new_dataset.isnull().sum()

sns.heatmap(new_dataset.isnull(), yticklabels=False, cbar = False, cmap = "Blues")
plt.show()

"""Actual Count of Fraud and Fair Jobs"""

fraudulent = new_dataset[new_dataset['fraudulent'] == 1]
no_fraudulent = new_dataset[new_dataset['fraudulent'] == 0]

print('Total = ', len(new_dataset))

print('Number of fake jobs = ', len(fraudulent))
print('Percentage of fake jobs = ', 1.*len(fraudulent)/len(new_dataset)*100, '%')

print('Number of fair jobs = ', len(no_fraudulent))
print('Percentage of fair jobs = ', 1.*len(no_fraudulent)/len(new_dataset)*100, '%')

"""Dropping Columns"""

#Dropping columns with categorical values
new_dataset.drop(['title', 'location', 'department', 'salary_range','company_profile', 'description', 'requirements', 'benefits', 'employment_type', 'required_experience',
                 'required_education', 'industry', 'function'], axis=1, inplace= True)

"""Preprocessed Dataset"""

new_dataset

"""# LOGISTIC REGRESSION"""

#Let's drop the target column before we do train test split
X = new_dataset.drop('fraudulent', axis=1).values
y = new_dataset['fraudulent'].values

X.shape

type(X)

y.shape

type(y)

"""Feature Scaling"""

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

X

y.shape

type(y)

"""Dataset Spliting"""

#Dataset spliting
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""MODEL TRAINING"""

#fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

"""MODEL TESTING"""

y_predict_train = classifier.predict(X_train)

y_predict_train

y_train

from sklearn.metrics import classification_report, confusion_matrix
cm = confusion_matrix(y_train, y_predict_train)
sns.heatmap(cm, annot = True, fmt = 'd')
plt.show()

y_predict_test = classifier.predict(X_test)

y_predict_test

cm = confusion_matrix(y_test, y_predict_test)
sns.heatmap(cm, annot = True, fmt = 'd')
plt.show()

print(classification_report(y_test, y_predict_test))

"""# DECISION TREE"""

#Let's drop the target column before we do train test split
X=new_dataset.drop('has_company_logo',axis=1).values
y=new_dataset['has_company_logo'].values

X.shape

type(X)

y.shape

type(y)

"""Feature Scaling"""

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

X

"""Dataset Splitting"""

#Dataset Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""MODEL TRAINING"""

#Fitting Decision Tree to the Training dataset
from sklearn.tree import DecisionTreeClassifier
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)

"""MODEL TESTING"""

from sklearn.metrics import classification_report, confusion_matrix

y_predict_train = decision_tree.predict(X_train)

y_predict_train

cm = confusion_matrix(y_train, y_predict_train)

sns.heatmap(cm, annot = True,fmt='d')
plt.show()

y_predict_test = decision_tree.predict(X_test)

y_predict_test

cm = confusion_matrix(y_test, y_predict_test)

sns.heatmap(cm, annot=True, fmt='d')
plt.show()

print(classification_report(y_test, y_predict_test))
