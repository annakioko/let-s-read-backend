from flask_bcrypt import Bcrypt
from app import app
from models import db, Category, Product, User

bcrypt = Bcrypt(app)

def seed_data():
    # Delete existing data
    Category.query.delete()
    Product.query.delete()
    User.query.delete()

    # user seed
    Users = [
            User(username="Anna Kioko", email="anna@gmail.com", password=bcrypt.generate_password_hash("Annakioko.123").decode('utf-8'),  role='admin'),
            User(username="Sharon Mwende", email="sharon@gmail.com", password=bcrypt.generate_password_hash("Sharonmwende.123").decode('utf-8'),  role='admin'),
            User(username="James Mbuvi", email="james@gmail.com", password=bcrypt.generate_password_hash("Jamesmbuvi.123").decode('utf-8'),  role='user'),
            User(username="Francis Ngigi", email="francis@gmail.com", password=bcrypt.generate_password_hash("francisngigi.123").decode('utf-8'),  role='user'),
            User(username="Ian Kinuthia", email="ian@gmail.com", password=bcrypt.generate_password_hash("Iankinuthia.123").decode('utf-8'),  role='user')
        ]
    db.session.add_all(Users)
    db.session.commit()    
        



    #  categories seed
    category_makeup = Category(name='Makeup')
    category_scents = Category(name='Scents')
    category_skincare = Category(name='Skincare')

    # Add categories to session
    db.session.add_all([category_makeup, category_scents, category_skincare])
    db.session.commit()

    # Create products
    products = [
        # Makeup products
        Product(name='soft matte lip colour', gender='Woman', description=' Luxurious, velvety, long-lasting shades for irresistible lips', price=1000, quantity_available=50, image='https://unsplash.com/photos/beige-becca-lipstick-jaV6cvSEqao', category=category_makeup),
        Product(name='radiant silk', gender='Woman', description='Silky smooth formula for flawless coverage and luminous complexion', price=1500, quantity_available=40, image='https://unsplash.com/photos/two-labeled-bottles-xBqYLnRhfaI', category=category_makeup),
        Product(name='golden glow', gender='Woman', description='Illuminating formula for a radiant, dewy complexion all day', price=500, quantity_available=40, image='https://unsplash.com/photos/white-petaled-flowers-on-top-of-conceleaer-bzBs0_g0lRo', category=category_makeup),

        # Scents products
        Product(name='enchanted elixir', gender='Woman', description='Enchanted Elixir: Captivating blend of florals and musk, evoking timeless elegance', price=4000.99, quantity_available=30, image='https://unsplash.com/photos/two-clear-glass-perfume-bottles-nka_sIQpKEU', category=category_scents),
        Product(name='midnight legend', gender='Man', description='Description for Product 4', price=4500, quantity_available=20, image='https://unsplash.com/photos/calvin-klein-one-perfume-bottle-C1qrJ9i4EPc', category=category_scents),
        Product(name='whispering petals', gender='Woman', description='Delicate floral notes intertwine for an enchanting, feminine aura', price=5000, quantity_available=20, image='https://unsplash.com/photos/pink-and-silver-perfume-bottle-M3PWXjCiRbQ', category=category_scents),

        # Skincare products
        Product(name='i am fabulous', gender='Woman', description='Luxurious body oil, enhances radiance, nourishes, and revitalizes skin', price=1500, quantity_available=10, image='https://unsplash.com/photos/brown-glass-bottle-beside-box-WnVrO-DvxcE', category=category_skincare),
        Product(name='necessarie', gender='Woman', description='Indulgent hydration, leaving skin supple, silky, and irresistibly smooth', price=1000, quantity_available=5, image='https://unsplash.com/photos/white-calvin-klein-soft-tube-p3O5f4u95Lo', category=category_skincare),
        Product(name='because its you', gender='Woman', description='Luxurious hydration, embracing your unique essence with confidence and grace', price='1500', quantity_available='30', image='https://unsplash.com/photos/white-calvin-klein-one-soft-tube-zot788TQRDU', category=category_skincare)
    ]

    # Add products to session
    db.session.add_all(products)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_data()








        #Category.query.delete()
        #Product.query.delete()


        #print("Seeding book...")
       # books = [
           # Book(title="The 48 laws of power", author="Robert Greene", year='1998', description='The 48 Laws of Power is a self-help book by the American author Robert Greene. This book is a New York Times bestseller, selling over 1.2 million copies in the United States.'),
            #Book(title="The Alchemist", author="Paulo Coelho", year='1988', description='The Alchemist is a novel by Brazilian author Paulo Coelho that was first published in 1988. Originally written in Portuguese, it was widely translated to become an international bestseller.'),
           # Book(title="Harry Potter", author="Jk.Rowling", year='1997', description='The first novel in the Harry Potter series and Rowlings debut novel, it follows Harry Potter, a young wizard who discovers his magical heritage on his eleventh birthday, when he receives a letter of acceptance to Hogwarts School of Witchcraft and Wizardry. Harry makes close friends and a few enemies during his first year at the school and with the help of his friends, Ron Weasley and Hermione Granger, he faces an attempted comeback by the dark wizard Lord Voldemort, who killed Harrys parents, but failed to kill Harry when he was just 15 months old.'),
           # Book(title="Pepper pig", author="Hasbro Entertainment", year='2004', description='the show follows Peppa, an anthropomorphic female piglet, and her family, as well as her peers portrayed as other animals.')
      #  ]

        #db.session.add_all(books)
        #db.session.commit()    
        #print("Done seeding!")