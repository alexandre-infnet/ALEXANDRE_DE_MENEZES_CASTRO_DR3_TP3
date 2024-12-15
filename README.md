Assistente de Turismo - New York

Descrição do Problema e da Solução

Problema

Ao planejar uma viagem ou passeios em New York, turistas enfrentam desafios como:
	•	A dificuldade de encontrar informações rápidas sobre o clima para planejar suas atividades.
	•	Identificar restaurantes próximos com rapidez e eficiência.
	•	Consolidar informações relevantes em um único local, evitando a navegação entre múltiplos aplicativos ou sites.

A necessidade de realizar essas consultas manualmente pode ser frustrante e demorada, especialmente para quem está em uma cidade nova.

Solução

Este Assistente de Turismo para New York foi criado para resolver esses problemas, integrando funcionalidades de consulta climática e busca de restaurantes em uma interface única e amigável. O agente utiliza um modelo de linguagem baseado em inteligência artificial para interagir de maneira natural e responsiva com os usuários, fornecendo:
	•	Informações detalhadas sobre o clima em qualquer cidade.
	•	Recomendações de restaurantes próximos, com localização em New York.
	•	Suporte contextual, lembrando interações anteriores para oferecer respostas mais completas.

Essa solução reduz o tempo gasto em buscas manuais, melhora a experiência do usuário e consolida informações em um único lugar.

Casos de Uso Testados e Resultados Observados

1. Consulta do Clima

Pergunta: “Qual é o clima em New York?”
Resultado Observado:
O agente retornou uma resposta detalhada sobre as condições climáticas atuais, incluindo:
	•	Descrição do tempo (ensolarado, nublado, etc.).
	•	Temperatura atual e sensação térmica.
	•	Velocidade do vento e outras informações relevantes.

Resposta Exemplo:

	O clima em New York, New York (Estados Unidos) é ensolarado, com temperatura de 25°C (sensação térmica de 27°C) e vento a 10 km/h.

2. Busca de Restaurantes em New York

Pergunta: “Quais restaurantes estão disponíveis dentro de 500 metros?”
Resultado Observado:
O agente listou até cinco restaurantes próximos na área central de New York, incluindo seus nomes e coordenadas aproximadas.

Resposta Exemplo:

	Restaurantes em New York encontrados:
    •	Joe’s Pizza (Localização: 40.73061, -73.935242)
	•	Shake Shack (Localização: 40.741895, -73.989308)
	•	Nome não disponível (Localização: 40.730901, -73.987654)

1.	Pré-requisitos
•	Python 3.7 ou superior instalado.
•	Biblioteca Streamlit instalada:

pip install streamlit


•	Outras bibliotecas necessárias:
langchain
openai
langchain_community
streamlit

2.	Configuração das Chaves de API
•	Substitua as variáveis no código pelo valor das suas chaves de API:
•	OPENAI_API_KEY: Chave da API OpenAI para o modelo GPT.
•	API_KEY_WEATHER: Chave da API WeatherAPI para consulta climática.

3.	Executar o Aplicativo
•	Salve o código em um arquivo chamado src/app.py.
•	Execute o seguinte comando no terminal:

•	O aplicativo será iniciado e estará disponível no navegador, geralmente em http://localhost:8501.

4.	Uso da Interface
•	Insira perguntas ou solicitações no campo de entrada, como “Qual é o clima em New York?”.
•	Clique no botão Enviar para obter a resposta do agente.
•	Use a barra lateral para consultar as ferramentas disponíveis.

Reflexão: Como o Agente Facilitou o Trabalho

Abordagem Manual

Antes deste agente, seria necessário:
	•	Acessar sites específicos para obter informações sobre o clima, como o WeatherAPI ou similares.
	•	Realizar buscas em ferramentas de mapas ou diretórios para identificar restaurantes próximos.
	•	Consolidar essas informações manualmente para tomar decisões, o que é demorado e fragmentado.

Com o Agente

O agente integrou todas essas funcionalidades em uma única interface:
	•	Responde perguntas em linguagem natural, eliminando a necessidade de navegação em diferentes sites.
	•	Fornece respostas contextualizadas, considerando o histórico da conversa.
	•	Reduziu significativamente o tempo necessário para obter informações.


Benefícios Observados
	•	Eficiência: Consultas rápidas e consolidadas em um único local.
	•	Personalização: Respostas contextualizadas baseadas em interações anteriores.
	•	Experiência do Usuário: Interface intuitiva que elimina o uso de múltiplos aplicativos.

Essa automação não apenas simplificou o processo, mas também melhorou a experiência do usuário ao oferecer informações de maneira integrada e eficiente.


Contribuições e Melhorias Futuras

Contribuições
	•	Um assistente funcional para planejamento de atividades em New York.
	•	Suporte a perguntas contextuais e personalizadas.

Melhorias Futuras
	•	Expandir a busca de restaurantes para outras cidades e permitir filtros (cozinha, preço, etc.).
	•	Adicionar recomendações de atividades turísticas baseadas no clima.
	•	Melhorar a interface do usuário com opções visuais para selecionar ferramentas específicas.