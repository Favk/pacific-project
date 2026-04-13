def search_documents(query, documents):
    query_words = query.lower().split()
    results = []

    for doc in documents:
        content = doc["content"].lower()
        title = doc["title"].lower()

        score = sum(word in content or word in title for word in query_words)

        if score > 0:
            doc["score"] = score
            results.append(doc)

    results.sort(key=lambda x: x["score"], reverse=True)
    return results