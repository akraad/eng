import nltk
from nltk.corpus import wordnet as wn
import os

# دانلود منابع لازم
nltk.download("wordnet")
nltk.download("omw-1.4")

def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            name = lemma.name().replace('_', ' ')
            if name.lower() != word.lower():
                synonyms.add(name)
            for ant in lemma.antonyms():
                ant_name = ant.name().replace('_', ' ')
                if ant_name.lower() != word.lower():
                    antonyms.add(ant_name)
    return sorted(synonyms), sorted(antonyms)

def format_entry(word, syns, ants):
    syn_line = "* Synonyms: " + (", ".join(syns) if syns else "—")
    ant_line = "* Antonyms: " + (", ".join(ants) if ants else "—")
    return f"{word}\n{syn_line}\n{ant_line}\n"

def main(input_file="words.txt", output_file="synonyms_antonyms_output.txt"):
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]

    results = []
    for word in words:
        syns, ants = get_synonyms_antonyms(word)
        results.append(format_entry(word, syns, ants))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(results))

    print(f"✅ Done! Output saved to '{output_file}'.")

if __name__ == "__main__":
    main()
