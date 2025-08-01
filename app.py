import streamlit as st
import numpy as np
from prediction import predict

st.title('Classifying Iris Flowers')
st.markdown('Toy model to classify iris flowers into \
     (setosa, versicolor, virginica) based on their sepal/petal \
    length/width.')

st.header("Plant Features")
col1, col2 = st.columns(2)

with col1:
    st.text("Sepal characteristics")
    sepal_l = st.slider('Sepal length (cm)', 1.0, 8.0, 5.0, step=0.1)
    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 3.0, step=0.1)

with col2:
    st.text("Petal characteristics")
    petal_l = st.slider('Petal length (cm)', 1.0, 7.0, 4.0, step=0.1)
    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 1.2, step=0.1)

st.text('')
if st.button("Predict type of Iris"):
    result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
    st.success(f'Predicted Iris class: {result[0]}')

    if result[0] == 'Iris-setosa':
        st.image('pic1.jpg')
    elif result[0] == 'Iris-versicolor':
        st.image('pic2.jpg')
    elif result[0] == 'Iris-virginica':
        st.image('pic3.jpg')

st.text('')
st.text('')
st.markdown('`CREATED BY` [PRATIBHA]')
