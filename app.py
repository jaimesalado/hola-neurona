import streamlit as st
import pandas as pd
import joblib



from PIL import Image
image = Image.open('neurona.jpg')

st.image(image)

# titulo
st.header('¡Hola neurona!')

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])


# una neurona
with tab1:
	peso = st.slider('Selecciona el valor del peso')
	st.write('El valor del peso seleccionado es : ', peso)
	entrada = st.number_input('Introduzca el valor de la entrada')
	st.write('El valor de la entrada seleccionada es : ', entrada)
	st.button('Calcular salida de neurona', key='tab1boton1')
	st.write('Resultado: ', peso * entrada)

# dos neurona


with tab2:
	col1, col2 = st.columns(2)
	with col1:
		peso1 = st.slider('Selecciona el valor del primer peso')
		st.write('El valor del primer peso seleccionado es : ', peso1)
	with col2:
		peso2 = st.slider('Selecciona el valor del segundo peso')
		st.write('El valor del segundo peso seleccionado es : ', peso2)
	col1, col2 = st.columns(2)
	with col1:
		entrada1 = st.number_input('Introduzca el valor primera entrada')
		st.write('El valor de la primera entrada seleccionada es : ', entrada1)
	with col2:
		entrada2 = st.number_input('Introduzca el valor segunda entrada')
		st.write('El valor de la seunda entrada seleccionada es : ', entrada2)
	resultado = (entrada1 * peso1) + (entrada2 * peso2)
	st.button('Calcular salida de neurona', key='tab2boton2')
	st.write('Resultado: ', resultado)


with tab3:
	col1, col2, col3 = st.columns(3)
	with col1:
		peso1 = st.slider('Selecciona el valor del primer peso', key='tab3peso1')
		st.write('El valor del primer peso seleccionado es : ', peso1)
	with col2:
		peso2 = st.slider('Selecciona el valor del segundo peso', key='tab3peso2')
		st.write('El valor del segundo peso seleccionado es : ', peso2)
	with col3:
		peso3 = st.slider('Selecciona el valor del tercer peso', key='tab3peso3')
		st.write('El valor del tercer peso seleccionado es : ', peso3)
	col1, col2, col3 = st.columns(3)
	with col1:
		entrada1 = st.number_input('Introduzca el valor primera entrada', key='tab3entrada1')
		st.write('El valor de la primera entrada seleccionada es : ', entrada1)
	with col2:
		entrada2 = st.number_input('Introduzca el valor segunda entrada', key='tab3entrada2')
		st.write('El valor de la segunda entrada seleccionada es : ', entrada2)
	with col3:
		entrada3 = st.number_input('Introduzca el valor tercera entrada', key='tab3entrada3')
		st.write('El valor de la tercera entrada seleccionada es : ', entrada3)
	sesgo = st.number_input('Introduzca el valor del sesgo')
	st.write('El valor del sesgo seleccionado es : ', sesgo)
	resultado = (entrada1 * peso1) + (entrada2 * peso2) + (entrada3 * peso3) + sesgo
	st.button('Calcular salida de neurona', key='tab3boton3')
	st.write('Resultado: ', resultado)