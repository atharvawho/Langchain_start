import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-start!")
    print(os.environ.get("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
