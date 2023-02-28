# import packages.data_processor as dp
import streamlit as st 
import joblib

# Load the model
spam_clf = joblib.load(open('./model/model.pkl','rb'))


### MAIN FUNCTION ###
def main(title = "Text classification App".upper()):
    st.markdown("<h1 style='text-align: center; font-size: 65px; color: #4682B4;'>{}</h1>".format(title), 
    unsafe_allow_html=True)
    st.image("./images/spam_image.jpeg")
    info = ''
    

    text_message = st.text_input("ENTER YOUR MESSAGE TO CHECK IF IT IS SPAM")
    if st.button("Predict"):
        prediction = spam_clf.predict([text_message])
        

        if(prediction[0] == 0):
            info = 'Ham'

        else:
            info = 'Spam'
        st.success('Prediction: {}'.format(info))
            
if __name__ == "__main__":
    main("TEXT CLASSIFICATION APP - v2")