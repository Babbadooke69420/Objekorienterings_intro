class Car():
   '''
   En klass som håller reda på några egenskaper hos en bil.
   '''
  
   def __init__(self, brand, color, mileage):

      self.brand = brand
      self.color = color
      self.mileage = mileage

   def get_brand(self):
      '''
      Skriver ut bilmärket
      '''
      print(self.brand)

   def set_brand(self, new_brand):
      '''
      Parameter: new_brand | sträng
      Uppdaterar bilmärket om det existerar. Om det inte existerar
      så tilldelas aktuellt objekt märket enligt parametern.
      '''
      self.brand = new_brand


