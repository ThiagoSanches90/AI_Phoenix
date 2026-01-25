import os

def read_cv_text(file_path):
    """
    Reads a CV in .txt format and returns its content as a string.
    (Later we can add PDF/DOCX support.)
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CV file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    return content

# Simple test (you can run later)
if __name__ == "__main__":
    print("CV Reader module ready.")
