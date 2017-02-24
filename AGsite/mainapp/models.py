from django.db import models

class Architects_supervision(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='some string')
    terms_name = models.CharField(max_length=100)
    terms = models.CharField(max_length=100)
    cost_name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Paragraphs_AS(models.Model):
    paragraph = models.CharField(max_length=300, default='some string')
    language = models.ForeignKey(Architects_supervision, default='1')

    def __str__(self):
        return self.paragraph

class Architecture(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='some string')
    terms_name = models.CharField(max_length=100)
    terms = models.CharField(max_length=100)
    cost_name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    schematic_desing_name =  models.CharField(max_length=100)
    desing_development_name =  models.CharField(max_length=100)
    construction_documents_name =  models.CharField(max_length=100)
    construction_documents_description = models.CharField(max_length=100, default='description')

    def __str__(self):
        return self.name

class Paragraphs_Arch_SD(models.Model):
    paragraph = models.CharField(max_length=300, default='some string')
    language = models.ForeignKey(Architecture, default='1')

    def __str__(self):
        return self.paragraph

class Paragraphs_Arch_DD(models.Model):
    paragraph = models.CharField(max_length=300, default='some string')
    language = models.ForeignKey(Architecture, default='1')

    def __str__(self):
        return self.paragraph

class Paragraphs_Arch_CD(models.Model):
    paragraph = models.CharField(max_length=300, default='some string')
    language = models.ForeignKey(Architecture, default='1')

    def __str__(self):
        return self.paragraph

class Interior_design(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='some string')
    paragraphs_name = models.CharField(max_length=100)
    terms_name = models.CharField(max_length=100)
    terms = models.CharField(max_length=100)
    cost_name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Paragraphs_ID(models.Model):
    paragraph = models.CharField(max_length=300, default='some string')
    language = models.ForeignKey(Interior_design, default='1')

    def __str__(self):
        return self.paragraph

class Product_design(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='some string')
    paragraphs_name = models.CharField(max_length=100)
    terms_name = models.CharField(max_length=100)
    terms = models.CharField(max_length=100)
    cost_name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Paragraphs_PD(models.Model):
    paragraph = models.CharField(max_length=300, default='some string')
    language = models.ForeignKey(Product_design, default='1')
