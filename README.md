# Spam Ham Classifier

This is a simple web application that predicts if a given text is spam or not spam (ham). It uses a Naive Bayes model that has been trained on a dataset of spam and not spam (ham) messages.

## Dependencies

- Python 3.x
- streamlit
- pandas
- pickle

## Getting Started

To use this application, you first need to install the required dependencies by running:

```sh
pip install streamlit pandas pickle
```

After installing the dependencies, you can run the application by running the following command:

```sh
streamlit run main.py
```

## Usage

The application has two modes of input, text input and file upload.

### Text Input

To classify a text input, type in the text in the text box provided and click on the "Predict" button. The application will then display the predicted label for the input text.

### File Upload

To classify a CSV file containing a column of text to be classified, click on the "Choose a CSV file" button and select the CSV file. The application will then display a button to download a CSV file containing the predicted labels for the text in the uploaded file.

## Files

- `main.py`: The main Python script containing the web application.
- `spam_not_spam_nb_trained_model.sav`: The trained Naive Bayes model.
- `count_vectorizer.pkl`: The trained count vectorizer.
- `result.csv`: The result file containing the predicted labels for the uploaded file.
