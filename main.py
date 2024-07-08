import streamlit as st
st.set_page_config(layout="wide")

# Définir les URLs des rapports Power BI
url_vision_globale = "https://app.powerbi.com/view?r=eyJrIjoiNzRmOTM2NWItMDBmYy00NTIzLWE5YTEtM2ZhZTk1NGM4ZWVjIiwidCI6IjhmMDQ4NTc4LWI0NGItNDRlMi04N2UyLWEyN2NkMzE0NTg2ZCIsImMiOjh9"
url_detection_anomalie = "https://app.powerbi.com/view?r=eyJrIjoiMzlhMmJhYTUtYmFlNi00M2M3LTk5MTEtZDdmNGQxZThmODIxIiwidCI6IjhmMDQ4NTc4LWI0NGItNDRlMi04N2UyLWEyN2NkMzE0NTg2ZCIsImMiOjh9"
url_prediction = "https://app.powerbi.com/view?r=eyJrIjoiNTBhODZmNWEtMjJlOC00M2VkLWE0MjYtNWYzZjJlMTA5NzE3IiwidCI6IjhmMDQ4NTc4LWI0NGItNDRlMi04N2UyLWEyN2NkMzE0NTg2ZCIsImMiOjh9"
url_social = "https://app.powerbi.com/view?r=eyJrIjoiYTM1MGMyZmItZmRkYy00ZjE3LThiN2ItYjc0YTcxMTUyNGUxIiwidCI6IjhmMDQ4NTc4LWI0NGItNDRlMi04N2UyLWEyN2NkMzE0NTg2ZCIsImMiOjh9"
url_top_model = "https://app.powerbi.com/view?r=eyJrIjoiYzdhNmJiYzMtNTY2NC00MmVjLTg4NTgtMjBlN2M3MGM0YzI1IiwidCI6IjhmMDQ4NTc4LWI0NGItNDRlMi04N2UyLWEyN2NkMzE0NTg2ZCIsImMiOjh9"
url_sondage_campagne = "https://docs.google.com/forms/d/e/1FAIpQLSfCn-k-Oo9Uhu4o3Fvz0bEkRAJRL8FpU0Ble6sZl6hVXETChg/viewform?usp=sf_link"
url_sondage_it = "https://docs.google.com/forms/d/e/1FAIpQLSe6eN81PbBVTNbHOd5HqcFzCsy9nKFWkUgKglD8lO3_8MFThw/viewform?usp=sf_link"
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

# Utiliser la session state pour gérer le menu sélectionné
if 'menu' not in st.session_state:
    st.session_state.menu = "Vision Globale d’Activité"

# Afficher l'image du logo dans la barre latérale
st.sidebar.image("brother.png", use_column_width=False)

# Ajouter des boutons dans la barre latérale
if st.sidebar.button("Vision Globale d’Activité"):
    st.session_state.menu = "Vision Globale d’Activité"
if st.sidebar.button("Détection d'Anomalie"):
    st.session_state.menu = "Détection d'Anomalie"
if st.sidebar.button("Prediction"):
    st.session_state.menu = "Prediction"
if st.sidebar.button("Ambiance Sociale"):
    st.session_state.menu = "Ambiance Sociale"
if st.sidebar.button("Topic Modeling"):
    st.session_state.menu = "Topic Modeling"
if st.sidebar.button("Sondage Campagne 2024 : Brother est n°1"):
    st.session_state.menu = "Sondage Campagne 2024 : Brother est n°1"
if st.sidebar.button("Sondage IT Partners"):
    st.session_state.menu = "Sondage IT Partners"

# Afficher le contenu basé sur la sélection du menu
if st.session_state.menu == "Vision Globale d’Activité":
    st.header("Vision Globale d’Activité")
    st.markdown(f'<iframe width="100%" height="800" src="{url_vision_globale}" frameborder="0" allowfullscreen></iframe>',unsafe_allow_html=True)

elif st.session_state.menu == "Détection d'Anomalie":
    st.header("Détection d'Anomalie")
    st.markdown(f'<iframe width="100%" height="800" src="{url_detection_anomalie}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

elif st.session_state.menu == "Prediction":
    st.header("Prediction")
    st.markdown(f'<iframe width="100%" height="800" src="{url_prediction}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

elif st.session_state.menu == "Ambiance Sociale":
    st.header("Ambiance Sociale")
    st.markdown(f'<iframe width="100%" height="800" src="{url_social}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

elif st.session_state.menu == "Topic Modeling":
    st.header("Topic Modeling")
    st.markdown(f'<iframe width="100%" height="800" src="{url_top_model}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

elif st.session_state.menu == "Sondage Campagne 2024 : Brother est n°1":
    st.header("Sondage Campagne 2024 : Brother est n°1")
    st.markdown(f'<iframe width="100%" height="800" src="{url_sondage_campagne}" frameborder="0" allowfullscreen></iframe>',unsafe_allow_html=True)

elif st.session_state.menu == "Sondage IT Partners":
    st.header("Sondage IT Partners")
    st.markdown(f'<iframe width="100%" height="800" src="{url_sondage_it}" frameborder="0" allowfullscreen></iframe>',unsafe_allow_html=True)
