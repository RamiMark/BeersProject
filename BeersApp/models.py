from django.db import models

# guy was here.


class Beer(models.Model):
    sort = models.CharField(max_length=30)
    parent_id = models.IntegerField() # for main brands it is empty, for sub_brand it's brand's primary key
    sub_brand = models.CharField(max_length=30)
    bottle_barrell = models.CharField(max_length=30)
    #alc = models.realField()  # in % 5%,4.5% ...                                                                              
    characters = models.CharField(max_length=100)
    country = models.CharField(max_length=30)
    website = models.URLField()

    def __unicode__(self):
        return u'%s %s %s' %(self.brand,self.sub_brand,self.bottle_burrell)

class Places(models.Model):
    RESTAURANT='RE'
    PUB='PU'
    RESTAURANT_PUB='RP'
    CAFFE='CA'
    OTHER='OTH'
    
    #PLACE_TYPE_CHOICES=((RE,Restaurant),(PU,Pub),(RP,Restaurant-Pub),(CA,Caffe),(OTH,Other))
    
    name = models.CharField(max_length=30)
    place_type = models.CharField(max_length=30) #rest/pub/rest-pub/caffe/other
    address = models.CharField(max_length=50)
    city = models.CharField (max_length=30)
    phone = models.CharField(max_length=30)
    hours = models.CharField(max_length=20)
    kosher_sabbath = models.NullBooleanField()
    website = models.URLField()
    beers = models.ManyToManyField(Beer)

    def __unicode__(self):
            return self.name
