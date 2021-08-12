# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artists(models.Model):
    ArtistId = models.AutoField(primary_key=True)  
    Name = models.TextField(blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'artists'

class Albums(models.Model):
    AlbumId = models.AutoField(primary_key=True)  
    Title = models.TextField()   
    ArtistId = models.ForeignKey(Artists, on_delete=models.CASCADE, db_column='ArtistId')  

    class Meta:
        managed = False
        db_table = 'albums'


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)  
    LastName = models.TextField()   
    FirstName = models.TextField()   
    Title = models.TextField(blank=True, null=True)   
    ReportsTo = models.ForeignKey('Employees', on_delete=models.CASCADE, db_column='ReportsTo')  
    BirthDate = models.DateTimeField(blank=True, null=True)  
    HireDate = models.DateTimeField(blank=True, null=True)  
    Address = models.TextField(blank=True, null=True)   
    City = models.TextField(blank=True, null=True)   
    State = models.TextField(blank=True, null=True)   
    Country = models.TextField(blank=True, null=True)   
    PostalCode = models.TextField(blank=True, null=True)   
    Phone = models.TextField(blank=True, null=True)   
    Fax = models.TextField(blank=True, null=True)   
    Email = models.TextField(blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'employees'


class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)  
    FirstName = models.TextField()   
    LastName = models.TextField()   
    Company = models.TextField(blank=True, null=True)   
    Address = models.TextField(blank=True, null=True)   
    City = models.TextField(blank=True, null=True)   
    State = models.TextField(blank=True, null=True)   
    Country = models.TextField(blank=True, null=True)   
    postalcode = models.TextField(blank=True, null=True)   
    Phone = models.TextField(blank=True, null=True)   
    Fax = models.TextField(blank=True, null=True)   
    Email = models.TextField()   
    SupportRepId = models.ForeignKey(Employees, on_delete=models.CASCADE, db_column='SupportRepId')  

    class Meta:
        managed = False
        db_table = 'customers'


class Genres(models.Model):
    GenreId = models.AutoField(primary_key=True)  
    Name = models.TextField(blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'genres'


class Invoices(models.Model):
    InvoiceId = models.AutoField(primary_key=True)  
    CustomerId = models.ForeignKey(Customers, on_delete=models.CASCADE, db_column='CustomerId')  
    InvoiceDate = models.DateTimeField()  
    BillingAddress = models.TextField(blank=True, null=True)   
    BillingCity = models.TextField(blank=True, null=True)   
    BillingState = models.TextField(blank=True, null=True)   
    BillingCountry = models.TextField(blank=True, null=True)   
    BillingPostalCode = models.TextField(blank=True, null=True)   
    Total = models.TextField()   

    class Meta:
        managed = False
        db_table = 'invoices'


class MediaTypes(models.Model):
    MediaTypeId = models.AutoField(primary_key=True)  
    Name = models.TextField(blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'mediatypes'


class Playlists(models.Model):
    PlaylistId = models.AutoField(primary_key=True)  
    Name = models.TextField(blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'playlists'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)
    idx = models.TextField(blank=True, null=True)
    stat = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sqlitestat1'


class Tracks(models.Model):
    TrackId = models.AutoField(primary_key=True)  
    Name = models.TextField()   
    AlbumId = models.ForeignKey(Albums, on_delete=models.CASCADE,db_column='AlbumId')  
    MediaTypeId = models.ForeignKey(MediaTypes, on_delete=models.CASCADE,db_column='MediaTypeId')  
    GenreId = models.ForeignKey(Genres, on_delete=models.CASCADE,db_column='GenreId')  
    Composer = models.TextField(blank=True, null=True)   
    Milliseconds = models.IntegerField()  
    Bytes = models.IntegerField(blank=True, null=True)  
    UnitPrice = models.TextField()   

    class Meta:
        managed = False
        db_table = 'tracks'


class PlaylistTrack(models.Model):
    PlaylistId = models.ForeignKey(Playlists, on_delete=models.CASCADE,db_column='PlaylistId')  
    TrackId = models.ForeignKey(Tracks, on_delete=models.CASCADE,db_column='TrackId')  

    class Meta:
        managed = False
        db_table = 'playlisttrack'


class InvoiceItems(models.Model):
    InvoiceLineId = models.AutoField(primary_key=True)  
    InvoiceId = models.ForeignKey(Invoices, on_delete=models.CASCADE,db_column='InvoiceId')  
    TrackId = models.ForeignKey(Tracks, on_delete=models.CASCADE,db_column='TrackId')  
    UnitPrice = models.TextField()   
    Quantity = models.IntegerField()  

    class Meta:
        managed = False
        db_table = 'invoiceitems'