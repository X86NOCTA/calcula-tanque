import streamlit as st
import math

st.set_page_config(page_title="Calculadora de Tanques Elevados", layout="centered")

st.title("CALCULADORA DE MATERIAIS PARA TANQUES ELEVADOS")
st.write("*ATENÇÃO! Utilize ponto (.) ao invés de vírgula (,)*")

# Inputs
valor_raio = st.number_input("Digite o raio do tanque (em metros)", min_value=0.0, step=0.1)
valor_altura = st.number_input("Digite a altura do tanque (em metros)", min_value=0.0, step=0.1)

if st.button("Calcular"):
    try:
        circunferencia = valor_raio * 2 * math.pi
        postes = math.ceil(circunferencia / 1.2) + 1
        cabos = circunferencia + 2
        volume = math.pi * valor_raio ** 2 * valor_altura
        fiadas = 6 if volume < 100 else 7
        tela = cabos
        diametro = valor_raio * 2
        grampos = fiadas * 4
        esticadores = fiadas
        baby = tela

        # Exibir resultados
        st.subheader("Resultados:")
        st.write(f"Circunferência: {circunferencia:.2f} m")
        st.write(f"Quantidade de Postes: {postes} un")
        st.write(f"Comprimento de Cabos: {cabos:.2f} m")
        st.write(f"Volume do Tanque: {volume:.2f} m³")
        st.write(f"Número de Fiadas: {fiadas}")
        st.write(f"Tela Morlan: {tela:.2f} m")
        st.write(f"Diâmetro do Tanque: {diametro:.2f} m")
        st.write(f"Número de Grampos: {grampos} un")
        st.write(f"Número de Esticadores: {esticadores} un")
        st.write(f"Baby Preto: {baby:.2f} m")

    except Exception as e:
        st.error("Ocorreu um erro. Verifique os valores digitados.")
        st.error(str(e))

st.markdown("---")
st.markdown("© 2025 Brasil Piscis   -   Developed by Matheus Tartaglia")
