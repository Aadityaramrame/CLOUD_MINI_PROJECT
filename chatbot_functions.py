import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split


class DataProcessor:
    def __init__(self, file_path=None):
        if not file_path:
            # Resolve path relative to this file
            file_path = os.path.join(os.path.dirname(__file__), "cleaned_medquad.csv")
        print(f"📂 Loading data from: {file_path}")

        self.df = pd.read_csv(file_path)
        self.clean_data()
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['question'])

    def clean_data(self):
        print("🧹 Cleaning data...")
        print("🔍 Missing values:\n", self.df.isnull().sum())

        # Remove rows with 'key points' in the answer
        self.df = self.df[~self.df['answer'].str.contains(r'key points', case=False, na=False)]

        # Preprocess question and answer columns
        self.df['question'] = self.df['question'].str.lower().str.strip()
        self.df['answer'] = self.df['answer'].str.lower().str.strip()

        # Group by question to merge duplicate entries
        self.df = self.df.groupby("question", as_index=False).agg({
            "answer": lambda x: " || ".join(x.astype(str)),
            "source": lambda x: ", ".join(x.astype(str).unique())
        })

        # Split into train/test for potential future use
        self.df, self.test_df = train_test_split(self.df, test_size=0.2, random_state=42)
        print("✅ Data cleaned and split.")


class Chatbot:
    def __init__(self, data_processor, similarity_threshold=0.5):
        self.data_processor = data_processor
        self.similarity_threshold = similarity_threshold

    def get_response(self, user_query):
        user_query = user_query.lower().strip()
        user_tfidf = self.data_processor.vectorizer.transform([user_query])
        similarities = cosine_similarity(user_tfidf, self.data_processor.tfidf_matrix)

        best_match_index = similarities.argmax()
        best_score = similarities[0, best_match_index]

        if best_score < self.similarity_threshold:
            return "UNKNOWN", "I'm sorry, I don't have enough information to answer that question.", "N/A"

        best_question = self.data_processor.df.iloc[best_match_index]['question']
        best_answer = self.data_processor.df.iloc[best_match_index]['answer'].replace(" || ", "\n- ")
        source = self.data_processor.df.iloc[best_match_index]['source']

        return best_question, best_answer, source

    def chat(self):
        print("💬 Medical Chatbot is ready! Type 'exit' to stop chatting.")
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() == "exit":
                print("👋 Chatbot: Goodbye! Take care!")
                break
            best_question, response, source = self.get_response(user_input)
            if best_question == "UNKNOWN":
                print(f"\n🤖 Chatbot: {response}")
            else:
                print(f"\n🤖 Chatbot (matched question): {best_question}")
                print(f"💡 Answer: {response}")
                print(f"📚 Source: {source}")

# ✅ Print to confirm successful module load
print("✅ chatbot_function.py loaded successfully")
