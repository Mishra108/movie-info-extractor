````md id="v5gc2q"
# 🎬 Movie Information Extractor

An AI-powered application that extracts movie details from a paragraph using LangChain, Mistral AI, and Streamlit.

## 🚀 Live Demo

🔗 Live App: [YOUR_STREAMLIT_LINK_HERE
](https://movieinfoextractor.streamlit.app/)
---

## 🚀 Features

- Extracts:
  - Movie Title
  - Release Year
  - Genre
  - Director
  - Cast
  - Rating
  - Summary

- Structured JSON Output
- Streamlit UI
- Download JSON Feature
- Powered by Mistral AI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- Pydantic

---

## 📌 Example Input

```text
Interstellar is a 2014 science fiction film directed by Christopher Nolan. 
The movie stars Matthew McConaughey and Anne Hathaway.
````

## ✅ Example Output

```json
{
  "title": "Interstellar",
  "release_year": 2014,
  "genre": ["Science Fiction"],
  "director": "Christopher Nolan",
  "cast": [
    "Matthew McConaughey",
    "Anne Hathaway"
  ]
}
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Mishra108/movie-info-extractor.git
```

Move into the project folder:

```bash
cd movie-info-extractor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Add API Key

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 👨‍💻 Author

Made by Mishra Ji 🚀

```
```
