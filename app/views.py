import json
import urllib2
from flask import render_template, url_for, request, session
from app import app, db
from models import Neighbourhood, Juicebar
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask.ext.basicauth import BasicAuth
from auth import username, password

#engine = 'postgresql+psycopg2://rkapoor:sham22@localhost/londonjuicebars_app'
#app.config['SQLALCHEMY_DATABASE_URI'] = engine
engine = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = engine

Session = sessionmaker(bind=engine)
session = Session()

app.secret_key = 'meangreens'

app.config['BASIC_AUTH_USERNAME'] = username
app.config['BASIC_AUTH_PASSWORD'] = password

basic_auth = BasicAuth(app)

def neigbourhood_url_from_neighbourhood_name(name):
	name = name.replace(" ","")
	lowercase_name = name.lower()
	return lowercase_name 

app.jinja_env.globals.update(n_url=neigbourhood_url_from_neighbourhood_name)


@app.route('/')
def index():
	bars_list = []
	bars=Juicebar.query.all()
	for bar in bars:
		bars_t = (bar.name, float(bar.lat), float(bar.lng), bar.address, bar.url, bar.phone_number)
		bars_list.append(bars_t)	
	return render_template("index.html", juicebars = json.dumps(bars_list))

@app.route('/about/')
def about():
	return render_template("about.html")

@app.route('/contact/')
def contact():
	return render_template("contact.html")

@app.route('/neighbourhoods/<url>/')
def neighbourhood_update(url):
	hood=Neighbourhood.query.filter_by(url=url).first()
	spots=Juicebar.query.filter(Juicebar.neighbourhood==hood.name)
	bars_list = []
	bars=Juicebar.query.all()
	for bar in bars:
		bars_t = (bar.name, float(bar.lat), float(bar.lng), bar.address, bar.url, bar.phone_number)
		bars_list.append(bars_t)
	lat=float(hood.lat)
	lng=float(hood.lng)
	zoom=hood.zoom	
	return render_template("neighbourhood_update.html", hood=hood, spots=spots, juicebars = json.dumps(bars_list), lat=json.dumps(lat), lng=json.dumps(lng), zoom=json.dumps(zoom))

def get_foursquare_data(vendor_id):
	api_url = 'https://api.foursquare.com/v2/venues/' + vendor_id + '?client_id=BDGPT1B5ZSK032UES4QHJLB3QO405NVRBJWHKHVIV0DGVPHZ&client_secret=VNG1KZDACS1EBMLJAHKHVFLNXIQYB22DPCV1EQGS0BY25IEK&v=20140905'
	print api_url 
	return api_url

@app.route('/juicebar/<url>')
def juicebar_update(url):	
	spot=Juicebar.query.filter_by(url=url).first()		
	instagram_tag=spot.instagram_tag
	tips_l = []
	opening_d={}
	status=""
	hours=""
	if not spot.foursquare is None:
		foursquare_url = get_foursquare_data(spot.foursquare)
		foursquare_open = urllib2.urlopen(foursquare_url)
		foursquare_data = json.load(foursquare_open)
		all_tips = foursquare_data['response']['venue']['tips']['groups'][0]['items']		
		for all_tip in all_tips:
			tip = all_tip['text']
			tips_l.append(tip)			
		try:
			foursquare_data['response']['venue']['hours']['status']		
			status = foursquare_data['response']['venue']['hours']['status']		
			hours = foursquare_data['response']['venue']['hours']['timeframes']		
			for hour in hours:
				opening_days = hour['days']				
				opening_hours = hour['open'][0]['renderedTime']
				opening_d[opening_days] = opening_hours
		except KeyError:
			print 'Foursquare API problem'								
	return render_template("juicebar_update.html", spot=spot, instagram_tag=json.dumps(instagram_tag), tips_l=tips_l, status=status, opening_d=opening_d) 

@app.route('/addneighbourhood/', methods=['GET'])
@basic_auth.required
def get_neighbourhood():
	neighbourhoods=Neighbourhood.query.all()
	return render_template("add_neighbourhood.html", neighbourhoods=neighbourhoods)

@app.route('/addneighbourhood/', methods=['POST'])
@basic_auth.required
def post_neighbourhood():
	name=request.form['name']
	url=request.form['url']
	lat = request.form['lat']
	lng = request.form['lng']	
	zoom = request.form['zoom']	
	neighbourhood=Neighbourhood(name=name, url=url, lat=lat, lng=lng, zoom=zoom)	
	db.session.add(neighbourhood)
	db.session.commit()
	return render_template("neighbourhood_submitted.html", name=name, url=url, lat=lat, lng=lng, zoom=zoom)

@app.route('/addjuicebar/', methods=['GET'])
@basic_auth.required
def get_juicebar():
	bars=Juicebar.query.all()
	return render_template("add_juicebar.html", bars=bars)

@app.route('/addjuicebar/', methods=['POST'])
@basic_auth.required
def post_juicebar():
	name=request.form['name']
	url=request.form['url']
	lat = request.form['lat']
	lng = request.form['lng']
	address=request.form['address']
	website=request.form['website']
	phone_number=request.form['phone_number']
	instagram_tag=request.form['instagram_tag']
	foursquare_id = request.form['foursquare']
	neighbourhood=request.form['neighbourhood']	
	bar=Juicebar(name=name, url=url, lat=lat, lng=lng, address=address, website=website, phone_number=phone_number, instagram_tag=instagram_tag, foursquare=foursquare_id, neighbourhood=neighbourhood)	
	db.session.add(bar)
	db.session.commit()
	return render_template("juicebars_submitted.html", name=name, url=url, lat=lat, lng=lng, address=address, website=website, phone_number=phone_number, instagram_tag=instagram_tag, foursquare=foursquare_id, neighbourhood=neighbourhood)


