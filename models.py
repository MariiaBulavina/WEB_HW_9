from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE

connect(db='hw_9', host='mongodb+srv://webuser18:password123456@cluster0.hhynnp6.mongodb.net/')

class Author(Document):
    
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {'collection': 'authors'}


class Quote(Document):

    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=50))
    quote = StringField()
    meta = {'collection': 'quotes'}