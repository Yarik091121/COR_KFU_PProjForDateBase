import re

def main():
    n = input()
    try:
        text = r"(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$"
        if re.match(text, n):
            print("Correct")
        else:
            print("Incorrect")
    except Exception as e:
        print("An Error has occured - ", e)

if __name__=='__main__':
    main()