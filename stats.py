def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        print(content)

def get_book_words_count(filepath):
    with open(filepath) as f:
        content = f.read()
        content_length = len(content.split())
        print(f"Found {content_length} total words")

def count_unique_characters(filepath):
    with open(filepath) as f:
        content = f.read()
        content_lower = content.lower()
        print(content_lower)