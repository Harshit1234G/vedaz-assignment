"""
1. Research Task (Non-Coding | 1-2 Pages PDF)

You are asked to build an LLM-based smart recommendation engine for Vedaz that analyzes user chat history and profile to recommend astrologers.

1. What LLM stack (OpenAI / Hugging Face / open-source like LLaMA) would you recommend and why?

2.How would you host and scale it (cloud provider, deployment options)?

3. Estimate the monthly cost for hosting a production-level LLM inference system for 50,000 monthly active users.

4.What privacy/safety concerns would you address?

What it tests:
Research skills, architecture thinking, cost-awareness, ability to communicate ideas clearly.

2. Technical Task (Coding | 4-5 hours)

Build a mini recommendation engine that takes user inputs (e.g. chat transcript or a mock profile) and returns top 3 astrologers using semantic matching (embeddings, keyword ranking, or fine-tuned model).

Expected output:

A simple Python script or Jupyter Notebook

Astrologer data can be mocked (5-10 entries with tags like love, career, marriage, etc.)

Bonus if they use OpenAI embeddings or Sentence Transformers

Should return relevance score and recommended astrologers

What it tests:
Hands-on NLP experience, prompt engineering, semantic search, quick prototyping, and ability to work with real-world user data structure.

3. Bonus : Small LLM Use Case
Prompt:

Write a prompt or small agent logic that behaves like a basic AI astrologer — it should be able to take a palm reading description or horoscope summary and reply with a life insight or advice.
(Use OpenAI, Claude, or open-source LLM, or write pseudocode.)
"""


import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from numpy.typing import NDArray


class AstrologerRecommender:
    def __init__(self) -> None:
        """
        Loads the sentence transformer and datasets.
        """
        # loading sentence transformer
        self.transformer = SentenceTransformer('all-MiniLM-L6-v2')

        # loading astrologer and user data
        self.astrologers = self.load_data(r'data/astrologers.json')
        self.users = self.load_data(r'data/users.json')

        # getting astrologer embeddings
        self.astrologer_bios = self.get_embeddings(self.astrologers, 'bio')


    @staticmethod
    def load_data(path: str) -> list[dict]:
        """Static function to load `.json` files.

        Args:
            path (str): path to the `.json` file

        Returns:
            list[dict]: Loaded `.json` file
        """
        with open(path, 'r') as f:
            data = json.load(f)
        return data


    def get_embeddings(self, json_data: list[dict], key: str) -> NDArray:
        """Extracts the sentences from the `json_data` and encodes them.

        Args:
            json_data (list[dict])
            key (str): key whose values are to be extracted

        Returns:
            NDArray: embedding from the sentence transformer
        """
        sentences = [data[key] for data in json_data]
        return self.transformer.encode(sentences)


    def recommend(self, user_input: str, *, top_k: int = 3) -> list[dict]:
        """Recommend top_k astrologers based on similarity between user_input and astrologer bios.

        Args:
            user_input (str): Recommendations on the basis of this text
            top_k (int, optional): total number of recommendations. Defaults to 3.

        Returns:
            list[dict]
        """
        # generate embedding for the user input text
        user_embeddings = self.transformer.encode([user_input.lower()])

        # compute cosine similarity between user input and all astrologer bios
        similarities = cosine_similarity(user_embeddings, self.astrologer_bios)[0]

        # get indices of top_k most similar astrologer bios
        top_k_indices = np.argsort(similarities)[::-1][:top_k]

        # Prepare the result dictionry for each top match
        recommendations = []

        for idx in top_k_indices:
            astrologer = self.astrologers[idx]
            score = round(float(similarities[idx]), 4)
            astrologer_with_score = {
                'astrologer_id': astrologer['id'],
                'name': astrologer['name'],
                'bio': astrologer['bio'],
                'similarity_score': score
            }
            recommendations.append(astrologer_with_score)

        return recommendations


if __name__ == '__main__':
    recommender = AstrologerRecommender()
    final_results = []

    # iterate over all users and generate top astrologer recommendations
    for user in recommender.users:
        user_id = user['id']
        chat_history = user['chat_history']

        # get top matching astrologers based on user chat history
        top_matches = recommender.recommend(chat_history)

        # Create a result entry for this user
        result_entry = {
            'user_id': user_id,
            'top_matches': top_matches
        }
        final_results.append(result_entry)

    # Save to result.json
    with open('data/result.json', 'w') as f:
        json.dump(final_results, f, indent=2)
