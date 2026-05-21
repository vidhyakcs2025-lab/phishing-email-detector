import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_email(text):

    data = vectorizer.transform([text])

    prediction = model.predict(data)[0]

    if prediction == 1:
        return "Phishing"
    else:
        return "Safe"