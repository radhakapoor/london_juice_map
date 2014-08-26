import json
from flask import render_template, url_for, request
from app import app

juicebars = [('The Juice Well', 51.512845, -0.134020, '4 Peter Street, Soho, London W1F 0DN', 'http://thejuicewell.hk', '+44 20 7439 9399'), ('Roots and Bulbs', 51.517697, -0.151675, '5 Thayer Street, Marylebone, London W1U 3JG', 'http://www.rootsandbulbs.com', ''), ('Juice Tonic Organic Juicery', 51.512152, -0.133273, '3 Winnett Street, Soho, London W1D 6JY', 'http://www.juicetonic.com', '+44 20 7434 3706'), ('Lab Organic', 51.514754, -0.126025, '58 Neal Street, Covent Garden, London WC2H 9PA', 'http://laborganic.co.uk', ''), ('The Good Life Eatery', 51.491950, -0.165379, '59 Sloane Avenue London SW3 3DH', 'http://www.goodlifeeatery.com', '+44 20 7052 9388'), ('Lovage', 51.525744, -0.077237, '100 Shoreditch High Street, London EC 6JQ', 'http://www.acehotel.com/london/lovage', ''), ('Goldies Fresh Projuice', 51.541899, -0.146058, 'The Fitness Mosaic, 81-84 Chalk Farm Road, London, NW1 8AR', 'http://goldiesfreshprojuice.com', ''), ('Raw Press at Wolf & Badger Notting Hill', 51.514122, -0.198761, 'Wolf & Badger, 46 Ledbury Road, London W11 2AB', 'http://www.rawpress.co', ''), ('Elixir Juicery', 51.521371, -0.210583, 'Urban Bliss, 333 Portobello Road, Notting Hill, London W10 5SA', 'http://www.elixirjuicery.com', ''), ('Imbibery London at Mount Street Deli', 51.509753, -0.150542, '100 Mount Street, W1K 2TG', 'http://www.imbiberylondon.com', '+44 20 7499 6843'), ('Imbibery London at The Box Boutique', 51.493665, -0.167818, '104 Draycott Avenue, SW3 3AE', 'http://www.imbiberylondon.com', ''), ('Planet Organic', 51.515546, -0.191101, '42 Westbourne Grove, London W2 5SH', 'http://www.planetorganic.com', '+44 20 7727 2227'), ('Blend & Press', 51.514561, -0.126364, '16a Neal\'s Yard, Covent Garden, London WC2H 9DP', 'http://blendandpress.com', '+44 20 3119 5966'), ('MOJO Juice Bar & Cafe', 51.514745, -0.136000, '8 D\'Arblay Street, W1F 8DP', '+44 20 8001 6520'), ('Juice Club at Maltby Street Food Market', 51.499629, -0.076117, 'Maltby Street, London SE1 3PA', 'http://juice-club.co.uk', ''), ('Juice Club at Selfridges', 51.514205, -0.152800, '400 Oxford Street, London W1A 1AB', 'http://juice-club.co.uk', ''), ('Raw Press at Wolf & Badger Mayfair', 51.509038, -0.142922, '32 Dover Street, London, W1S 4NE', 'http://www.rawpress.co', ''), ('Press', 51.510752, -0.134808, '6 Denman Street, Ham Yard Hotel, London W1D 7HD', 'http://press-london.com', '')]

#can delete by_neighbourhood when urls_for confirmed
#by_neighbourhood = {'Soho':[('The Juice Well','4 Peter Street, Soho, London W1F 0DN', '+44 20 7439 9399',''), ('Juice Tonic Organic Juicery', '3 Winnett Street, Soho, London W1D 6JY', '+44 20 7434 3706'),('MOJO Juice Bar & Cafe','8 D\'Arblay Street, W1F 8DP', '+44 20 8001 6520')],'West End':[('Juice Club at Selfridges','400 Oxford Street, London W1A 1AB')], 'Marylebone':[('Roots and Bulbs','5 Thayer Street, Marylebone, London W1U 3JG', '')], 'Mayfair':[('Imbibery London at Mount Street Deli','100 Mount Street, W1K 2TG', '+44 20 7499 6843'), ('Raw Press at Wolf & Badger Mayfair', '32 Dover Street, London, W1S 4NE', '', '')], 'Covent Garden':[('Lab Organic','58 Neal Street, Covent Garden, London WC2H 9PA'),('Blend & Press','16a Neal\'s Yard, Covent Garden, London WC2H 9DP', '+44 20 3119 5966')], 'Chelsea':[('The Good Life Eatery','59 Sloane Avenue London SW3 3DH','+44 20 7052 9388'), ('Imbibery London at The Box Boutique','104 Draycott Avenue, SW3 3AE', '')], 'Shoreditch': [('Lovage','100 Shoreditch High Street, London EC 6JQ')], 'Camden':[('Goldies Fresh Projuice','The Fitness Mosaic, 81-84 Chalk Farm Road, London, NW1 8AR')], 'Notting Hill':[('Raw Press at Wolf & Badger Notting Hill','Wolf & Badger, 46 Ledbury Road, London W11 2AB', ''), ('Elixir Juicery','Urban Bliss, 333 Portobello Road, Notting Hill, London W10 5SA',''), ('Planet Organic','42 Westbourne Grove, London W2 5SH', '+44 20 7727 2227','')],'Tower Bridge':[('Juice Club at Maltby Street Food Market, Maltby Street, London SE1 3PA', '', '', '')]}

@app.route('/')
def index():	
	return render_template("index.html", juicebars = json.dumps(juicebars))

@app.route('/about/')
def about():
	return render_template("about.html")

@app.route('/contact/')
def contact():
	return render_template("contact.html")

by_id = {1:{'neighbourhood_url':'soho' , 'neighbourhood_name':'Soho', 'lat': 51.512845, 'lng':-0.134020, 'zoom': 16, 'bars':[1, 2, 3, 18] }, 			
			2:{'neighbourhood_url': 'nottinghill' , 'neighbourhood_name': 'Notting Hill', 'lat': 51.515095, 'lng': -0.201228, 'zoom': 15, 'bars':[14, 15, 16] },
			3:{'neighbourhood_url': 'mayfair' , 'neighbourhood_name': 'Mayfair', 'lat': 51.512413, 'lng': -0.145555, 'zoom': 16, 'bars':[6,7] },
			4:{'neighbourhood_url': 'marylebone' , 'neighbourhood_name': 'Marylebone', 'lat': 51.517697, 'lng': -0.151675, 'zoom': 16, 'bars':[4] },
			5:{'neighbourhood_url': 'camden' , 'neighbourhood_name': 'Camden', 'lat': 51.5410, 'lng': -0.1433, 'zoom': 15, 'bars':[13] },
			6:{'neighbourhood_url': 'chelsea' , 'neighbourhood_name': 'Chelsea', 'lat': 51.485120, 'lng': -0.174707, 'zoom': 15, 'bars':[10, 11] },
			7:{'neighbourhood_url': 'westend' , 'neighbourhood_name': 'West End', 'lat': 51.514310, 'lng': -0.149700, 'zoom': 16, 'bars':[5] },
			8:{'neighbourhood_url': 'towerbridge' , 'neighbourhood_name': 'Tower Bridge', 'lat': 51.504185, 'lng': -0.076322, 'zoom': 15, 'bars':[17] },
			9:{'neighbourhood_url': 'shoreditch' , 'neighbourhood_name': 'Shoreditch', 'lat': 51.523447, 'lng': -0.077107, 'zoom': 16, 'bars': [12] },
			10:{'neighbourhood_url': 'coventgarden' , 'neighbourhood_name': 'Covent Garden', 'lat': 51.513180, 'lng': -0.121726, 'zoom': 16, 'bars':[8, 9] }
		}
by_name = {1:{'name_url': 'juicetonic', 'name': 'Juice Tonic', 'address': '3 Winnett Street, Soho, London W1D 6JY', 'phone_number': '+44 207 439 9399', 'instagram_tag': 'juicetonic'}, 
			2:{'name_url': 'juicewell', 'name': 'The Juice Well', 'address':'4 Peter Street, Soho, London W1F 0DN', 'phone_number': '+44 20 7439 9399', 'instagram_tag': 'thejuicewell'},
			3:{'name_url': 'mojojuice', 'name': 'MOJO Juice Bar & Cafe', 'address': '8 D\'Arblay Street, W1F 8DP', 'phone_number': '+44 20 8001 6520', 'instagram_tag': 'mojojuice'},
			4:{'name_url': 'rootsandbulbs', 'name': 'Roots and Bulbs', 'address': '5 Thayer Street, Marylebone, London W1U 3JG', 'phone_number': '+44 207 434 3706', 'instagram_tag': 'rootsandbulbs'},
			5:{'name_url': 'juiceclubselfridges', 'name': 'Juice Club at Selfridges', 'address':'400 Oxford Street, London W1A 1AB', 'phone_number': '+44 207 434 3706', 'instagram_tag': 'juiceclublondon'},  
			6:{'name_url': 'mountstreetdeliimbibery', 'name': 'Imbibery London at Mount Street Deli', 'address':'100 Mount Street, W1K 2TG', 'phone_number': '+44 20 7499 6843', 'instagram_tag': 'imbibery'},
			7:{'name_url': 'wolfandbadgerrawpressco', 'name': 'Raw Press at Wolf & Badger Mayfair', 'address': '32 Dover Street, London, W1S 4NE', 'phone_number': '', 'instagram_tag': 'rawpressco'},
			8:{'name_url': 'laborganic', 'name': 'Lab Organic', 'address': '58 Neal Street, Covent Garden, London WC2H 9PA', 'phone_number': '', 'instagram_tag': 'laborganic'},
			9:{'name_url': 'blendandpress', 'name': 'Blend & Press', 'address': '16a Neal\'s Yard, Covent Garden, London WC2H 9DP', 'phone_number': '+44 20 3119 5966', 'instagram_tag': 'blendandpress'},
			10:{'name_url': 'goodlifeeatery', 'name': 'The Good Life Eatery', 'address':'59 Sloane Avenue London SW3 3DH', 'phone_number': '+44 20 7052 9388', 'instagram_tag': 'goodlifeeatery'},
			11:{'name_url': 'boxboutiqueimbibery', 'name': 'Imbibery London at The Box Boutique', 'address': '104 Draycott Avenue, SW3 3AE', 'phone_number':'', 'instagram_tag': 'imbibery'},
			12:{'name_url': 'lovage', 'name': 'Lovage', 'address': '100 Shoreditch High Street, London EC 6JQ', 'phone_number': '', 'instagram_tag': 'wearelovage'},
			13:{'name_url': 'goldiesfreshprojuice', 'name':'Goldies Fresh Projuice', 'address':'The Fitness Mosaic, 81-84 Chalk Farm Road, London, NW1 8AR', 'phone_number':'', 'instagram_tag': 'goldiesfreshprojuice'},
			14:{'name_url': 'wolfandbadgerrawpressco', 'name':'Raw Press at Wolf & Badger Notting Hill','address': '46 Ledbury Road, London W11 2AB', 'phone_number':'', 'instagram_tag':'rawpressco'},
			15:{'name_url': 'elixirjuicery', 'name': 'Elixir Juicery','address': 'Urban Bliss, 333 Portobello Road, Notting Hill, London W10 5SA', 'phone_number':'', 'instagram_tag': 'elixirjuicery'},
			16:{'name_url': 'planetorganic', 'name':'Planet Organic', 'address': '42 Westbourne Grove, London W2 5SH', 'phone_number': '+44 20 7727 2227', 'instagram_tag': 'planetorganic'},
			17:{'name_url': 'juiceclubmaltbystreetmarket', 'name': 'Juice Club at Maltby Street Food Market', 'address': 'Maltby Street, London SE1 3PA', 'phone_number':'', 'instagram_tag': 'juiceclublondon'},
			18:{'name_url': 'press', 'name': 'Press', 'address': '6 Denman Street, Ham Yard Hotel, London W1D 7HD', 'phone_number': '', 'instagram_tag': 'presslondon'}
			}

@app.route('/<int:id>/<neighbourhood>/')
def neighbourhood(id, neighbourhood):	
	j = by_id[id]
	neighbourhood=j['neighbourhood_url']
	latitude = j['lat']
	longitude = j['lng']	
	zoom = j['zoom']		
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(latitude), lng=json.dumps(longitude), zoom=json.dumps(zoom), neighbourhood_name=j['neighbourhood_name'], neighbourhood_bars=j['bars'], by_name=by_name)


@app.route('/addjuicebar/', methods=['GET'])
def get_juicebar():	
	return render_template("add_juicebar2.html")

@app.route('/instagram/')
def instagram():
	return render_template("instagram.html")

@app.route('/addjuicebar/', methods=['POST'])
def post_juicebar():
	name=request.form['name']	
	return render_template("add_juicebar2.html", name=name)

@app.route('/juicebar/<int:id>/<name>')
def juicebar(id, name):	
	j = by_name[id]
	name = j['name_url']
	instagram_tag = j['instagram_tag']	
	return render_template("juicebar.html", name=j['name'], address=j['address'], phone_number=j['phone_number'], instagram_tag=json.dumps(instagram_tag))

# def get_reviews(phone_number):
# 	  params = {
# 	  'phone':phone_number
# 	  #'ywsid': ? 
# 	  } 
# 	  #Obtain these from Yelp's manage access page
# 	  consumer_key = "YOUR_KEY"
# 	  consumer_secret = "YOUR_SECRET"
# 	  token = "YOUR_TOKEN"
# 	  token_secret = "YOUR_TOKEN_SECRET"
	   
# 	  session = rauth.OAuth1Session(
# 	    consumer_key = consumer_key
# 	    ,consumer_secret = consumer_secret
# 	    ,access_token = token
# 	    ,access_token_secret = token_secret)
	     
# 	  request = session.get("http://api.yelp.com/phone_search", params)
	   
# 	  #Transforms the JSON API response into a Python dictionary
# 	  data = request.json()
# 	  session.close()
   	
#   	  return data