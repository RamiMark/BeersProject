from django.db import models


class Beer(models.Model):
    brand = models.CharField(max_length=30)
    parent_id = models.IntegerField() # for main brands it is empty, for sub_brand it's brand's primary key
    sub_brand = models.CharField(max_length=30)
    bottle_barrel = models.CharField(max_length=30)
    alc = models.DecimalField(max_digits=5,decimal_places=2)  # in % 5%,4.5% ...                                                                              
   # characters = models.CharField(max_length=2, choices)
    country = models.CharField(max_length=30)
    website = models.URLField()

    def __unicode__(self):
        return u'%s %s %s' % (self.brand,self.sub_brand,self.bottle_barrel)

class Places(models.Model):

    RE='RESTAURANT'
    PU='PUB'
    RP='RESTAURANT_PUB'
    CA='CAFFE'
    OT='OTHER'
    
    PLACE_TYPE_CHOICES=((RE,'Restaurant'),(PU,'Pub'),(RP,'Restaurant-Pub'),(CA,'Caffe'),(OT,'Other'))
    
    name = models.CharField(max_length=30)
    place_type = models.CharField(max_length=30, choices=PLACE_TYPE_CHOICES) #rest/pub/rest-pub/caffe/other
    address = models.CharField(max_length=50)
    city = models.CharField (max_length=30)
    phone = models.CharField(max_length=30)
    hours = models.CharField(max_length=20)  #till last customer will be,e.g "21-last"
    kosher_sabbath = models.NullBooleanField()
    website = models.URLField()
    beers = models.ManyToManyField(Beer)

    def __unicode__(self):
            return self.name
