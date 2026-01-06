def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        print(content)

def main():
    get_book_text("./books/frankenstein.txt")

main()
