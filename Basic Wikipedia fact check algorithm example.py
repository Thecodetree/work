import requests
import re
import difflib
import wikipedia

# Function to clean text
def clean_text(text):
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"\s+", "", text)
    return text.strip()

# Extract keywords - naive demo approach

def extract_keywords(statement):
    words = re.findall(r"\b\w+\b", statement.lower())
    stop_words = set(["the", "is", "at", "which", "on", "and", "a", "an", "to", "in", "of", "for", "with", "by"])
    keywords = [word for word in words if word not in stop_words]
    return keywords
    
def search_wikipedia(keywords):
    query = "" .join(keywords)
    try:
        search_results = wikipedia.search(query)
        if search_results:
            page = wikipedia.page(search_results[0])
            return clean_text(page.summary)
        else:
            return ""
    except Exception as e:
        print("Wikipedia error:", e)
        return ""
    
    def compare_statement(statement, summary):
        ratio = difflib.SequenceMatcher(None, statement.lower(), summary.lower()).ratio()
        return ratio
    
    def fact_check(statement):
        print(f"Extracted Keywords: {keywords}")
        
        summary = search_wikipedia(keywords)
        if not summary:
            print("No reliable data found to fact check.")
            return "Unable to verify due to lack of data."
        print(f"Retrieved Summary: {summary[:300]}...")
        
        similarity = compare_statement(statement, summary)
        print(f"Similarity score: {similarity:.2f}")
        
        if similarity > 0.6:
            return "Likely true"
        elif similarity > 0.3:
            return "Uncertain / Needs human review"
        else:
            return "likely false"
        
    if __name__ == "__man__":
        statement = "The Grand Canyon is located in Las Vegas, Nevada."
        result = fact_check(statement)
        print(f"Fact check result: {result}")