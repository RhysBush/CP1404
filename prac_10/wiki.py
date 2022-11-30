"""
Wikipedia's coolness!
-Rhys Bush, 30/11/2022
"""
import wikipedia
INPUT_PROMPT = "Input a wikipedia article name: "


def main():
    page_name = input(INPUT_PROMPT)
    while page_name != "":
        try:
            page = wikipedia.page(page_name)
            print(wikipedia.page(title=page_name, auto_suggest=False))
            print(wikipedia.summary(page_name))
            print(page.url)
        except wikipedia.exceptions.DisambiguationError:
            print(f"Your input, {page_name}, could be interpreted as other articles.\n"
                  f"Please try again.")
        page_name = input(INPUT_PROMPT)


main()
