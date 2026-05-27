import json
import streamlit as st
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="🎬 Movie Info Extractor",
    page_icon="🎬",
    layout="centered"
)

# -------------------- Load Environment --------------------
load_dotenv()

# -------------------- Model --------------------
@st.cache_resource
def get_model():
    return ChatMistralAI(
        model="mistral-small-2506",
        temperature=0
    )

model = get_model()

# -------------------- Pydantic Schema --------------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str

# -------------------- Parser --------------------
parser = PydanticOutputParser(pydantic_object=Movie)

# -------------------- Prompt --------------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an AI assistant that extracts movie information 
from unstructured text.

Return ONLY valid JSON.

{format_instructions}
"""
    ),
    ("human", "{paragraph}")
])

# -------------------- UI --------------------
st.title("🎬 Movie Information Extractor")

st.write(
    "Paste any movie description and AI will convert it "
    "into structured structured data using LLMs."
)

st.divider()

# -------------------- Example Input --------------------
example_text = """
Interstellar is a 2014 epic science fiction film directed by Christopher Nolan.
The movie stars Matthew McConaughey, Anne Hathaway, and Jessica Chastain.
It explores space travel, black holes, and survival of humanity.
The film received a rating of 8.7 for its emotional depth and visuals.
"""

if st.button("📌 Load Example"):
    st.session_state["movie_paragraph"] = example_text

# -------------------- Text Area --------------------
paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=220,
    key="movie_paragraph",
    placeholder="Paste movie description here..."
)

# -------------------- Extract Button --------------------
if st.button("🚀 Extract Data"):

    if not paragraph.strip():
        st.warning("⚠️ Please enter a movie paragraph first.")

    else:
        with st.spinner("🔍 Analyzing movie information..."):

            try:
                # Create Prompt
                final_prompt = prompt.invoke({
                    "paragraph": paragraph,
                    "format_instructions": parser.get_format_instructions()
                })

                # LLM Response
                response = model.invoke(final_prompt)

                # Raw Output
                st.subheader("🧠 Raw Model Output")
                st.code(response.content, language="json")

                # Parse Response
                movie_data = parser.parse(response.content)

                # Structured Output
                st.subheader("✅ Structured Output")

                movie_json = movie_data.model_dump()

                st.json(movie_json)

                # -------------------- Download Button --------------------
                st.download_button(
                    label="📥 Download JSON",
                    data=json.dumps(movie_json, indent=4),
                    file_name="movie_data.json",
                    mime="application/json"
                )

                st.success("🎉 Extraction Completed Successfully!")

            except Exception as e:
                st.error(
                    "❌ Failed to parse response. "
                    "The model did not follow the schema correctly."
                )

                st.exception(e)

# -------------------- Footer --------------------
st.divider()

st.caption("⚡ Built with LangChain + Mistral AI + Streamlit")