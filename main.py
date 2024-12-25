def main():
    buch_path = "books/frankenstein.txt"
    buch = read_text(buch_path)
    words = count_words(buch)
    print(f"--- Beginne Zusammenfassung der Daten von {buch_path} ---")
    print(f"{words} Wörter gefunden im Dokument")
    chars = count_chars(buch)
    sorted_chars = sorted(chars.items(), reverse=True, key=sort_on)
    sort_char_count(sorted_chars)

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

def sort_on(item):
    # wir brauchen den 2. Wert des Tupels (0 = key, 1 = value)
    return(item[1])

def sort_char_count(chars):
    for char,count in chars:
        # if char.isalpha(): 
        # würde auch reichen, da das True impliziert ist
        if char.isalpha() == True:
            print(f"The letter {char} was found {count} times.")

if __name__ == "__main__":
    main()