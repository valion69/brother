import streamlit as st
st.set_page_config(layout="wide")

# Définir les URLs des rapports Power BI
url_detection_anomalie = "https://app.powerbi.com/view?r=eyJrIjoiMzlhMmJhYTUtYmFlNi00M2M3LTk5MTEtZDdmNGQxZThmODIxIiwidCI6IjhmMDQ4NTc4LWI0NGItNDRlMi04N2UyLWEyN2NkMzE0NTg2ZCIsImMiOjh9"
url_prediction = "https://app.powerbi.com/view?r=eyJrIjoiMzlhMmJhYTUtYmFlNi00M2M3LTk5MTEtZDdmNGQxZThmODIxIiwidCI6IjhmMDQ4NTc4LWI0NGItNDRlMi04N2UyLWEyN2NkMzE0NTg2ZCIsImMiOjh9"
url_social = "https://docs.google.com/forms/d/e/1FAIpQLSeMMDfYsfcs7YYD82vvt2Dro-026iGa24EZWV7QtD-41o9Big/viewform"

# Appliquer des styles CSS pour les boutons
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        color: white;
        background-color: #007BFF;
        border: none;
        border-radius: 5px;
        margin: 5px 0;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

# Définir le titre de l'application
st.title("Application de Surveillance")

# Utiliser la session state pour gérer le menu sélectionné
if 'menu' not in st.session_state:
    st.session_state.menu = "Détection d'Anomalie"

# Afficher l'image du logo dans la barre latérale
st.sidebar.image("brother.png", use_column_width=False)

# Ajouter des boutons dans la barre latérale
if st.sidebar.button("Détection d'Anomalie"):
    st.session_state.menu = "Détection d'Anomalie"
if st.sidebar.button("Prediction"):
    st.session_state.menu = "Prediction"
if st.sidebar.button("Ambiance Sociale"):
    st.session_state.menu = "Ambiance Sociale"
if st.sidebar.button("Topic Modeling"):
    st.session_state.menu = "Topic Modeling"

# Afficher le contenu basé sur la sélection du menu
if st.session_state.menu == "Détection d'Anomalie":
    st.header("Détection d'Anomalie")
    st.markdown(f'<iframe width="100%" height="800" src="{url_detection_anomalie}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

elif st.session_state.menu == "Prediction":
    st.header("Prediction")
    st.markdown(f'<iframe width="100%" height="800" src="{url_prediction}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

elif st.session_state.menu == "Ambiance Sociale":
    st.header("Ambiance Sociale")
    st.markdown(f'<iframe width="100%" height="800" src="{url_social}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    # Ajoutez le contenu spécifique ou le lien pour "Ambiance Sociale"

elif st.session_state.menu == "Topic Modeling":
    st.header("Topic Modeling")
    st.write("Contenu pour Topic Modeling à ajouter ici.")
    # Ajoutez le contenu spécifique ou le lien pour "Topic Modeling"
