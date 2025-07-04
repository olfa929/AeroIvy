import streamlit as st
import streamlit.components.v1 as components
import base64

DEPARTMENTS = [
    "Intensive Care Unit (ICU)", "Cardiac Care Unit (CCU)",
    "Neonatal Intensive Care Unit (NICU)", "Pediatric Intensive Care Unit (PICU)",
    "Medical Ward", "Surgical Ward", "Maternity Ward", "Postpartum Ward",
    "Oncology Ward", "Psychiatric Inpatient Unit", "Rehabilitation Unit",
    "Step-Down Unit", "Burn Unit"
]
st.set_page_config(page_title="AeroIvy.ai Smart Mask Dashbord", layout="wide")
def do_login():
    if validate_credentials(hospital, role, name, password):
        st.session_state.auth = True
        st.session_state.user_name     = name
        st.session_state.user_role     = role
        st.session_state.user_hospital = hospital
    else:
        st.error("Invalid credentials. Please try again.")
if "auth" not in st.session_state:
    st.session_state.auth = False
if not st.session_state.auth:
    col_empty, col_form = st.columns([2, 2])

    with col_empty:
        st.write("")

    with col_form:
        st.markdown(
            """
            <style>
            .stApp {
                background-image: url("https://i.pinimg.com/736x/f7/10/3e/f7103e5b3a214fb77ad8b647003dfd4e.jpg");
                background-size: cover;
                background-position: center;
            }
            [data-testid="stHeader"] {
                visibility: hidden;
            }
            [data-testid="stHeader"] {
                visibility: hidden;
            }
            .stApp .block-container, 
            .stApp .block-container h1,
            .stApp .block-container h2,
            .stApp .block-container h3,
            .stApp .block-container label {
                color: white !important;
            }
            .stApp input, .stApp .stSelectbox, .stApp .stTextInput {
                color: white !important;
            }
            .stApp button[kind="primary"] {
                background-color: rgba(255,255,255,0.2) !important;
                color: white !important;
            }
            /* Background image */
            .stApp {
                background-image: url("https://sdmntprpolandcentral.oaiusercontent.com/files/00000000-faa4-620a-bf31-931036a927f1/raw?se=2025-07-04T07%3A12%3A56Z&sp=r&sv=2024-08-04&sr=b&scid=8333fe00-3aa0-57e7-a985-a1aae0bbd65d&skoid=31bc9c1a-c7e0-460a-8671-bf4a3c419305&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-03T15%3A17%3A11Z&ske=2025-07-04T15%3A17%3A11Z&sks=b&skv=2024-08-04&sig=BlSgGGE1efJYsP%2BMGwqY8ojlZ3QQzZXd/O2G5xH0dQ8%3D");
                background-size: cover;
                background-position: center;
            }
            /* Shrink and prevent wrapping of the main title */
            .stApp h1 {
                font-size: 1.5rem !important;
                white-space: nowrap !important;
            }
            
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <style>
            /* keep placeholders white but make typed text black */
            .stApp .stTextInput>div>div>input,
            .stApp .stTextInput>div>div>input[type="password"] {
                color: black !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.title("😷🏥 Real-Time Biochemical Monitoring With AeroIvy.ai")

        HOSPITALS = ["Hôpital Farhat-Hached (Sousse)","Hôpital Sahloul (Sousse)","Hôpital La Rabta (Tunis)","Hôpital Habib-Bourguiba (Sfax)",
        "Hôpital Hédi-Chaker (Sfax)","Hôpital Fattouma-Bourguiba (Monastir)","Hôpital Tahar-Sfar (Mahdia)","Hôpital Abderrahmène Mami (Ariana)",
        "Hôpital Aziza Othmana (Tunis)","Hôpital Béchir Hamza d'enfants (Tunis)","Hôpital Charles Nicolle (Tunis)","Hôpital Habib Thameur (Tunis)",
        "Hôpital militaire principal d'instruction (Tunis)","Hôpital Mohamed Sassi (Gabès)","Hôpital Mohamed Tlatli (Nabeul)","Hôpital Mongi Slim (La Marsa)",
        "Hôpital Taher Maâmouri (Nabeul)","Hôpital Ibn El Jazzar (Kairouan)","Clinique Internationale Hannibal (Tunis)","Clinique Soukra (Soukra)",
        "Centre International Carthage Médical (Monastir)","Clinique Alyssa (Tunis)","Clinique Taoufik (El Menzah)","Clinique Pasteur (Tunis)",
        "Clinique Méditerranéenne (Tunis)","Clinique de la Medina de Tunis","Clinique de l'Espoir (Tunis)","Clinique El Amen","Clinique Ophtalmologique de Tunis",
        "Clinique Ophtalmo du Lac Ste AMC","Clinique El Menzah (Tunis)","Clinique Saint Augustin (Tunis) "]

        ROLES = ["Doctor", "Nurse", "Biomedical Engineer", "Administration Staff"]

        def validate_credentials(establishment, role, name, password):
            user_db = {
            ("Hôpital Farhat-Hached (Sousse)", "Doctor", "ali"):           "Ali345!",
            ("Hôpital La Rabta (Tunis)",     "Biomedical Engineer", "Olfa Boutiti"): "23776493",
            ("Hôpital Sahloul (Sousse)",     "Nurse",  "sara"):          "Sara2025#",
            ("Hôpital La Rabta (Tunis)",     "Biomedical Engineer", "mohamed"): "Moha789$",
            ("Hôpital Habib-Bourguiba (Sfax)","Doctor", "amina"):         "Amina321@",
            ("Hôpital Hédi-Chaker (Sfax)",   "Nurse",  "omar"):          "Omar654%",
            ("Hôpital Fattouma-Bourguiba (Monastir)", "Administration Staff", "hanen"): "Hanen111^",
            ("Hôpital Tahar-Sfar (Mahdia)",  "Doctor", "anas"):           "Anas987&",
            ("Hôpital Abderrahmène Mami (Ariana)", "Biomedical Engineer", "malek"):    "Malek543*",
            ("Hôpital Aziza Othmana (Tunis)", "Nurse",  "aya"):           "Aya246!",
            ("Hôpital Charles Nicolle (Tunis)", "Doctor", "maya"):        "Maya369?"
            }
            name_norm = name.strip().lower()

            # scan your DB for a matching hospital+role and case-insensitive username
            for (hosp, rl, user_key), pwd in user_db.items():
                if hosp == establishment and rl == role and user_key.lower() == name_norm:
                    return pwd == password
            return False

        st.title("🔒 Login")
        # 1) Select hospital
        hospital = st.selectbox("Establishment (Hospital)", HOSPITALS)
        # 2a) Select role
        role = st.selectbox("Function / Role", ROLES)
        # 2b) Enter your name
        name = st.text_input("Your Name")
        # 3) Password
        password = st.text_input("Password", type="password")
        st.button("Login", on_click=do_login)

        
else:
       
    st.markdown(
        """
        <style>
        
        /* Hide the top bar */
        [data-testid="stHeader"] { visibility: hidden; }

        /* Make the Streamlit container fill the window */
        .appview-container .main,
        .block-container {
          margin: 0; 
          padding: 0;
          height: 100vh;
        }

        /* Full-screen background image */
        .stApp {
          background: url("https://sdmntprnortheu.oaiusercontent.com/files/00000000-6164-61f4-ac2d-6ceb6f5699a8/raw?se=2025-07-03T23%3A55%3A30Z&sp=r&sv=2024-08-04&sr=b&scid=5b62c6cd-2f5f-5a80-b9db-b6ede8c15fda&skoid=eb780365-537d-4279-a878-cae64e33aa9c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-03T06%3A43%3A22Z&ske=2025-07-04T06%3A43%3A22Z&sks=b&skv=2024-08-04&sig=R513T4SgaQZ/Ry%2BSP/24Nz5gWMQly0ho1o9LsZbmvQo%3D")
                      center/cover no-repeat !important;
        }

        
        </style>

        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style>
          /* Pin Streamlit’s widget panel to the top-right at full height */
          .appview-container .main .block-container {
            position: fixed !important;
            top: 0;
            right: 0;
            width: 60vw !important;
            height: 100vh !important;
            padding: 1rem !important;
            overflow-y: auto !important;
            z-index: 10;
          }
          /* Ensure the 3D model (<div id="leftModel">) stays underneath */
          #leftModel {
            z-index: 0 !important;
          }
          .appview-container .main .block-container label {
            color: white !important;

        }
        .stTextInput label,
        .stSelectbox label {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 2) Load & base64-encode your GLB
    file_path = r"C:\Users\bouti\Downloads\ImageToStl.com_Male\Male.glb"
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()

    # 3) Embed the 3D model, absolutely positioned
    
    col_empty, col_form = st.columns([4, 6], gap="small")
    with col_form:
        st.markdown(
        """
        <style>
          /* keep placeholders white but make typed text black */
          .stApp .stTextInput>div>div>input,
          .stApp .stTextInput>div>div>input[type="password"] {
              color: black !important;
          }

          /* shrink all inputs & selects to 50% of the container */
          .stApp .stTextInput>div,
          .stApp .stSelectbox>div {
            max-width: 50% !important;
          }
        </style>
        """,
        unsafe_allow_html=True,
        )
        # directly render your widgets here (no st.columns)
        st.write("")   # ← spacer
        st.write("")   # ← spacer
        user = st.session_state.get("user_name", "")
        hosp = st.session_state.get("user_hospital", "")
        st.markdown(
        f"<h3 style='color:white; margin-bottom:1rem;'>Welcome {user} from {hosp}</h3>",
        unsafe_allow_html=True
    )
        dept = st.selectbox("Department", DEPARTMENTS)
        patient_id   = st.text_input("Patient ID")
        patient_name = st.text_input("Patient Name")
        if st.button("Proceed"):
            
            st.success(f"Proceeding with {patient_name} ({patient_id}) in {dept}")
            # --- embed your standalone HTML dashboard here: ---
            with open("docdash.html", "r", encoding="utf-8") as f:
                dash_html = f.read()
        
            st.components.v1.html(
                dash_html,
                height=800,        # adjust height as needed
                scrolling=True
            )

  