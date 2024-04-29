from flask_bcrypt import Bcrypt
from app import app
from models import db, Book, Review

bcrypt = Bcrypt(app)

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        Book.query.delete()
        Review.query.delete()


        print("Seeding book...")
        books = [
            Book(title="The 48 laws of power", author="Robert Greene", year='1998', description='The 48 Laws of Power is a self-help book by the American author Robert Greene. This book is a New York Times bestseller, selling over 1.2 million copies in the United States.'),
            Book(title="The Alchemist", author="Paulo Coelho", year='1988', description='The Alchemist is a novel by Brazilian author Paulo Coelho that was first published in 1988. Originally written in Portuguese, it was widely translated to become an international bestseller.'),
            Book(title="Harry Potter", author="Jk.Rowling", year='1997', description='The first novel in the Harry Potter series and Rowlings debut novel, it follows Harry Potter, a young wizard who discovers his magical heritage on his eleventh birthday, when he receives a letter of acceptance to Hogwarts School of Witchcraft and Wizardry. Harry makes close friends and a few enemies during his first year at the school and with the help of his friends, Ron Weasley and Hermione Granger, he faces an attempted comeback by the dark wizard Lord Voldemort, who killed Harrys parents, but failed to kill Harry when he was just 15 months old.'),
            Book(title="Pepper pig", author="Hasbro Entertainment", year='2004', description='the show follows Peppa, an anthropomorphic female piglet, and her family, as well as her peers portrayed as other animals.')
        ]

        db.session.add_all(books)
        db.session.commit()    
        print("Done seeding!")