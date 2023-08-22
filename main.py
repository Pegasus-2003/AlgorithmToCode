import streamlit as st
import requests

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=64c10025d15e6b31ea77ea72&org=d6e96cdf-6762-4a24-a895-cf391227484c"
headers = {
    'Authorization':'Bearer dfaa5eed-a090-4f62-87bd-3aadda211a18',
    'Content-Type': 'application/json'
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def main():
    st.set_page_config(page_title="Code Generator", page_icon=":tada:", layout="wide")
    st.subheader("Convert Your Algorithm to Code")
    st.write("Please Enter your Algorithm Below")
    user_question = st.text_input("ALGORITHM HERE")
    if(user_question):
        with st.spinner("Processing"):
            print("processing")
            payload={
                "in-0":user_question
            }
            response1 = query(payload)
            st.write(response1['out-0'])

if __name__ == '__main__':
    main()



