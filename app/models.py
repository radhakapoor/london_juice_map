from app import db
from sqlalchemy import Column, Integer, String


class Neighbourhood(db.Model):
	__tablename__='neighbourhood'
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String)
	url = db.Column(String)
	lat = db.Column(Integer)
	lng = db.Column(Integer)
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
	__juicebar__='juicebar'
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String)
	url = db.Column(String)
	address = db.Column(String)
	website = db.Column(String)
	phone_number = db.Column(String)
	instagram_tag = db.Column(String)
	neighbourhood = db.Column(String)

	def __init__(self, name, url, address, website, phone_number, instagram_tag, neighbourhood):
		self.name = name
		self.url = url
		self.address = address
		self.website = website
		self.phone_number = phone_number
		self.instagram_tag = instagram_tag
		self.neighbourhood = neighbourhood

	def __repr__(self):
		return '<Juicebar name is {}, url is {}, address is {}, website is {}, phone_number is {}, instagram tag is {}, is in the neighbourhood of {}'.format(self.name, self.url, self.address, self.website, self.phone_number, self.instagram_tag, self.neighbourhood)

