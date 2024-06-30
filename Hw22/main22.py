from peewee import *

"""1"""
class Artist(Model):
    '''клас-модель який реалізує таблицю Artist'''

    ArtistId = AutoField(primary_key= True)
    Name = CharField(max_length=120)

    def __str__(self)->str:
        ''''''
        return f'{self.ArtistId} {self.Name}'

    __repr__ = __str__

    class Meta:
        # https://docs.pee  wee-orm.com/en/latest/peewee/models.html#model-options-and-table-metadata
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Artist'


class Album(Model):
    '''клас-модель який реалізує таблицю Album'''
    AlbumId = AutoField(primary_key=True)
    Title = CharField(max_length=160, null=False)
    ArtistId = IntegerField(null=False)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Album'

class Customer(Model):
    '''клас-модель який реалізує таблицю Customer'''
    CustomerId = AutoField(primary_key= True)
    FirstName = CharField(max_length=40, null=False)
    LastName = CharField(max_length=20, null=False)
    Company = CharField(max_length=80)
    Address = CharField(max_length=70)
    City = CharField(max_length=40)
    State = CharField(max_length=40)
    Country = CharField(max_length=40)
    PostalCode = CharField(max_length=10)
    Phone = CharField(max_length=24)
    Fax = CharField(max_length=24, null=False)
    Email = CharField(max_length=60, null=False)
    SupportId = IntegerField()
    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Customer'

class Employee(Model):
    '''клас-модель який реалізує таблицю Employee'''
    EmployeeId = AutoField(primary_key= True)
    LastName = CharField(max_length=20, null=False)
    FirstName = CharField(max_length=29, null=False)
    Titlle = CharField(max_length=30)
    ReportsTo = IntegerField(null=True)
    BirthDate = DateTimeField()
    HireDate = DateTimeField()
    Address = CharField(max_length=70)
    City = CharField(max_length=40)
    State = CharField(max_length=40)
    Country = CharField(max_length=40)
    PostalCode = CharField(max_length=10)
    Phone = CharField(max_length=24)
    Fax = CharField(max_length=24)
    Email = CharField(max_length=60)
    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Employee'


class Genre(Model):
    '''клас-модель який реалізує таблицю Genre'''
    
    GenreId = AutoField(primary_key=True)
    Name = CharField(max_length=120)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Genre'


class Images(Model):
    '''клас-модель який реалізує таблицю Images'''
    images_id = IntegerField()
    Genre = TextField(null=True)
    Image = BlobField(null=False)
    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Images'


class Invoice(Model):
    '''клас-модель який реалізує таблицю Invoice'''
    InvoiceId = AutoField(primary_key= True)
    CustomerId = IntegerField(null=False)
    InvoiceDate = DateTimeField(null=False)
    BillingCity = CharField(max_length=40)
    BillingState = CharField(max_length=40)
    BillingCountry = CharField(max_length=40)
    BillingPostalCode = CharField(max_length=10)
    Total = FloatField(null=False)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Invoice'


class InvoiceLine(Model):
    '''клас-модель який реалізує таблицю InvoiceLine'''
    InvoiceLineId = AutoField(primary_key= True)
    InvoiceId = IntegerField(null=False)
    TrackId = IntegerField(null=False)
    UntilPrice = FloatField(null=False)
    Quantity = IntegerField(null=False)
    BillingCountry = CharField(max_length=40)
    BillingPostalCode = CharField(max_length=10)
    Total = FloatField(null=False)
    
    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'InvoiceLine'


class MediaType(Model):
    '''клас-модель який реалізує таблицю MediaType'''

    MediaTypeId = AutoField(primary_key= True)
    Name = CharField(max_length=120)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'MediaType'


class Playlist(Model):
    '''клас-модель який реалізує таблицю Playlist'''
    PlaylistId = AutoField(primary_key= True)
    Name = CharField(max_length=120)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Playlist'


class PlaylistTrack(Model):
    '''клас-модель який реалізує таблицю PlaylistTrack'''
    PlaylistId = AutoField(primary_key= True)
    TrackId = IntegerField(null=False)

    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'PlaylistTrack'


class Track(Model):
    '''клас-модель який реалізує таблицю Track'''

    TrackId = AutoField(primary_key= True)
    Name = CharField(max_length=200, null=False)
    AlbumId = IntegerField()
    MediaTypeId = IntegerField(null=False)
    GenreId = IntegerField()
    Composer = CharField(max_length=220)
    Milliseconds = IntegerField(null=False)
    Bytes = IntegerField()
    UnitPrice = FloatField(null=False)


    class Meta:
        database = SqliteDatabase('Chinook_Sqlite.sqlite')
        table_name = 'Track'

"""2"""

name = Genre.select().where(Genre.Name.length() > 8)
name_diict = {g.GenreId: g.Name for g in name}
print(name_diict, sep='\n')

"""3"""

albums = Album.select(Album.Title)

albumTitle = [album.Title for album in albums]
print(albumTitle)
