import streamlit as st
import math

st.set_page_config(page_title="CALCULADORA DE TANQUES ELEVADOS", layout="centered")
st.title("CALCULADORA DE MATERIAIS PARA TANQUES ELEVADOS")

# Frase de instrução
st.markdown("*ATENÇÃO! Utilize ponto (.) ao invés de vírgula (,)*")

# Inputs
diametro = st.number_input("Digite o diâmetro do tanque (em metros)", min_value=0.0, step=0.1)
altura = st.number_input("Digite a altura do tanque (em metros)", min_value=0.0, step=0.1)

tipo_pvc = st.selectbox(
    "Escolha o tipo de PVC",
    ["PVC TRANÇADO CINZA 0,8MM", "PVC PURO/LISO 1MM", "PVC TRANÇADO AZUL 0,9MM"]
)

pesos = {
    "PVC TRANÇADO CINZA 0,8MM": 0.7,
    "PVC PURO/LISO 1MM": 1.1,
    "PVC TRANÇADO AZUL 0,9MM": 1.3
}

# Botão de calcular
if st.button("Calcular"):
    try:
        raio = diametro / 2
        circunferencia = 2 * math.pi * raio
        postes = math.ceil(circunferencia / 1.2) + 1
        cabos = circunferencia + 2 
        volume = math.pi * raio**2 * altura
        fiadas = 6 if volume < 100 else 7
        tela = cabos
        grampos = fiadas * 4
        esticadores = fiadas
        baby = tela
        metragem_quadrada_parede = circunferencia * (altura + 0.3)
        metragem_quadrada_fundo = math.pi * raio**2
        metragem_quadrada_total = metragem_quadrada_parede + metragem_quadrada_fundo

        peso_especifico = pesos[tipo_pvc]
        peso_bolsa = peso_especifico * metragem_quadrada_total

        # Resultados
        st.subheader("Resultados:")
        st.write(f"Circunferência: {circunferencia:.2f} m")
        st.write(f"Quantidade de Postes: {postes} un")
        st.write(f"Comprimento de Cabos: {cabos:.2f} m")
        st.write(f"Volume do Tanque: {volume:.2f} m³")
        st.write(f"Número de Fiadas: {fiadas}")
        st.write(f"Tela Morlan: {tela:.2f} m")
        st.write(f"Raio do Tanque: {raio:.2f} m")
        st.write(f"Número de Grampos: {grampos} un")
        st.write(f"Número de Esticadores: {esticadores} un")
        st.write(f"Baby Preto: {baby:.2f} m")
        st.write(f"Metragem Quadrada Total: {metragem_quadrada_total:.2f} m²")
        st.write(f"Peso do Bolsão: {peso_bolsa:.2f} kg")

    except ValueError:
        st.error("Por favor, digite um número válido.")

# Rodapé
st.markdown("---")
st.markdown("© 2025 Brasil Piscis - Developed by Matheus Tartalha")
