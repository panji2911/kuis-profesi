import streamlit as st

# Judul Aplikasi
st.set_page_config(page_title="Kuis Profesi", layout="centered")
st.title("🔍 Kuis: Profesi Apa yang Cocok untukmu?")
st.write("Jawab pertanyaan berikut untuk mengetahui profesi yang paling cocok untukmu!")

# Inisialisasi skor
scores = {
    "Programmer": 0,
    "Designer": 0,
    "Data Scientist": 0
}

# Pertanyaan dan pilihan jawaban dengan nilai untuk setiap profesi
questions = [
    {
        "question": "Apa kegiatan favoritmu saat bekerja?",
        "options": {
            "Menulis kode dan membangun aplikasi": "Programmer",
            "Mendesain dan membuat hal-hal terlihat menarik": "Designer",
            "Menganalisis data dan mencari pola": "Data Scientist"
        }
    },
    {
        "question": "Mana yang paling kamu sukai?",
        "options": {
            "Logika dan pemrograman": "Programmer",
            "Warna dan estetika visual": "Designer",
            "Angka dan statistik": "Data Scientist"
        }
    },
    {
        "question": "Software apa yang paling sering kamu gunakan?",
        "options": {
            "Visual Studio Code atau PyCharm": "Programmer",
            "Adobe Photoshop atau Figma": "Designer",
            "Jupyter Notebook atau Excel": "Data Scientist"
        }
    },
    {
        "question": "Apa tipe tantangan yang kamu sukai?",
        "options": {
            "Menyelesaikan bug dalam program": "Programmer",
            "Membuat desain user-friendly": "Designer",
            "Memprediksi tren dari data": "Data Scientist"
        }
    },
    {
        "question": "Bagaimana kamu membuat keputusan?",
        "options": {
            "Berdasarkan logika dan algoritma": "Programmer",
            "Berdasarkan intuisi visual dan kreativitas": "Designer",
            "Berdasarkan data dan fakta": "Data Scientist"
        }
    }
]

# Menyimpan jawaban pengguna
answers = []

# Loop pertanyaan
for i, q in enumerate(questions):
    st.markdown(f"**{i+1}. {q['question']}**")
    choice = st.radio("", list(q["options"].keys()), key=f"q{i}")
    answers.append(q["options"][choice])

# Tombol untuk melihat hasil
if st.button("🔎 Lihat Hasil"):
    # Hitung skor berdasarkan jawaban
    for answer in answers:
        scores[answer] += 1

    # Tentukan profesi dengan skor tertinggi
    result = max(scores, key=scores.get)

    # Tampilkan hasil dengan gambar dan pesan
    st.markdown("---")
    st.header("✨ Hasil Kuismu:")
    
    if result == "Programmer":
        st.image("https://cdn-icons-png.flaticon.com/512/2721/2721297.png", width=150)
        st.success("Kamu cocok menjadi **Programmer**! 💻")
        st.write("Kamu suka menyelesaikan masalah dengan logika dan teknologi. Dunia kode adalah duniamu!")
    
    elif result == "Designer":
        st.image("https://cdn-icons-png.flaticon.com/512/3534/3534369.png", width=150)
        st.success("Kamu cocok menjadi **Designer**! 🎨")
        st.write("Kamu punya rasa estetika yang tinggi dan suka menciptakan desain yang memukau.")

    elif result == "Data Scientist":
        st.image("https://cdn-icons-png.flaticon.com/512/2965/2965567.png", width=150)
        st.success("Kamu cocok menjadi **Data Scientist**! 📊")
        st.write("Kamu suka bermain dengan data dan mengubahnya menjadi wawasan yang bermanfaat.")

    st.balloons()
