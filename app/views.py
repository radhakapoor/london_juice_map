import json
from flask import render_template, url_for
from app import app

juicebars = [('The Juice Well', 51.512845, -0.134020, '4 Peter Street, Soho, London W1F 0DN', 'http://thejuicewell.hk', '+44 20 7439 9399'), ('Roots and Bulbs', 51.517697, -0.151675, '5 Thayer Street, Marylebone, London W1U 3JG', 'http://www.rootsandbulbs.com', ''), ('Juice Tonic Organic Juicery', 51.512152, -0.133273, '3 Winnett Street, Soho, London W1D 6JY', 'http://www.juicetonic.com', '+44 20 7434 3706'), ('Lab Organic', 51.514754, -0.126025, '58 Neal Street, Covent Garden, London WC2H 9PA', 'http://laborganic.co.uk', ''), ('The Good Life Eatery', 51.491950, -0.165379, '59 Sloane Avenue London SW3 3DH', 'http://www.goodlifeeatery.com', '+44 20 7052 9388'), ('Lovage', 51.525744, -0.077237, '100 Shoreditch High Street, London EC 6JQ', 'http://www.acehotel.com/london/lovage', ''), ('Goldies Fresh Projuice', 51.541899, -0.146058, 'The Fitness Mosaic, 81-84 Chalk Farm Road, London, NW1 8AR', 'http://goldiesfreshprojuice.com', ''), ('Raw Press at Wolf & Badger', 51.514122, -0.198761, 'Wolf & Badger, 46 Ledbury Road, London W11 2AB', 'http://www.rawpress.co', ''), ('Elixir Juicery', 51.521371, -0.210583, 'Urban Bliss, 333 Portobello Road, Notting Hill, London W10 5SA', 'http://www.elixirjuicery.com', ''), ('Imbibery London at Mount Street Deli', 51.509753, -0.150542, '100 Mount Street, W1K 2TG', 'http://www.imbiberylondon.com', '+44 20 7499 6843'), ('Imbibery London at The Box Boutique', 51.493665, -0.167818, '104 Draycott Avenue, SW3 3AE', 'http://www.imbiberylondon.com', ''), ('Planet Organic', 51.515546, -0.191101, '42 Westbourne Grove, London W2 5SH', 'http://www.planetorganic.com', '+44 20 7727 2227'), ('Blend & Press', 51.514561, -0.126364, '16a Neal\'s Yard, Covent Garden, London WC2H 9DP', 'http://blendandpress.com', '+44 20 3119 5966'), ('MOJO Juice Bar & Cafe', 51.514745, -0.136000, '8 D\'Arblay Street, W1F 8DP', '+44 20 8001 6520'), ('Juice Club at Maltby Street Food Market', 51.499629, -0.076117, 'Maltby Street, London SE1 3PA'), ('Juice Club at Selfridges', 51.514205, -0.152800, '400 Oxford Street, London W1A 1AB', '', '')]
by_neighbourhood = {'Soho':[('The Juice Well','4 Peter Street, Soho, London W1F 0DN', '+44 20 7439 9399'), ('Juice Tonic Organic Juicery', '3 Winnett Street, Soho, London W1D 6JY', '+44 20 7434 3706'),('MOJO Juice Bar & Cafe','8 D\'Arblay Street, W1F 8DP', '+44 20 8001 6520')],'West End':[('Juice Club at Selfridges','400 Oxford Street, London W1A 1AB')], 'Marylebone':[('Roots and Bulbs','5 Thayer Street, Marylebone, London W1U 3JG', '')], 'Mayfair':[('Imbibery London at Mount Street Deli','100 Mount Street, W1K 2TG', '+44 20 7499 6843')], 'Covent Garden':[('Lab Organic','58 Neal Street, Covent Garden, London WC2H 9PA'),('Blend & Press','16a Neal\'s Yard, Covent Garden, London WC2H 9DP', '+44 20 3119 5966')], 'Chelsea':[('The Good Life Eatery','59 Sloane Avenue London SW3 3DH','+44 20 7052 9388'), ('Imbibery London at The Box Boutique','104 Draycott Avenue, SW3 3AE', '')], 'Shoreditch': [('Lovage','100 Shoreditch High Street, London EC 6JQ')], 'Camden':[('Goldies Fresh Projuice','The Fitness Mosaic, 81-84 Chalk Farm Road, London, NW1 8AR')], 'Notting Hill':[('Raw Press at Wolf & Badger','Wolf & Badger, 46 Ledbury Road, London W11 2AB', ''), ('Elixir Juicery','Urban Bliss, 333 Portobello Road, Notting Hill, London W10 5SA',''), ('Planet Organic','42 Westbourne Grove, London W2 5SH', '+44 20 7727 2227','')],'Tower Bridge':[('Juice Club at Maltby Street Food Market, Maltby Street, London SE1 3PA', '', '', '')]}

@app.route('/')
@app.route('/londonjuicemap')
def index():	
	return render_template("index.html", juicebars = json.dumps(juicebars))

@app.route('/notting hill/')
def notting_hill():	
	neighbourhoods = [('Notting Hill', 51.515095, -0.201228, 15)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['Notting Hill'])

@app.route('/soho/')
def soho():
	neighbourhoods = [('Soho', 51.512845, -0.134020, 16)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['Soho'])

@app.route('/mayfair/')
def mayfair():
	neighbourhoods = [('Mayfair', 51.512413, -0.145555, 16)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['Mayfair'])

@app.route('/marylebone/')
def marylebone():
	neighbourhoods = [('Marylebone', 51.517697, -0.151675, 16)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['Marylebone'])

@app.route('/camden/')
def camden():
	neighbourhoods = [('Camden', 51.5410, -0.1433, 15)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['Camden'])

@app.route('/chelsea/')
def chelsea():
	neighbourhoods = [('Chelsea', 51.485120, -0.174707, 15)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['Chelsea'])

@app.route('/westend/')
def west_end():
	neighbourhoods = [('West End', 51.514310, -0.149700, 16)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['West End'])

@app.route('/towerbridge/')
def tower_bridge():
	neighbourhoods = [('Tower Bridge', 51.504185, -0.076322, 15)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['Tower Bridge'])

@app.route('/shoreditch/')
def shoreditch():
	neighbourhoods = [('Shoreditch', 51.523447, -0.077107, 16)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['Shoreditch'])

@app.route('/coventgarden/')
def covent_garden():
	neighbourhoods = [('Covent Garden', 51.513180, -0.121726, 16)]	
	return render_template("neighbourhood.html", juicebars = json.dumps(juicebars), lat=json.dumps(neighbourhoods[0][1]), lng=json.dumps(neighbourhoods[0][2]), zoom=json.dumps(neighbourhoods[0][3]), neighbourhood_name=neighbourhoods[0][0], by_neighbourhood=by_neighbourhood['Covent Garden'])

