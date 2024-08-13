
import re

def main():
    try:
        html_input = input("HTML: ").strip()
        if parse(html_input) is None:
            print("None")
        else:
            print(parse(html_input))
    except Exception as e:
        print(f"An error occurred: {e}")

def parse(s):
    pattern = r'<iframe[^>]*\ssrc="(https?://(?:www\.)?youtube\.com/embed/([^"]+))"[^>]*>'
    if match := re.search(pattern, s):
        video_ID = match.group(2)
        return f"https://youtu.be/{video_ID}"
    else:
        return None



if __name__ == "__main__":
    main()
