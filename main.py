def main():
    buch_path = "books/frankenstein.txt"
    buch = lese_buch(buch_path)
    words = zaehle_woerter(buch)
    print(buch)
    print(f"{words} Wörter gefunden im Dokument")
    zaehle_buchstaben(buch)

def lese_buch(location):
    with open(location) as f:
        return f.read()
    
def zaehle_woerter(text):
    woerter = text.split()
    # nachbesprechung: len(woerter) würde direkt die länge ausgeben
    counter = 0
    for wort in woerter:
        counter += 1
    return counter

def zaehle_buchstaben(text):
    after_convert = text.lower()
    print(after_convert)

if __name__ == "__main__":
    main()