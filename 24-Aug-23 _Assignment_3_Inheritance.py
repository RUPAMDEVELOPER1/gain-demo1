3>24-Aug-23 
Assignment 3
Inheritance

class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_author(self):
        return f"Author: {self.name} ({self.email})"


class Publication:
    def __init__(self, title, date):
        self.title = title
        self.date = date
    
    def get_date(self):
        return f"Date: {self.date}"
    
    def get_title(self):
        return f"Title: {self.title}"


class Book(Author, Publication):
    def __init__(self, name, email, title, date):
        Author.__init__(self, name, email)
        Publication.__init__(self, title, date)


class Email(Author, Publication):
    def __init__(self, name, email, title, date, subject, to):
        Author.__init__(self, name, email)
        Publication.__init__(self, title, date)
        self.subject = subject
        self.to = to
    
    def get_subject(self):
        return f"Subject: {self.subject}"
    
    def get_to(self):
        return f"To: {self.to}"


# Example usage
book = Book("John Doe", "john@example.com", "The Python Guide", "2023-08-28")
email = Email("Jane Smith", "jane@example.com", "Important Announcement", "2023-08-29", "Meeting details", "team@example.com")

print(book.get_author())
print(book.get_date())
print(book.get_title())

print(email.get_author())
print(email.get_date())
print(email.get_title())
print(email.get_subject())
print(email.get_to())
