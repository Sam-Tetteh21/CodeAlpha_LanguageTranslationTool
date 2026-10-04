# CodeAlpha_LanguageTranslationTool

A simple web-based Language Translation Tool built during my **CodeAlpha Artificial Intelligence Internship** (Task 1).

The app lets a user type text, choose a source and target language, and instantly get a translation — powered by Google Translate under the hood.

## 🎥 Demo
[[LinkedIn video link here]](https://lnkd.in/p/dyvTRXFy)

## 🌍 Live Demo
👉 [Try it live here](https://codealpha-languagetranslationtool.streamlit.app)

## ✨ Features
- Text input box for entering any text
- Dropdown menus to select source language (or auto-detect) and target language
- One-click translation
- Translated text shown clearly, in a copy-friendly text box

## 🛠️ Tech Stack
- **Python 3**
- **[Streamlit](https://streamlit.io/)** — turns a Python script into a web UI
- **[deep-translator](https://github.com/nidhaloff/deep-translator)** — free Python wrapper around Google Translate (no API key required)

## 📂 Project Structure
```
CodeAlpha_LanguageTranslationTool/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md
└── .gitignore
```

## 🚀 How to Run Locally

1. Clone this repository
   ```bash
   git clone https://github.com/<your-username>/CodeAlpha_LanguageTranslationTool.git
   cd CodeAlpha_LanguageTranslationTool
   ```

2. (Optional but recommended) create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app
   ```bash
   streamlit run app.py
   ```

5. Your browser will open automatically at `http://localhost:8501`

## 🧠 How It Works
1. The user types text and picks a source/target language from dropdowns populated dynamically from Google Translate's supported language list.
2. On clicking **Translate**, the app sends the text to Google Translate via the `deep-translator` library.
3. The translated result is displayed on screen in a text box the user can easily copy.

## 📌 About the Internship
This project was built as part of the **CodeAlpha Artificial Intelligence Internship**.

- Website: [www.codealpha.tech](https://www.codealpha.tech)
- Task: Language Translation Tool

## 👤 Author
**Samuel Tetteh**
BSc. Information Technology Education, Level 300
University of Skills Training and Entrepreneurial Development (USTED)

🔗 [LinkedIn](www.linkedin.com/in/samuel-tetteh-b5a247356) · [GitHub](https://github.com/Sam-Tetteh21)
