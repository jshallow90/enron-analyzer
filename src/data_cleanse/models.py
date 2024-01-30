from pathlib import Path

class Email:
    def __init__(self, path: Path):
        self.path = path
    
    def __repr__(self) -> str:
        return f"Email({self.path})"


class Person:
    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path
        self.emails: dict[str, list[Email]] = {}
    
    def __repr__(self) -> str:
        return f"Person({self.name}, {self.path})"
    
    def get_all_emails(self):
        for path in self.path.iterdir():
            if path.is_file():
                email = Email(path)
                self.append_emails('all', email)
            else:
                for email_path in path.iterdir():
                    email = Email(email_path)
                    self.append_emails(path.name, email)
    
    def append_emails(self, folder: str, email: Email):
        self.emails[folder] = self.emails.get(folder, []) + [email]
