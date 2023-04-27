from pathlib import Path
from googletrans import Translator


def format_comment(_text: str):
    _text = line.split("#", maxsplit=1)
    _indentation = _text[0]
    _text = _text[1].removesuffix("\n")
    _text = _text.strip()
    return [_indentation, _text]


def translate_formatted_comment(formatted_comment: [[str]]):
    _translated = translator.translate(formatted_comment[1], dest="zh-cn").text
    return f"{formatted_comment[0]}# {_translated}\n"


if __name__ == "__main__":
    test_file = Path("test_files")
    file = test_file / "main.py"
    translator = Translator()

    with open(file, "r") as f:
        data = f.readlines()

    for i, line in enumerate(data):
        if "#" in line:
            line = format_comment(line)
            line = translate_formatted_comment(line)
            data[i] = line

    with open(test_file / "main_translated.py", "w") as new_f:
        new_f.writelines(data)
