import argparse
import sys

class FileCounter:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def count_bytes(self, content):
        """Count the number of bytes in content."""
        return len(content)

    def count_lines(self, content):
        """Count the number of lines in content."""
        return len(content.splitlines())

    def count_words(self, content):
        """Count the number of words in content."""
        return len(content.split())

    def count_characters(self, content):
        """Count the number of characters in content."""
        return len(content)

    def count_from_file(self):
        """Count from a file specified by file_path."""
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return ''

    def count_from_stdin(self):
        """Count from standard input."""
        return sys.stdin.read()

def main():
    parser = argparse.ArgumentParser(description="ccwc - Count Bytes, Lines, Words, and Characters in a File")
    parser.add_argument('-c', action='store_true', help='Print byte counts')
    parser.add_argument('-l', action='store_true', help='Print line counts')
    parser.add_argument('-w', action='store_true', help='Print word counts')
    parser.add_argument('-m', action='store_true', help='Print character counts')
    parser.add_argument('file', nargs='?', help='Path to the file for counts. If not specified, read from standard input.')
    args = parser.parse_args()

    file_counter = FileCounter(args.file)

    if args.file:
        content = file_counter.count_from_file()
    else:
        # Read from standard input
        content = file_counter.count_from_stdin()

    byte_count = file_counter.count_bytes(content)
    line_count = file_counter.count_lines(content)
    word_count = file_counter.count_words(content)
    char_count = file_counter.count_characters(content)

    # Default option: equivalent to -c, -l, -w
    if not any([args.c, args.l, args.w, args.m]):
        print(f" {line_count}", end='')
    else:
        if args.c:
            print(f" {byte_count}", end='')
        if args.l:
            print(f" {line_count}", end='')
        if args.w:
            print(f" {word_count}", end='')
        if args.m:
            print(f" {char_count}", end='')

    if args.file:
        print(f" {args.file}")
    else:
        print()

if __name__ == "__main__":
    main()



