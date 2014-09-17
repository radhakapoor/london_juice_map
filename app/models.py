from app import db
from sqlalchemy import Column, Integer, String, Numeric


class Neighbourhood(db.Model):
	__tablename__='neighbourhood'
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String)
	url = db.Column(String)
	lat = db.Column(Numeric)
	lng = db.Column(Numeric)
	zoom = db.Column(Integer)

	def __init__(self, name, url, lat, lng, zoom):
		self.name = name
		self.url = url
		self.lat = lat
		self.lng = lng
		self.zoom = zoom

	def __repr__(self):
		return '<Neighbourhood name is {}, url is {}, latitude is {}, longitude is {}, zoom is {}'.format(self.name, self.url, self.lat, self.lng, self.zoom)

class Juicebar(db.Model):
	__tablename__='juicebar'
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String)
	url = db.Column(String)
	lat = db.Column(Numeric)
	lng = db.Column(Numeric)
	address = db.Column(String)
	website = db.Column(String)
	phone_number = db.Column(String)
	instagram_tag = db.Column(String)
	neighbourhood = db.Column(String)
	foursquare = db.Column(String)

	def __init__(self, name, url, lat, lng, address, website, phone_number, instagram_tag, neighbourhood, foursquare):
		self.name = name
		self.url = url
		self.lat = lat
		self.lng = lng
		self.address = address
		self.website = website
		self.phone_number = phone_number
		self.instagram_tag = instagram_tag
		self.neighbourhood = neighbourhood
		self.foursquare = foursquare

	def __repr__(self):
		return '<Juicebar name is {}, url is {}, lat is {}, lng is {}, address is {}, website is {}, phone_number is {}, instagram tag is {}, foursquare id is {}, is in the neighbourhood of {}'.format(self.name, self.url, self.lat, self.lng, self.address, self.website, self.phone_number, self.instagram_tag, self.foursquare, self.neighbourhood)

# class Admin(db.Model):
# 	__tablename__='admin'
# 	id = db.Column(Integer, primary_key=True)
# 	name = db.Column(String)
# 	password = db.Column(String)

# 	def __init__(self, name, password):
# 		self.name = name
# 		self.password = password

# 	def __repr__(self):
# 		return '<Admin name is {} and password is {}'.format(self.name, self.password)
