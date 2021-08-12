# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artists(models.Model):
    ArtistId = models.AutoField(primary_key=True)  # Field name made lowercase.
    Name = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'artists'

class Albums(models.Model):
    AlbumId = models.AutoField(primary_key=True)  # Field name made lowercase.
    Title = models.TextField()  # Field name made lowercase. This field type is a guess.
    ArtistId = models.ForeignKey(Artists, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'albums'


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)  # Field name made lowercase.
    LastName = models.TextField()  # Field name made lowercase. This field type is a guess.
    FirstName = models.TextField()  # Field name made lowercase. This field type is a guess.
    Title = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ReportsTo = models.ForeignKey('Employees', on_delete=models.CASCADE)  # Field name made lowercase.
    BirthDate = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    HireDate = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    Address = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    City = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    State = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Country = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    PostalCode = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Phone = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Fax = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Email = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'employees'


class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)  # Field name made lowercase.
    FirstName = models.TextField()  # Field name made lowercase. This field type is a guess.
    LastName = models.TextField()  # Field name made lowercase. This field type is a guess.
    Company = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Address = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    City = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    State = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Country = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Phone = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Fax = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Email = models.TextField()  # Field name made lowercase. This field type is a guess.
    SupportRepId = models.ForeignKey(Employees, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Genres(models.Model):
    GenreId = models.AutoField(primary_key=True)  # Field name made lowercase.
    Name = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'genres'


class Invoices(models.Model):
    InvoiceId = models.AutoField(primary_key=True)  # Field name made lowercase.
    CustomerId = models.ForeignKey(Customers, on_delete=models.CASCADE)  # Field name made lowercase.
    InvoiceDate = models.DateTimeField()  # Field name made lowercase.
    BillingAddress = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    BillingCity = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    BillingState = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    BillingCountry = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    BillingPostalCode = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Total = models.TextField()  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'invoices'


class MediaTypes(models.Model):
    MediaTypeId = models.AutoField(primary_key=True)  # Field name made lowercase.
    Name = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mediatypes'


class Playlists(models.Model):
    PlaylistId = models.AutoField(primary_key=True)  # Field name made lowercase.
    Name = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'playlists'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlitestat1'


class Tracks(models.Model):
    TrackId = models.AutoField(primary_key=True)  # Field name made lowercase.
    Name = models.TextField()  # Field name made lowercase. This field type is a guess.
    AlbumId = models.ForeignKey(Albums, on_delete=models.CASCADE)  # Field name made lowercase.
    MediaTypeId = models.ForeignKey(MediaTypes, on_delete=models.CASCADE)  # Field name made lowercase.
    GenreId = models.ForeignKey(Genres, on_delete=models.CASCADE)  # Field name made lowercase.
    Composer = models.TextField(blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Milliseconds = models.IntegerField()  # Field name made lowercase.
    Bytes = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    UnitPrice = models.TextField()  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tracks'


class PlaylistTrack(models.Model):
    PlaylistId = models.ForeignKey(Playlists, on_delete=models.CASCADE)  # Field name made lowercase.
    TrackId = models.ForeignKey(Tracks, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playlisttrack'


class InvoiceItems(models.Model):
    InvoiceLineId = models.AutoField(primary_key=True)  # Field name made lowercase.
    InvoiceId = models.ForeignKey(Invoices, on_delete=models.CASCADE)  # Field name made lowercase.
    TrackId = models.ForeignKey(Tracks, on_delete=models.CASCADE)  # Field name made lowercase.
    UnitPrice = models.TextField()  # Field name made lowercase. This field type is a guess.
    Quantity = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoiceitems'