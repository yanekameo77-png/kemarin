import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import time 
#=========================
# Background
#=========================
import streamlit as st

st.set_page_config(
    page_title="CalcuGas",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# NAVY GLASS THEME
# =========================
st.markdown("""
<style>

/* Background utama */
.stApp{
    background: linear-gradient(
        135deg,
        #3B82F6 0%,
        #60A5FA 35%,
        #93C5FD 70%,
        #BFDBFE 100%
    );
    background-attachment: fixed;
}

/* Sidebar Glass */
section[data-testid="stSidebar"]{
    background: rgba(10, 25, 47, 0.70);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* SEMUA TULISAN SIDEBAR PUTIH */
section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Judul radio */
div[data-testid="stRadio"] > label{
    color:white !important;
    font-weight:bold !important;
    font-size:18px !important;
}


/* Header sidebar */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color: white !important;
    font-weight: 700;
}

/* Radio Menu */
div[role="radiogroup"]{
    background: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Setiap pilihan menu */
div[role="radiogroup"] label{
    background: rgba(255,255,255,0.04);
    border-radius: 15px;
    padding: 12px 15px;
    margin-bottom: 8px;
    transition: all 0.3s ease;
}

/* Hover */
div[role="radiogroup"] label:hover{
    background: rgba(59,130,246,0.20);
    transform: translateX(5px);
}

/* Tulisan menu */
div[role="radiogroup"] p{
    color: white !important;
    font-weight: 600;
}

/* Tombol */
.stButton > button{
    width:100%;
    border:none;
    border-radius:15px;
    background: linear-gradient(
        135deg,
        #1e3a8a,
        #2563eb
    );
    color:white;
    font-weight:bold;
    padding:12px;
    transition:0.3s;
}

.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 8px 20px rgba(37,99,235,0.4);
}

/* Card Glass */
.glass-card{
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(15px);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:20px;
    padding:20px;
    margin-bottom:15px;
}

/* Hilangkan warna putih bawaan */
[data-testid="stHeader"]{
    background: transparent;
}

/* Footer */
footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)
# =========================
# KALKULATOR CEPAT
# =========================
import streamlit as st
import math

def kalkulator_samping():

    st.markdown("### 🧮 Kalkulator Cepat")

    ekspresi = st.text_input(
        "Masukkan perhitungan",
        ""
    )

    with st.expander("📖 Contoh Penggunaan"):
        st.write("""
        **Operasi dasar**
        - 2+3
        - 10-4
        - 5*6
        - 20/4
    
        **Pangkat**
        - 2^3
        - 5^2
    
        **Akar**
        - sqrt(9)
        - sqrt(25)
    
        **Logaritma**
        - log(100)
    
        **Trigonometri**
        - sin(pi/2)
        - cos(0)
        - tan(pi/4)
        """)

    if st.button("Hitung", key="btn_sidebar"):

        try:
            ekspresi = ekspresi.replace("^", "**")

            hasil = eval(
                ekspresi,
                {"__builtins__": None},
                {
                    "sqrt": math.sqrt,
                    "sin": math.sin,
                    "cos": math.cos,
                    "tan": math.tan,
                    "log": math.log10,
                    "pi": math.pi,
                    "e": math.e
                }
            )

            st.success(f"Hasil = {hasil}")
            except ZeroDivisionError:
                st.error("Tidak bisa membagi dengan nol.")
            except SyntaxError:
                st.error("Format perhitungan salah.")
            except TypeError:
                st.error("Gunakan titik (.) sebagai desimal, misalnya 24.63.")
            except Exception:
                st.error("Terjadi kesalahan pada perhitungan.")
                
    st.markdown("### 🌡️ Konverter Suhu")

    suhu = st.number_input(
        "Nilai Suhu",
        key="suhu"
    )

    dari = st.selectbox(
        "Dari",
        ["Celsius", "Kelvin", "Fahrenheit"],
        key="dari"
    )

    ke = st.selectbox(
        "Ke",
        ["Celsius", "Kelvin", "Fahrenheit"],
        key="ke"
    )

    hasil = suhu

    # Celsius
    if dari == "Celsius":
        if ke == "Kelvin":
            hasil = suhu + 273
        elif ke == "Fahrenheit":
            hasil = (suhu * 9/5) + 32

    # Kelvin
    elif dari == "Kelvin":
        if ke == "Celsius":
            hasil = suhu - 273
        elif ke == "Fahrenheit":
            hasil = (suhu - 273) * 9/5 + 32

    # Fahrenheit
    elif dari == "Fahrenheit":
        if ke == "Celsius":
            hasil = (suhu - 32) * 5/9
        elif ke == "Kelvin":
            hasil = (suhu - 32) * 5/9 + 273

    st.info(f"Hasil = {hasil:.2f} {ke}")

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    "📌 Silakan Pilih Halaman",
    ["🏠 Home",
     "🧪 Studi Kasus",
     "📘 Hukum Boyle",
     "📘 Hukum Charles",
     "📘 Hukum Gay-Lussac",
     "⚗️ Gas Ideal",
     "📈 Regresi Linear",
     "ℹ️ Tentang Aplikasi",
     "📬 Kotak Saran"]
)

# =========================
# HOME
# =========================
# =========================
# HOME
# =========================
if menu == "🏠 Home":

    st.markdown("""
    <div style="
        padding:30px;
        border-radius:25px;
    ">
    
    <h1>⚗️ CalcuGas Dashboard</h1>
    
    <p style="
        color:#e6f0ff;
        text-align:center;
        font-size:18px;
    ">
        Kalkulator Hukum Gas Ideal Interaktif
        <br>
        Simulasi • Regresi Linear • Quiz • Perhitungan Gas
    </p>
    
    </div>
    """, unsafe_allow_html=True)

   

    st.write("")
    st.write("")

    # =========================
    # KARTU FITUR
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="
            background:rgba(255,255,255,0.08);
            padding:25px;
            border-radius:20px;
            border:1px solid rgba(255,255,255,0.1);
            text-align:center;
            backdrop-filter:blur(12px);
        ">
            <h2>🧪</h2>
            <h3 style="color:white;">Studi Kasus</h3>
            <p style="color:#d6e6ff;">
            Simulasi massa jenis gas dan quiz interaktif.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background:rgba(255,255,255,0.08);
            padding:25px;
            border-radius:20px;
            border:1px solid rgba(255,255,255,0.1);
            text-align:center;
            backdrop-filter:blur(12px);
        ">
            <h2>⚗️</h2>
            <h3 style="color:white;">Gas Ideal</h3>
            <p style="color:#d6e6ff;">
            Hitung tekanan, volume, mol, dan suhu.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            background:rgba(255,255,255,0.08);
            padding:25px;
            border-radius:20px;
            border:1px solid rgba(255,255,255,0.1);
            text-align:center;
            backdrop-filter:blur(12px);
        ">
            <h2>📈</h2>
            <h3 style="color:white;">Regresi Linear</h3>
            <p style="color:#d6e6ff;">
            Analisis data dan grafik regresi otomatis.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # =========================
    # FITUR APLIKASI
    # =========================
    st.markdown("""
    <div style="
    background:rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.1);
    ">
    
    <h2 style="color:white;">
    🔬 Fitur Utama CalcuGas
    </h2>
    
    <ul style="
    color:#e6f0ff;
    line-height:2;
    font-size:17px;
    ">
    <li>🧪 Studi Kasus Interaktif</li>
    <li>📘 Hukum Boyle</li>
    <li>📘 Hukum Charles</li>
    <li>📘 Hukum Gay-Lussac</li>
    <li>⚗️ Persamaan Gas Ideal</li>
    <li>📈 Regresi Linear</li>
    <li>📝 Quiz Hukum Gas</li>
    <li>📬 Kotak Saran</li>
    </ul>
    
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.success("👈 Pilih menu pada sidebar untuk memulai.")
# =========================
# STUDI KASUS
# =========================
elif menu == "🧪 Studi Kasus":

    kiri, kanan = st.columns([3,1])

    with kiri:

        pilihan = st.selectbox(
            "Pilih Studi Kasus",
            ["Simulasi Massa Jenis Gas","Quiz Hukum Gas"]
        )
    
        # ===================================
        # SIMULASI MASSA JENIS GAS
        # ===================================
        if pilihan == "Simulasi Massa Jenis Gas":
    
            st.title("Simulasi Gas Ideal Interaktif")
    
            st.write("""
            Aplikasi ini menghitung massa jenis gas menggunakan persamaan gas ideal.
    
            Pengguna dapat mengubah:
            - tekanan (atm)
            - suhu (K)
            - Bobot Molekul gas (g/mol)
            """)
    
            st.subheader("Input Variabel")
    
            P = st.slider(
                "Tekanan Gas (atm)",
                0.1,
                10.0,
                2.0,
                0.1
            )
    
            T = st.slider(
                "Suhu Gas (K)",
                100,
                1000,
                298
            )
    
            n = st.number_input(
                "Bobot Molekul Gas (g/mol)",
                value=32.0
            )
    
            R = 0.082
            
            #===================
            #KECEPATAN ANIMASI
            #===================
    
            kecepatan = max(0.5, 8 - (T / 150))
    
            # =======================
            # PENJELASAN
            # =======================
    
            st.info(
                f"""
                Tekanan = {P} atm
    
                Suhu = {T} K
    
                Bobot Molekul = {n} g/mol
    
                Semakin tinggi suhu, partikel bergerak semakin cepat.
                """
            )
            #====================
            #HTML + CSS ANIMASI
            #=====================
    
            html_code = f"""
            <!DOCTYPE html>
    
            <head>
    
            <style>
    
            body {{
                margin:0;
                overflow:hidden;
                background-color:transparent;
            }}
    
            .kotak {{
                width:100%;
                height:420px;
    
                position:relative;
                overflow:hidden;
    
                border-radius:20px;
    
                background:
                radial-gradient(circle,
                #1e3a8a,
                #020617);
    
                border:2px solid cyan;
    
                box-shadow:
                0px 0px 25px rgba(0,255,255,0.4);
            }}
    
            .bola{{
            
                width:18px;
                height:18px;
    
                position:absolute;
    
                border-radius:50%;
    
                background:cyan;
    
                box-shadow:
                0 0 15px cyan,
                0 0 30px cyan;
            }}
            
            .b1 {{
                animation: gerak1 {kecepatan}s linear infinite alternate;
            }}
    
            .b2 {{
                animation: gerak2 {kecepatan*0.8}s linear infinite alternate;
            }}
    
            .b3 {{
                animation:gerak3 {kecepatan*1.2}s linear infinite alternate;
            }}
    
            .b4 {{
                animation: gerak4 {kecepatan*0.6}s linear infinite alternate;
            }}
            @keyframes gerak1 {{
    
                from {{
                    transform: translate(0px,0px);
                }}
    
                to {{
                    transform: translate(320px,240px);
                }}
            }}
    
            @keyframes gerak2 {{
            
                from {{
                    transform: translate(0px,200px);
                }}
                to {{
                    transform: translate(280px,-60px);
                }}
            }}
    
            @keyframes gerak3 {{
            
                from {{
                    transform: translate(150px,0px);
                }}
            
                to {{
                    transform: translate(-120px,250px);
                }}
            }}
    
            @keyframes gerak4 {{
            
                0% {{
                    transform: translate(0px,0px);
                }}
            
                25% {{
                    transform: translate(220px,50px);
                }}
    
                50% {{
                    transform: translate(100px,220px);
                }}
            
                75% {{
                    transform: translate(260px,130px);
                }}
    
                100% {{
                    transform: translate(50px,260px);
                }}
            }}
    
            </style>
    
            </head>
    
            <body>
    
            <div class="kotak">
    
                <div class="bola b1"
                style="left:20px; top:20px;">
                </div>
    
                <div class="bola b2"
                style="left:80px; top:100px;">
                </div>
    
                <div class="bola b3"
                style="left:180px; top:150px;">
                </div>
    
                <div class="bola b4"
                style="left:300px; top:80px;">
                </div>
    
                <div class="bola b1"
                style="left:400px; top:200px;">
                </div>
    
                <div class="bola b2"
                style="left:520px; top:140px;">
                </div>
    
                <div class="bola b3"
                style="left:620px; top:240px;">
                </div>
    
                <div class="bola b4"
                style="left:700px; top:100px;">
                </div>
    
            </div>
    
            </body>
            </html>
            """
            #==================
            #TAMPILAN ANIMASI
            #==================
    
            st.subheader("🌌 Simulasi Pergerakan Partikel")
    
            components.html(
                html_code,
                height=430
            )
    
            #======================
            # PERSAMAAN GAS IDEAL
            #======================
            st.subheader("Persamaan Gas Ideal")
    
            st.latex(r"PV=nRT")
    
            st.write("Untuk mencari massa jenis gas:")
    
            st.latex(r"\rho=\frac{Pn}{RT}")
    
            #=======================
            # PERHITUNGAN OTOMATIS
            #=======================
    
            hasil = (P * n) / (R * T)
    
            #====================
            # LANGKAH PERHITUNGAN
            #====================
    
            st.subheader("Langkah Perhitungan")
    
            st.latex(
                rf"\rho=\frac{{({P})({n})}}{{({R})({T})}}"
            )
    
    
            #==========================
            # TOMBOL HASIL + KESIMPULAN
            #===========================
    
            if st.button("✨ Tampilkan Hasil"):
    
                with st.spinner("Menghitung massa jenis gas..."):
    
                    progress = st.progress(0)
    
                    for i in range(100):
                        time.sleep(0.01)
                        progress.progress(i + 1)
    
                st.success("Perhitungan berhasil✨!")
                st.balloons()
    
                st.markdown(
                    f"""
                    <div style="
                    background:linear-gradient(to right,#BFEFFF,#87CEFA);
                    padding:30px;
                    border-radius:20px;
                    color:black;
                    box-shadow:0px 0px 25px rgba(137,207,240,0.6);
                    animation: fadein 1s;
                    ">
    
                    <h1 style="
                    text-align:center;
                    font-size:40px;
                    ">
                    Massa Jenis Gas
                    </h1>
    
                    <hr>
    
                    <h2 style="
                    text-align:center;
                    font-size:35px;
                    ">
                    {hasil:.2f} g/mL
                    </h2>
    
                    <br>
    
                    <h3> Kesimpulan</h3>
    
                    <p style="font-size;20px; line-height:1.8;">
    
                    Dengan:
                    <br>
                    • tekanan = {P} atm
                    <br>
                    • suhu = {T} K
                    <br>
                    • Bobot Molekul = {n} g/mol
                    <br><br>
    
                    Maka massa jenis gas adalah:
    
                    <b>{hasil:.2f} g/mL</b>
    
                    </p>
    
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
            #===================
            # Test
            #===================
    
            assert hasil > 0, "Hasil tidak boleh negatif"
    
        #==================
        # Quiz
        #==================
        
        elif pilihan == "Quiz Hukum Gas":
        
            st.markdown("## 📝 Quiz Hukum Gas")
                
            st.write(
                "Jawab pertanyaan berikut untuk menguji pemahamanmu tentang hukum-hukum gas."
            )
            
            # =========================
            # SESSION STATE
            # =========================
            if "soal" not in st.session_state:
                st.session_state.soal = 1
            
            if "skor" not in st.session_state:
                st.session_state.skor = 0
            
            st.progress((st.session_state.soal-1)/10)
            
            # =========================
            # SOAL 1
            # =========================
            if st.session_state.soal == 1:
            
                jawaban = st.radio(
                    "1. Hukum Boyle menyatakan hubungan antara...",
                    [
                        "Tekanan dan Volume",
                        "Volume dan Suhu",
                        "Tekanan dan Suhu",
                        "Mol dan Volume"
                    ],
                    index=None
                )
            
                if st.button("➡️ Berikutnya"):
            
                    if jawaban == "Tekanan dan Volume":
                        st.session_state.skor += 10
            
                    st.session_state.soal = 2
                    st.rerun()
            
            # =========================
            # SOAL 2
            # =========================
            elif st.session_state.soal == 2:
            
                jawaban = st.radio(
                    "2. Jika suhu gas meningkat pada tekanan tetap maka volumenya...",
                    [
                        "Tetap",
                        "Menurun",
                        "Meningkat",
                        "Menjadi nol"
                    ],
                    index=None
                )
            
                if st.button("➡️ Berikutnya"):
            
                    if jawaban == "Meningkat":
                        st.session_state.skor += 10
            
                    st.session_state.soal = 3
                    st.rerun()
            
            # =========================
            # SOAL 3
            # =========================
            elif st.session_state.soal == 3:
            
                jawaban = st.radio(
                    "3. Hukum Gay-Lussac menjelaskan hubungan antara...",
                    [
                        "Tekanan dan Suhu",
                        "Volume dan Suhu",
                        "Volume dan Mol",
                        "Massa dan Volume"
                    ],
                    index=None
                )
            
                if st.button("➡️ Berikutnya"):
            
                    if jawaban == "Tekanan dan Suhu":
                        st.session_state.skor += 10
            
                    st.session_state.soal = 4
                    st.rerun()
            
            # =========================
            # SOAL 4
            # =========================
            elif st.session_state.soal == 4:
            
                jawaban = st.radio(
                    "4. Satuan suhu dalam hukum gas adalah...",
                    [
                        "Celcius",
                        "Kelvin",
                        "Fahrenheit",
                        "Rankine"
                    ],
                    index=None
                )
            
                if st.button("➡️ Berikutnya"):
            
                    if jawaban == "Kelvin":
                        st.session_state.skor += 10
            
                    st.session_state.soal = 5
                    st.rerun()
            
            # =========================
            # SOAL 5
            # =========================
            elif st.session_state.soal == 5:
            
                jawaban = st.radio(
                    "5. Persamaan gas ideal adalah...",
                    [
                        "PV = nRT",
                        "P = m/V",
                        "F = ma",
                        "V = IR"
                    ],
                    index=None
                )
            
                if st.button("➡️ Berikutnya"):
            
                    if jawaban == "PV = nRT":
                        st.session_state.skor += 10
            
                    st.session_state.soal = 6
                    st.rerun()
            
            # =========================
            # SOAL 6
            # =========================
            elif st.session_state.soal == 6:
            
                jawaban = st.number_input(
                    "6. P1=2 atm, V1=4 L, P2=4 atm. Berapa V2?",
                    value=None,
                    placeholder="Masukkan jawaban"
                )
            
                if st.button("➡️ Berikutnya"):
            
                    if jawaban is not None and abs(jawaban - 2) < 0.01:
                        st.session_state.skor += 10
            
                    st.session_state.soal = 7
                    st.rerun()
            
            # =========================
            # SOAL 7
            # =========================
            elif st.session_state.soal == 7:
            
                jawaban = st.number_input(
                    "7. V1=2 L, T1=300 K, T2=450 K. Berapa V2?",
                    value=None,
                    placeholder="Masukkan jawaban"
                )
            
                if st.button("➡️ Berikutnya"):
            
                    if jawaban is not None and abs(jawaban - 3) < 0.01:
                        st.session_state.skor += 10
            
                    st.session_state.soal = 8
                    st.rerun()
            
            # =========================
            # SOAL 8
            # =========================
            elif st.session_state.soal == 8:
            
                 jawaban = st.number_input(
                    "8. P1=1 atm, T1=300 K, T2=600 K. Berapa P2?",
                    value=None,
                    placeholder="Masukkan jawaban"
                )
            
                 if st.button("➡️ Berikutnya"):
            
                    if jawaban is not None and abs(jawaban - 2) < 0.01:
                        st.session_state.skor += 10
            
                    st.session_state.soal = 9
                    st.rerun()
            
            # =========================
            # SOAL 9
            # =========================
            elif st.session_state.soal == 9:
            
                jawaban = st.number_input(
                    "9. P=1 atm, V=24,63 L, T=300 K, R=0,0821. Berapa n?",
                    value=None,
                    placeholder="Masukkan jawaban"
                )
            
                if st.button("➡️ Berikutnya"):
            
                    if jawaban is not None and abs(jawaban - 1) < 0.05:
                        st.session_state.skor += 10
            
                    st.session_state.soal = 10
                    st.rerun()
            
            # =========================
            # SOAL 10
            # =========================
            elif st.session_state.soal == 10:
            
                jawaban = st.number_input(
                    "10. P=2 atm, V=10 L, n=1 mol, R=0,0821. Berapa T?",
                    value=None,
                    placeholder="Masukkan jawaban"
                )
            
                if st.button("🏁 Selesai"):
            
                    if jawaban is not None and abs(jawaban - 243.61) < 0.1:
                        st.session_state.skor += 10
            
                    st.session_state.soal = 11
                    st.rerun()
            
            # =========================
            # HASIL AKHIR
            # =========================
            elif st.session_state.soal == 11:
            
                st.balloons()
            
                st.subheader("🏆 Hasil Quiz")
            
                st.success(
                    f"Skor Akhir Anda = {st.session_state.skor}/100"
                )
            
                if st.session_state.skor == 100:
                    st.success("🎉 Luar biasa! Semua jawaban benar.")
            
                elif st.session_state.skor >= 80:
                    st.info("👍 Sangat baik.")
            
                elif st.session_state.skor >= 60:
                    st.warning("🙂 Cukup baik.")
            
                else:
                    st.error("📚 Pelajari kembali materi hukum gas.")
            
                    if st.button("🔄 Ulangi Quiz"):
            
                        st.session_state.soal = 1
                        st.session_state.skor = 0
                        st.rerun()

    with kanan:
        kalkulator_samping()
    
# =========================
# BOYLE
# =========================
elif menu == "📘 Hukum Boyle":

    kiri, kanan = st.columns([3,1])

    with kiri: 

        st.subheader("📘 Hukum Boyle")
    
        st.write(""" Hukum Boyle menyatakan bahwa tekanan gas berbanding terbalik dengan volume gas, saat temperatur dan jumlah zat gas dijaga tetap konstan. Secara matematis, hal tersebut dapat dituliskan seperti berikut:
                
        PV = nRT
        """)
    
        st.latex(r"P_1V_1=P_2V_2")
    
        dicari = st.selectbox(
            "Pilih variabel yang dicari:",
            ["P1", "V1", "P2", "V2"]
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            P1 = st.number_input(
                "P1", value=0.0, disabled=(dicari == "P1")
            )
            V1 = st.number_input(
                "V1", value=0.0, disabled=(dicari == "V1")
            )
    
        with col2:
            P2 = st.number_input(
                "P2", value=0.0, disabled=(dicari == "P2")
            )
            V2 = st.number_input(
                "V2", value=0.0, disabled=(dicari == "V2")
            )
    
        if st.button(
            "Hitung",
            key="btn_boyle"
        ):
    
            try:
    
                if dicari == "P1":
                    hasil = (P2 * V2) / V1
    
                    st.success(f"P1 = {hasil:.3f}")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"P_1=\frac{P_2V_2}{V_1}")
                    st.latex(
                        fr"P_1=\frac{{({P2})({V2})}}{{{V1}}}"
                    )
                    st.latex(fr"P_1={hasil:.3f}")
    
                elif dicari == "V1":
                    hasil = (P2 * V2) / P1
    
                    st.success(f"V1 = {hasil:.3f}")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"V_1=\frac{P_2V_2}{P_1}")
                    st.latex(
                        fr"V_1=\frac{{({P2})({V2})}}{{{P1}}}"
                    )
                    st.latex(fr"V_1={hasil:.3f}")
    
                elif dicari == "P2":
                    hasil = (P1 * V1) / V2
    
                    st.success(f"P2 = {hasil:.3f}")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"P_2=\frac{P_1V_1}{V_2}")
                    st.latex(
                        fr"P_2=\frac{{({P1})({V1})}}{{{V2}}}"
                    )
                    st.latex(fr"P_2={hasil:.3f}")
    
                elif dicari == "V2":
                    hasil = (P1 * V1) / P2
    
                    st.success(f"V2 = {hasil:.3f}")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"V_2=\frac{P_1V_1}{P_2}")
                    st.latex(
                        fr"V_2=\frac{{({P1})({V1})}}{{{P2}}}"
                    )
                    st.latex(fr"V_2={hasil:.3f}")
    
            except ZeroDivisionError:
                st.error("Tidak boleh ada pembagi bernilai 0.")

    with kanan:
        kalkulator_samping()

# =========================
# CHARLES
# =========================
elif menu == "📘 Hukum Charles":

    kiri, kanan = st.columns([3,1])

    with kiri:

        st.subheader("📘 Hukum Charles")
    
        st.write("""Hukum Charles menyatakan apabila gas dalam sebuah ruang tertutup dengan tekanan yang dijaga konstan, membuat volume pada gas dalam jumlah tertentu akan berbanding lurus dengan temperatur mutlaknya.hal tersebut bisa dituliskan seperti ini:
        
        V ∝ T 
        """)
    
        st.latex(r"\frac{V_1}{T_1}=\frac{V_2}{T_2}")
    
        dicari = st.selectbox(
            "Pilih variabel yang dicari:",
            ["V1", "T1", "V2", "T2"]
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            V1 = st.number_input(
                "V1 (L)", value=0.0,
                disabled=(dicari == "V1")
            )
    
            T1 = st.number_input(
                "T1 (K)", value=0.0,
                disabled=(dicari == "T1")
            )
    
        with col2:
            V2 = st.number_input(
                "V2 (L)", value=0.0,
                disabled=(dicari == "V2")
            )
    
            T2 = st.number_input(
                "T2 (K)", value=0.0,
                disabled=(dicari == "T2")
            )
    
        if st.button(
            "Hitung",
            key="btn_charles"
        ):
    
            try:
    
                if dicari == "V1":
                    hasil = (V2 * T1) / T2
    
                    st.success(f"V1 = {hasil:.3f} L")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"V_1=\frac{V_2T_1}{T_2}")
                    st.latex(
                        fr"V_1=\frac{{({V2})({T1})}}{{{T2}}}"
                    )
                    st.latex(fr"V_1={hasil:.3f}\,L")
    
                elif dicari == "T1":
                    hasil = (V1 * T2) / V2
    
                    st.success(f"T1 = {hasil:.3f} K")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"T_1=\frac{V_1T_2}{V_2}")
                    st.latex(
                        fr"T_1=\frac{{({V1})({T2})}}{{{V2}}}"
                    )
                    st.latex(fr"T_1={hasil:.3f}\,K")
    
                elif dicari == "V2":
                    hasil = (V1 * T2) / T1
    
                    st.success(f"V2 = {hasil:.3f} L")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"V_2=\frac{V_1T_2}{T_1}")
                    st.latex(
                        fr"V_2=\frac{{({V1})({T2})}}{{{T1}}}"
                    )
                    st.latex(fr"V_2={hasil:.3f}\,L")
    
                elif dicari == "T2":
                    hasil = (V2 * T1) / V1
    
                    st.success(f"T2 = {hasil:.3f} K")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"T_2=\frac{V_2T_1}{V_1}")
                    st.latex(
                        fr"T_2=\frac{{({V2})({T1})}}{{{V1}}}"
                    )
                    st.latex(fr"T_2={hasil:.3f}\,K")
    
            except ZeroDivisionError:
                st.error("Tidak boleh ada pembagi bernilai 0.")

    with kanan:
        kalkulator_samping()

# =========================
# GAY LUSSAC
# =========================
elif menu == "📘 Hukum Gay-Lussac":

    kiri, kanan = st.columns([3,1])

    with kiri:

        st.subheader("📘 Hukum Gay-Lussac")
    
        st.write("""Hukum Gay-Lussac menyatakan bahwa tekanan pada gas berbanding lurus dengan temperatur mutlaknya, saat gas dijaga dalam volume dan jumlah zat yang tetap. Secara matematis, hal tersebut dapat dituliskan seperti ini:
    
        P ∝  T
        """)
    
        st.latex(r"\frac{P_1}{T_1}=\frac{P_2}{T_2}")
    
        dicari = st.selectbox(
            "Pilih variabel yang dicari:",
            ["P1", "T1", "P2", "T2"]
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            P1 = st.number_input(
                "P1 (atm)", value=0.0,
                disabled=(dicari == "P1")
            )
    
            T1 = st.number_input(
                "T1 (K)", value=0.0,
                disabled=(dicari == "T1")
            )
    
        with col2:
            P2 = st.number_input(
                "P2 (atm)", value=0.0,
                disabled=(dicari == "P2")
            )
    
            T2 = st.number_input(
                "Suhu 2 (K)", value=0.0,
                disabled=(dicari == "T2")
            )
    
        if st.button(
            "Hitung",
            key="btn_gaylussac"
        ):
    
            try:
    
                if dicari == "P1":
                    hasil = (P2 * T1) / T2
    
                    st.success(f"P1 = {hasil:.3f} atm")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"P_1=\frac{P_2T_1}{T_2}")
                    st.latex(
                        fr"P_1=\frac{{({P2})({T1})}}{{{T2}}}"
                    )
                    st.latex(fr"P_1={hasil:.3f}\,\text{{atm}}")
    
                elif dicari == "T1":
                    hasil = (P1 * T2) / P2
    
                    st.success(f"T1 = {hasil:.3f} K")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"T_1=\frac{P_1T_2}{P_2}")
                    st.latex(
                        fr"T_1=\frac{{({P1})({T2})}}{{{P2}}}"
                    )
                    st.latex(fr"T_1={hasil:.3f}\,\text{{K}}")
    
                elif dicari == "P2":
                    hasil = (P1 * T2) / T1
    
                    st.success(f"P2 = {hasil:.3f} atm")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"P_2=\frac{P_1T_2}{T_1}")
                    st.latex(
                        fr"P_2=\frac{{({P1})({T2})}}{{{T1}}}"
                    )
                    st.latex(fr"P_2={hasil:.3f}\,\text{{atm}}")
    
                elif dicari == "T2":
                    hasil = (P2 * T1) / P1
    
                    st.success(f"T2 = {hasil:.3f} K")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"T_2=\frac{P_2T_1}{P_1}")
                    st.latex(
                        fr"T_2=\frac{{({P2})({T1})}}{{{P1}}}"
                    )
                    st.latex(fr"T_2={hasil:.3f}\,\text{{K}}")
    
            except ZeroDivisionError:
                st.error("Tidak boleh ada pembagi bernilai 0.")

    with kanan:
        kalkulator_samping()

# =========================
# GAS IDEAL
# =========================
elif menu == "⚗️ Gas Ideal":

    kiri, kanan = st.columns([3,1])
    with kiri:

        st.subheader("📘 Persamaan Gas Ideal")
    
        st.write("""
        Gas ideal menjelaskan hubungan antara tekanan (P), volume (V),
        jumlah mol (n), dan suhu (T).
    
        Persamaan gas ideal:
        """)
    
        st.latex(r"PV=nRT")
    
        R = 0.0821  # L·atm/mol·K
    
        dicari = st.selectbox(
            "Pilih variabel yang dicari:",
            ["P", "V", "n", "T"]
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            P = st.number_input(
                "Tekanan (atm)", value=0.0,
                disabled=(dicari == "P")
            )
    
            V = st.number_input(
                "Volume (L)", value=0.0,
                disabled=(dicari == "V")
            )
    
        with col2:
            n = st.number_input(
                "Jumlah mol (mol)", value=0.0,
                disabled=(dicari == "n")
            )
    
            T = st.number_input(
                "Suhu (K)", value=0.0,
                disabled=(dicari == "T")
            )
    
        st.info(f"Konstanta gas (R) = {R} L·atm/mol·K")
    
        if st.button(
            "Hitung",
            key="btn_gasideal"
        ):
    
            try:
    
                if dicari == "P":
                    hasil = (n * R * T) / V
    
                    st.success(f"P = {hasil:.3f} atm")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"P=\frac{nRT}{V}")
                    st.latex(
                        fr"P=\frac{{({n})({R})({T})}}{{{V}}}"
                    )
                    st.latex(fr"P={hasil:.3f}\,\text{{atm}}")
    
                elif dicari == "V":
                    hasil = (n * R * T) / P
    
                    st.success(f"V = {hasil:.3f} L")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"V=\frac{nRT}{P}")
                    st.latex(
                        fr"V=\frac{{({n})({R})({T})}}{{{P}}}"
                    )
                    st.latex(fr"V={hasil:.3f}\,\text{{L}}")
    
                elif dicari == "n":
                    hasil = (P * V) / (R * T)
    
                    st.success(f"n = {hasil:.3f} mol")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"n=\frac{PV}{RT}")
                    st.latex(
                        fr"n=\frac{{({P})({V})}}{{({R})({T})}}"
                    )
                    st.latex(fr"n={hasil:.3f}\,\text{{mol}}")
    
                elif dicari == "T":
                    hasil = (P * V) / (n * R)
    
                    st.success(f"T = {hasil:.3f} K")
    
                    st.markdown("### Cara Kerja")
                    st.latex(r"T=\frac{PV}{nR}")
                    st.latex(
                        fr"T=\frac{{({P})({V})}}{{({n})({R})}}"
                    )
                    st.latex(fr"T={hasil:.3f}\,\text{{K}}")
    
            except ZeroDivisionError:
                st.error("Tidak boleh ada pembagi bernilai 0.")

    with kanan:
        kalkulator_samping()
        
# =========================
# REGRESI LINEAR (LINE CHART)
# =========================
elif menu == "📈 Regresi Linear":

    st.subheader("📈 Regresi Linear")

    x_input = st.text_input(
        "Data x (Tekanan) (pisahkan koma)",
        "1,2,3,4,5"
    )

    y_input = st.text_input(
        "Data y (Volume) (pisahkan koma)",
        "10,8,6,4,2"
    )

    if st.button("Hitung & Grafik"):

        try:
            # Convert data
            x = np.array([float(i.strip()) for i in x_input.split(",")])
            y = np.array([float(i.strip()) for i in y_input.split(",")])

            # Cek jumlah data
            if len(x) != len(y):
                st.error(
                    f"Jumlah data P ({len(x)}) dan V ({len(y)}) tidak sama!"
                )

            elif len(x) < 2:
                st.error(
                    "Minimal diperlukan 2 pasang data untuk regresi linear."
                )

            else:

                # Regresi linear
                m, b = np.polyfit(x, y, 1)
                y_pred = m * x + b

                # Hitung R²
                ss_res = np.sum((y - y_pred) ** 2)
                ss_tot = np.sum((y - np.mean(y)) ** 2)
                r2 = 1 - (ss_res / ss_tot)

                st.success(
                    f"Persamaan: y = {m:.3f}x + {b:.3f}"
                )

                st.info(
                    f"Koefisien Determinasi (r²) = {r2:.4f}"
                )

                # DataFrame
                df = pd.DataFrame({
                    "P": x,
                    "V (data asli)": y,
                    "V (regresi)": y_pred
                })

                df = df.sort_values("P")

                # Grafik
                st.line_chart(df.set_index("P"))

                st.dataframe(df)

        except ValueError:
            st.error(
                "Pastikan semua data berupa angka dan dipisahkan dengan koma."
            )

#=========================
# LATAR BELAKANG APK
#=========================
elif menu == "ℹ️ Tentang Aplikasi":

    st.title("✨Tentang Aplikasi ini")
    
    st.write("""
             Kalkulator Gas Ideal
             Kalkulator gas ideal merupakan aplikasi berbasis web yang dirancang untuk 
             membantu mahasiswa dan pengguna dalam melakukan perhitungan hukum
             gas ideal secara cepat, akurat dan interaktif. Aplikasi ini mempermudah 
             analisis hubungan antara tekanan (P), volume (V), suhu (T) dan jumlah mol (n) tanpa
             perlu melakukan perhitungan manual yang kompleks.

             Dengan antarmuka yang sederhana dan mudah digunakan, apllikasi ini
             mendukung proses pembelajaran serta kegiatan laboratorium sehingga
             pengguna dapat memahami konsep hukum gas ideal dengan lebih efektif.
             Selain sebagai alat bantu hitungan, aplikasi ini juga menjadi media 
             pembelajaran digital yang mendukung efisiensi dan pemanfaatan teknologi
             dalam bidang kimia analisis.
    """)

#========================
# Kotak Saran
#========================
elif menu == "📬 Kotak Saran":

    st.link_button(
        "📬Isi kotak saran",
        "https://forms.gle/whtokShqsm9jkQuE6"
    )

    st.write("""
        Terima Kasih Telah Berkunjung
        Semoga setiap perhitungan yang dilakukan dapat membantu anda memahami
        dunia gas ideal dengan lebih mudah dan menyenangkan.
        Terimakasih telah mencoba web aplikasi ini. Dukungan, kritik dan saran 
        dari anda menjadi motivasi bagi kami untuk terus menghadirkan fitur yang lebih baik.
        """)

    st.markdown("""
    
    Tetaplah kuat
    Walau kadang yang merusak mental justru
    nilai mata uang rupiah yang semakin lemah
    
    """) 

    st.write("""
    Dibuat oleh kelompok 3:
    Achmad Rifa`i (2560552), Bianca Titanya Wibowo (2560597),
    Maulida Fathiyyah Khansa (2560666),Naila Safha Azzahra (2560702),
    Sandra Amelia Lian (2560772)
    """)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Kelompok 3 kelas 1A")
