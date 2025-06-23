# 🤖 AI Chatbot with OpenRouter and Streamlit

## 📋 Description
Proyek ini adalah chatbot interaktif yang dibangun menggunakan **Streamlit** sebagai antarmuka pengguna dan **OpenRouter API** sebagai penyedia model AI (seperti GPT-3.5 atau Mistral). Cocok untuk tugas kuliah, demo AI, atau eksperimen chatbot pribadi.

## 🎯 Key Features

- 💬 **Tampilan Chat Bubble**  
  Menggunakan komponen `st.chat_message()` untuk menampilkan percakapan seperti aplikasi chat modern.

- 🔄 **Riwayat Chat**  
  Percakapan disimpan selama sesi berlangsung agar terasa natural dan berkelanjutan.

- 🧠 **Integrasi Model AI via OpenRouter**  
  Chatbot didukung oleh model besar seperti GPT-3.5 atau Mistral melalui OpenRouter API.

- ⚡ **Respon Dinamis**  
  Spinner dan feedback visual selama AI sedang berpikir.

## 🛠️ How to Run Locally

### 1. Clone Repo & Masuk Folder
```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

### 2. Buat Virtual Environment
```bash
python3 -m venv chatbot-env
source chatbot-env/bin/activate  # Linux/macOS/WSL
# .\chatbot-env\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run chatbot.py
```

## 📦 Requirements

File `requirement.txt` harus memuat minimal:
```
streamlit
requests
```

## 🔐 API Configuration

Edit `chatbot.py` dan ganti `OPEN_ROUTER_API_KEY` dengan key milikmu sendiri dari [https://openrouter.ai](https://openrouter.ai)

```python
OPEN_ROUTER_API_KEY = "your-api-key-here"
```

## 📡 Deployment (Optional)

Kamu bisa deploy ke:

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Hugging Face Spaces](https://huggingface.co/spaces)

## 🧑‍💻 Author

**Lathif Jumatiawan**  
Built with ❤️ and Python.