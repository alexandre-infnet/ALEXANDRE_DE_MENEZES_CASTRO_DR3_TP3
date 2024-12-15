import streamlit as st
from agents.tourism_agent import agent


st.title("Assistente de Turismo - New York")
st.subheader("Ferramentas disponíveis")
st.write("- **Consulta Clima**: Verifica o clima em qualquer cidade.")
st.write("- **Busca Restaurantes**: Busca restaurantes próximos em New York.")

user_input = st.text_input("Digite sua pergunta ou solicitação:")

if st.button("Enviar"):
    if user_input.strip():
        with st.spinner("Processando..."):
            response = agent.run(user_input)
        st.write(f"Resposta: {response}")
    else:
        st.warning("Por favor, insira uma pergunta ou solicitação.")
