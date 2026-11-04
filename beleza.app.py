import streamlit as st

# ------------------- CONFIGURAÇÕES -------------------
st.set_page_config(
    page_title="Beleza da Natureza",
    page_icon="🌿",
    layout="wide"
)

# ------------------- ESTILO VISUAL -------------------
st.markdown("""
<style>
    .stApp {
        background-color: #f8fffa;
    }
    h1, h2, h3 {
        color: #2d6a4f;
    }
    div.stButton > button {
        background-color: #40916c;
        color: white;
        border-radius: 12px;
        font-weight: bold;
        padding: 0.5rem 1.2rem;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #2d6a4f;
    }
    .stImage {
        border-radius: 12px;
    }
    section[data-testid="stSidebar"] {
        background-color: #e8f5e9;
    }
</style>
""", unsafe_allow_html=True)

# ------------------- MENU -------------------
menu = st.sidebar.selectbox(
    "🌿 Navegação",
    ["🏠 Início", "🌳 Florestas", "🌊 Oceanos", "⛰️ Montanhas", "🌸 Curiosidades"]
)

# ------------------- PÁGINAS -------------------

if menu == "🏠 Início":
    st.title("🌿 Beleza da Natureza")
    st.subheader("Explorando as maravilhas do nosso planeta")
    
    st.image("https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1200", caption="A natureza é nossa maior riqueza", use_container_width=True)
    
    st.write("""
    ## 💚 Bem-vindo ao nosso passeio!
    
    O nosso planeta é incrível — cheio de florestas exuberantes, oceanos misteriosos, 
    montanhas majestosas e uma biodiversidade que nos deixa de queixo caído. 
    
    Este espaço foi criado para você conhecer e se apaixonar um pouco mais 
    pelas maravilhas da Terra. 🌍✨
    
    ---
    
    🔍 **Use o menu ao lado** para explorar cada categoria!
    """)
    
    st.info("💡 *'A natureza não é um lugar para visitar. É o lar.'* — Wendell Berry")

elif menu == "🌳 Florestas":
    st.title("🌳 Florestas: Os Pulmões do Mundo")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?w=600", caption="Floresta Amazônica — Brasil", use_container_width=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1473448912268-2022ce9509d8?w=600", caption="Floresta boreal — Canadá", use_container_width=True)
    
    st.markdown("""
    ### 🌲 Por que as florestas são tão importantes?
    
    - 🌳 Produzem **oxigênio** para respirarmos
    - 💧 Regulam o ciclo da **água**
    - 🏠 Abrigam mais de **80%** das espécies terrestres
    - 🛡️ Protegem o solo contra erosão
    - 🌍 Armazenam carbono, ajudando no clima do planeta
    
    ### 📍 Curiosidade:
    A **Floresta Amazônica** é a maior floresta tropical do mundo! 
    Abrange cerca de 5,5 milhões de km² e abriga milhões de espécies 
    que ainda nem foram descobertas. 🌎
    """)

elif menu == "🌊 Oceanos":
    st.title("🌊 Oceanos: O Coração Azul do Planeta")
    
    st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1000", caption="Oceano — fonte de vida", use_container_width=True)
    
    st.markdown("""
    ### 🐚 O que você precisa saber:
    
    - 🌙 Cobrem **71%** da superfície da Terra
    - 💡 Produzem mais de **50% do oxigênio** que respiramos
    - 🌡️ Regulam a temperatura global
    - 🐠 Abrigam uma biodiversidade impressionante
    - 🚢 São responsáveis por grande parte do clima do planeta
    
    ### 🐢 Uma verdade fascinante:
    Apenas cerca de **5% dos oceanos** do mundo foram explorados. 
    Isso significa que sabemos mais sobre a superfície da Lua 
    do que sobre os oceanos da nossa própria casa! 🌊🔭
    """)
    
    st.image("https://images.unsplash.com/photo-1583212292454-1fe622965b47?w=600", caption="Vida marinha colorida", use_container_width=True)

elif menu == "⛰️ Montanhas":
    st.title("⛰️ Montanhas: Gigantes da Terra")
    
    st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1000", caption="Montanhas nevadas — majestosas", use_container_width=True)
    
    st.markdown("""
    ### 🏔️ As montanhas são essenciais para nós:
    
    - 💧 São as **torres de água** do mundo — abrigam quase todo o gelo do planeta
    - 🌡️ Influenciam o clima e os ventos
    - 🏠 São lar de povos tradicionais e espécies únicas
    - ⛰️ Representam desafio, beleza e força
    
    ### 📏 Você sabia?
    O **Monte Everest** é a montanha mais alta do mundo acima do nível do mar: 
    **8.848 metros!** 🏔️ Mas a montanha mais alta do mundo inteiro, 
    se contarmos da base ao topo, é o **Mauna Kea**, no Havaí — a maior parte dela está debaixo d'água! 🌊⛰️
    """)

elif menu == "🌸 Curiosidades":
    st.title("🌸 Curiosidades da Natureza")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🪴 Plantas incríveis")
        st.image("https://images.unsplash.com/photo-1518495973542-4542c06a5843?w=400", use_container_width=True)
        st.write("As plantas conseguem sentir o ambiente ao redor — algumas até emitem sons quando precisam de água!")
        
        st.divider()
        
        st.markdown("### 🐋 O maior ser vivo")
        st.image("https://images.unsplash.com/photo-1566900775201-034b14dcb8c4?w=400", use_container_width=True)
        st.write("A **baleia-azul** é o maior animal que já existiu na Terra — chega a 30 metros de comprimento!")
    
    with col2:
        st.markdown("### 🌧️ A floresta que chove")
        st.image("https://images.unsplash.com/photo-1504744480895-7a89cf07e39a?w=400", use_container_width=True)
        st.write("A Floresta Amazônica cria sua própria chuva — as árvores liberam vapor que forma nuvens!")
        
        st.divider()
        
        st.markdown("### 🌍 O planeta se recupera")
        st.image("https://images.unsplash.com/photo-1515169187536-40708703368c?w=400", use_container_width=True)
        st.write("Quando cuidamos bem da natureza, ela tem uma capacidade incrível de se recuperar e crescer ainda mais forte. 💚")
    
    st.divider()
    
    st.success("💚 Cuide da natureza, como ela cuida de você!")
    st.caption("Projeto Beleza da Natureza | 2026")
