#TODO: Add the router

def retrieve_relevant_context(vectorstore, message, k=5, threshold=0.2):
    hits = vectorstore.similarity_search_with_relevance_scores(message, k=k)
    relevant_hits = [(doc, sim) for doc, sim in hits if sim >= threshold]
    if not relevant_hits:
        return f"<<<RETRIEVED_CONTEXT>>>\nNO_CONTEXT\n<<<END_RETRIEVED_CONTEXT>>>\n\n<<<STUDENT_QUESTION>>>\n{message}\n<<<END_STUDENT_QUESTION>>>\n"

    content = "<<<RETRIEVED_CONTEXT>>>\n\n"
    for doc, sim in relevant_hits:
        lecture_id = doc.metadata.get("lecture_id", "N/A")
        slide_id = doc.metadata.get("slide_id", "N/A")
        content += (
            f"[Lecture = {lecture_id}] [Slide = {slide_id}]\n\n"
            f"{doc.page_content}\n\n\n"
        )
    content += "<<<END_RETRIEVED_CONTEXT>>>\n\n"
    content += f"<<<STUDENT_QUESTION>>>\n{message}\n<<<END_STUDENT_QUESTION>>>\n"
    return content


def retrieve_relevant_context_mistral(vectorstore, message, k=5, threshold=0.5):
    hits = vectorstore.similarity_search_with_relevance_scores(message, k=k)
    relevant_hits = [(doc, sim) for doc, sim in hits if sim >= threshold]
    if not relevant_hits:
        return f"<<<RETRIEVED_CONTEXT>>>\nNO_CONTEXT\n<<<END_RETRIEVED_CONTEXT>>>\n\n<<<STUDENT_QUESTION>>>\n{message}\n<<<END_STUDENT_QUESTION>>>\n"

    content = "<<<RETRIEVED_CONTEXT>>>\n\n"
    for doc, sim in relevant_hits:
        content += (
            f"{doc.page_content}\n\n\n"
        )
    content += "<<<END_RETRIEVED_CONTEXT>>>\n\n"
    content += f"<<<STUDENT_QUESTION>>>\n{message}\n<<<END_STUDENT_QUESTION>>>\n"
    return content