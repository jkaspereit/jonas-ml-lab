import sys
import nltk
import pandas as pd

# Make sure punkt tokenizer is available
nltk.download('punkt', quiet=True)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <book.txt>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read the book file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Split text into sentences
    sentences = nltk.sent_tokenize(text)

    # Create DataFrame
    df = pd.DataFrame(sentences, columns=["sentence"])

    # Create output file name
    output_file = input_file.rsplit(".", 1)[0] + "_sentences.csv"

    # Save to CSV
    df.to_csv(output_file, index=False)

    print(f"Saved {len(df)} sentences to {output_file}")

if __name__ == "__main__":
    main()