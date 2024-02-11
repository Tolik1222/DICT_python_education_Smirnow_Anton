"""The program allows the user to format text using Markdown"""


def display_help():
    print("""
Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done
""")


def format_plain(text):
    return text


def format_bold(text):
    return f"**{text}**"


def format_italic(text):
    return f"*{text}*"


def format_header(level, text):
    return "#" * level + " " + text + "\n"


def format_link(label, url):
    return f"[{label}]({url})"


def format_inline_code(text):
    return f"`{text}`"


"""Functions for formatting text using Markdown"""


def format_ordered_list(text):
    items = text.split("\n")
    formatted_items = [f"{i}. {item}" for i, item in enumerate(items, start=1)]
    return "\n".join(formatted_items) + "\n"


"""takes a string text representing a list of items separated by newlines"""


def format_unordered_list(text):
    items = text.split("\n")
    formatted_items = [f"* {item}" for item in items]
    return "\n".join(formatted_items) + "\n"


"""representing a list of items separated by newlines"""


def main():
    formatted_text = ""
    while True:
        choice = input("Choose a formatter: > ")
        if choice == "!help":
            display_help()
            continue
        elif choice == "!done":
            with open("output.md", "w") as file:
                file.write(formatted_text)
            print("Output has been saved to output.md")
            break

        if choice not in ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
                          "new-line"]:
            print("Unknown formatting type or command")
            continue

        if choice == "header":
            level = int(input("Level: > "))
            if level < 1 or level > 6:
                print("The level should be within the range of 1 to 6.")
                continue
            text = input("Text: > ")
            formatted_text += format_header(level, text)
        elif choice == "link":
            label = input("Label: > ")
            url = input("URL: > ")
            formatted_text += format_link(label, url)
        elif choice == "ordered-list" or choice == "unordered-list":
            num_rows = int(input("Number of rows: > "))
            if num_rows <= 0:
                print("The number of rows should be greater than zero")
                continue
            rows = ""
            for i in range(num_rows):
                rows += input(f"Row #{i + 1}: > ") + "\n"
            if choice == "ordered-list":
                formatted_text += format_ordered_list(rows)
            else:
                formatted_text += format_unordered_list(rows)
        elif choice != "new-line":
            text = input("Text: > ")
            if choice == "plain":
                formatted_text += format_plain(text)
            elif choice == "bold":
                formatted_text += format_bold(text)
            elif choice == "italic":
                formatted_text += format_italic(text)
            elif choice == "inline-code":
                formatted_text += format_inline_code(text)
        else:
            formatted_text += "\n"
            formatted_result = "\n"

        # Appending formatted result to the main formatted text
        formatted_text += formatted_result
        # Appending formatted result to the results of all formatters
        formatted_results += formatted_result


"""acts as the main entry point for the program"""

if __name__ == "__main__":
    main()