def palindrome(text: str) -> bool:
    """Return True if the text reads the same in both directions."""

    # simpler version - uncomment this line
    # text = text.lower().replace(" ", "").replace(",", "").replace(".", "")

    return text == text[::-1]


if __name__ == "__main__":
    test_texts = ["OTTO", "Python", "Lagerregal"]

    for text in test_texts:
        print(f"{text:<20}: \t{palindrome(text)}")