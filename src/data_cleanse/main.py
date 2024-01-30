import logging

from argparse import ArgumentParser
from pathlib import Path

from src.data_cleanse.models import Person


class AllEmails:
    def __init__(self, root_path: str):
        self.root_path = root_path
        self.root = Path(root_path)
        self.directory: dict[str, Person] = {}
    
    def __repr__(self) -> str:
        return f"AllEmails({self.root_path})"

    def main(self):
        logging.info("Creating")
        for p in self.root.iterdir():
            person = Person(p.name, p)
            person.get_all_emails()
            self.directory[p.name] = person
        logging.info("Book created")


def main(path: str):
    AllEmails(path).main()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--data-path', type=str, required=True)
    args = parser.parse_args()

    main(args.data_path)
