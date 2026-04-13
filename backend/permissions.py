def filter_by_permission(role, docs):
    if role == "admin":
        return docs

    return [doc for doc in docs if doc["role"] == role]