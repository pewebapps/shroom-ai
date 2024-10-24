import streamlit as st
import requests
from PIL import Image
import io

st.title("Shroom AI")

st.header("Upload a mushroom image to determine if it's edible or not")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert image to byte array
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')
    img_bytes = img_bytes.getvalue()

    # When the user clicks the button, send the image to the API
    if st.button("Classify"):
        # API endpoint
        api_url = "https://your-api-endpoint.com/classify"

        # Send image to API
        response = requests.post(api_url, files={"file": img_bytes})

        # Check if request was successful
        if response.status_code == 200:
            # Display the result returned from the API
            result = response.json().get("edible", None)
            if result is not None:
                if result:
                    st.success("This mushroom is edible!")
                else:
                    st.error("This mushroom is NOT edible!")
            else:
                st.warning("Could not determine if the mushroom is edible.")
        else:
            st.error("Error in API request. Please try again.")
