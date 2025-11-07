🎥 YouTube Video Q&A Bot (LLM-Powered)

This project allows users to ask questions about any YouTube video, and the AI model (LLM) answers based on the video’s content.
Just enter a YouTube video URL and your query, and the chatbot will provide an intelligent, context-based response.

🌐 Live Demo: https://yt-rag-chat.streamlit.app/

🚀 Project Overview

This project demonstrates the power of Large Language Models (LLMs) when combined with YouTube video transcription and retrieval.
It extracts the transcript of the video, processes it, and uses a language model to answer user questions accurately.

It’s an exciting showcase of how AI can make video content searchable and interactive — perfect for learners, researchers, or anyone who wants quick insights from long videos.

🧠 Tech Stack

Python 🐍

Streamlit – for interactive UI

LangChain / OpenAI API – for LLM integration

YouTube Transcript API – to fetch video transcripts

Pandas & NumPy – for data handling

Scikit-learn (optional) – for preprocessing or embeddings

⚙️ How It Works

The user provides a YouTube video URL and a question/query.

The app fetches the video transcript using the YouTube API.

The LLM processes the transcript and the query together.

The model returns a context-aware answer based on the video content.

🖥️ Installation & Setup

To run this project locally:

# Clone the repository
git clone YOUR_GITHUB_REPO_LINK_HERE

# Navigate into the project folder
cd YOUR_PROJECT_FOLDER_NAME

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


Then open your browser and go to:
👉 http://localhost:8501/

📸 Live Demo

Try it online without installation!
👉 https://yt-rag-chat.streamlit.app/

🤝 Contributing

Contributions, ideas, and suggestions are always welcome!
Feel free to fork the repository and submit a pull request.

🧾 License

This project is open source and available under the MIT License
.
