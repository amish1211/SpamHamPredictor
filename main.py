import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('spam_not_spam_nb_trained_model.sav', 'rb'))
vectorizer = pickle.load(open('count_vectorizer.pkl', 'rb'))


def spam_not_spam_prediction(input_text,file=False):
    if not file:
        return model.predict(vectorizer.transform(input_text))[0]
    else:
        return model.predict(vectorizer.transform(input_text))



def main():
    # Giving a title
    st.set_page_config(page_title='Spam Ham Classifier',
                       page_icon=':email:')
    st.title('spam predicted model')

    # Getting the input from the user
    inputText = st.text_input('Enter the text to be classified')
   
    # Code for Prediction
    predicted_value = ""


    # Creating a button for Prediction
    if st.button('Predict'):
        predicted_value = spam_not_spam_prediction([inputText])
    

    if predicted_value == 'ham':
        st.success("This is NOT SPAM")
    elif predicted_value == 'spam':
        st.error("This is SPAM")
    
    uploaded_file = st.file_uploader(
        "Choose a CSV file")
    
  
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file,encoding='latin-1')
        dataset = df['text']
        df['result'] = spam_not_spam_prediction(dataset,file=True)
        df.to_csv('result.csv',)
        with open('result.csv',encoding='latin-1') as f:
            st.download_button('Download CSV', f)  



if __name__ == '__main__':
    main()
