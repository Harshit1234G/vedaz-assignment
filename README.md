# 🔮 Astrologer Recommendation Engine

This project implements a **smart recommendation system** that matches users with the most suitable astrologers based on their **chat history** using **semantic similarity** powered by **Sentence Transformers**.

---

## 🚀 Features

* Loads and processes astrologer and user data from JSON files.
* Uses `sentence-transformers` to convert bios and chat history into embeddings.
* Recommends top astrologers for each user using **cosine similarity**.
* Saves structured results into `result.json`.

---

## 🧠 Tech Stack

* **Python 3.10+**
* [SentenceTransformers](https://www.sbert.net/)
* **Scikit-learn**
* **NumPy**
* JSON for data storage

---

## 📁 Project Structure

```
├── data/
│   ├── astrologers.json       # Astrologer profiles with bios
│   ├── users.json             # Users with their chat history
│   └── result.json            # Output file with recommendations
├── README.md
├── research_task.pdf          # Researching task
├── task2.py                   # Main logic and recommendation engine
└── task3.py                   # Prompt Engineering task
```

---

## ⚙️ How It Works

1. **Embedding Generation**
   Astrologer bios and user chat histories are converted into vector embeddings using `all-MiniLM-L6-v2`.

2. **Similarity Calculation**
   Cosine similarity is calculated between user and astrologer vectors.

3. **Recommendation**
   Top 3 astrologers are selected based on similarity score for each user.

4. **Output Format**
   Results are saved as:

```json
[
  {
    "user_id": "chat_01",
    "top_matches": [
      {
        "astrologer_id": 5,
        "name": "Neha Kapoor",
        "bio": "tarot reader and astrologer who helps with decision-making in relationships and daily challenges. offers intuitive forecasts for navigating emotional dilemmas and life paths.",
        "similarity_score": 0.1353
      },
      ...
    ]
  },
  ...
]
```

---


## 📚 Future Improvements

* Use multi-modal embeddings (chat + profile).
* Integrate with a web app or chatbot.
* Add support for feedback and re-ranking.

---

## **📜 License**  

This project is licensed under the **Apache 2.0 License** – see the [LICENSE](https://github.com/Harshit1234G/vedaz-assignment/blob/main/LICENSE) file for details.  

---

## 🙌 Acknowledgements

* [SentenceTransformers](https://www.sbert.net/)
* [Scikit-learn](https://scikit-learn.org/)
* You, for exploring this repo!

---
