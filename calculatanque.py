import customtkinter as ctk
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CALCULADORA DE TANQUES ELEVADOS")
app.geometry("500x850")

# Função para subir suavemente a instrução
def subir_instrucao(step=5):
    # Pega o padding atual do label
    pady_atual = instrucao_label.pack_info()["pady"]
    if isinstance(pady_atual, tuple):
        pady_atual = pady_atual[0]

    if pady_atual > 0:
        # Diminui o padding aos poucos
        instrucao_label.pack_configure(pady=pady_atual - step)
        app.after(20, lambda: subir_instrucao(step))
    else:
        # Quando chegar no topo, esconde o label
        instrucao_label.pack_forget()

def calcular():
    try:
        # Inicia a animação de subir o label
        subir_instrucao()

        valor_raio = float(entrada.get())
        valor_altura = float(altura.get())
        circunferencia = valor_raio * 2 * 3.1415
        postes = math.ceil(circunferencia / 1.2) + 1
        cabos = circunferencia + 2 
        volume = 3.1415 * valor_raio ** 2 * valor_altura 
        if volume < 100:
            fiadas = 6 
        else:
            fiadas = 7 
        tela = cabos
        diametro = valor_raio * 2
        grampos = fiadas * 4 
        esticadores = fiadas 
        baby = tela

        resposta_label.configure(text=f"Circunferência: {circunferencia:.2f} m")
        resposta_label1.configure(text=f"Quantidade de Postes: {postes} un")
        resposta_label2.configure(text=f"Comprimento de Cabos: {cabos:.2f} m")
        resposta_label3.configure(text=f"Volume do Tanque: {volume:.2f} m³")
        resposta_label4.configure(text=f"Número de Fiadas: {fiadas}")
        resposta_label5.configure(text=f"Tela Morlan: {tela:.2f} m")
        resposta_label6.configure(text=f"Diâmetro do Tanque: {diametro:.2f} m")
        resposta_label7.configure(text=f"Número de Grampos: {grampos} un")
        resposta_label8.configure(text=f"Número de Esticadores: {esticadores} un")
        resposta_label9.configure(text=f"Baby Preto: {baby:.2f} m")

    except ValueError:
        resposta_label.configure(text="Por favor, digite um número válido.")
        resposta_label1.configure(text="")

# Cabeçalho
frase_label = ctk.CTkLabel(app, text="CALCULADORA DE MATERIAIS PARA TANQUES ELEVADOS", font=("Comic Sans", 14, "bold"))
frase_label.pack(pady=30, padx=40)

# Entry para raio
entrada = ctk.CTkEntry(
    app,
    placeholder_text="Digite o raio do tanque (em metros)",
    width=310,
    height=40,
    font=("Arial", 16)
)
entrada.pack(pady=20)

# Entry para altura
altura = ctk.CTkEntry(
    app,
    placeholder_text="Digite a altura do tanque (em metros)",
    width=310,
    height=40,
    font=("Arial", 16)
)
altura.pack(pady=20)

# Botão de calcular
botao = ctk.CTkButton(app, text="Calcular", command=calcular)
botao.pack(pady=10)

# Frase de instrução (vai subir suavemente ao clicar)
instrucao_label = ctk.CTkLabel(app, text="*ATENÇÃO!   Utilize ponto (.) ao invés de vírgula (,)", font=("Arial", 14))
instrucao_label.pack(pady=10)

# Labels de resposta
resposta_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label.pack(pady=7)
resposta_label1 = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label1.pack(pady=7)
resposta_label2 = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label2.pack(pady=7)
resposta_label3 = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label3.pack(pady=7)
resposta_label4 = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label4.pack(pady=7)
resposta_label5 = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label5.pack(pady=7)
resposta_label6 = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label6.pack(pady=7)
resposta_label7 = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label7.pack(pady=7)
resposta_label8 = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label8.pack(pady=7)
resposta_label9 = ctk.CTkLabel(app, text="", font=("Arial", 16))
resposta_label9.pack(pady=7)

# Rodapé fixo
rodape_label = ctk.CTkLabel(app, text="© 2025 Brasil Piscis   -   Developed by Matheus Tartalha", font=("Arial", 12))
rodape_label.pack(side="bottom", pady=10)

app.mainloop()
