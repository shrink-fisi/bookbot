def main():
    buch_path = "books/frankenstein.txt"
    buch = read_text(buch_path)
    words = count_words(buch)
    print(f"{words} Wörter gefunden im Dokument")
    chars = count_chars(buch)
    print(chars)

def read_text(location):
    with open(location) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    # nachbesprechung: len(woerter) würde direkt die länge ausgeben
    counter = 0
    for word in words:
        counter += 1
    return counter

def count_chars(text):
    after_convert = text.lower()
    char_count = {}
    for char in after_convert:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

if __name__ == "__main__":
    main()