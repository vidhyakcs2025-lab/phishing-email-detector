from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

emails = [
    "Your bank account is suspended click here",
    "Win a free iPhone now",
    "Update your password immediately",
    "Meeting scheduled tomorrow",
    "Project report attached",
    "Lunch at 1 PM",
]

labels = [1, 1, 1, 0, 0, 0]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully")