import json
from flask import render_template
from app import app

@app.route('/')
@app.route('/londonjuicemap')
def index():
	juicebars = [('The Juice Well', 51.512845, -0.134020, '4 Peter Street, Soho, London W1F 0DN', 'http://thejuicewell.hk', '+44 20 7439 9399'), ('Roots and Bulbs', 51.517697, -0.151675, '5 Thayer Street, Marylebone, London W1U 3JG', 'http://www.rootsandbulbs.com', ''), ('Juice Tonic Organic Juicery', 51.512152, -0.133273, '3 Winnett Street, Soho, London W1D 6JY', 'http://www.juicetonic.com', '+44 20 7434 3706'), ('Lab Organic', 51.514754, -0.126025, '58 Neal Street, Covent Garden, London WC2H 9PA', 'http://laborganic.co.uk', ''), ('The Good Life Eatery', 51.491950, -0.165379, '59 Sloane Avenue London SW3 3DH', 'http://www.goodlifeeatery.com', '+44 20 7052 9388'), ('Lovage', 51.525744, -0.077237, '100 Shoreditch High Street, London EC 6JQ', 'http://www.acehotel.com/london/lovage', ''), ('Goldies Fresh Projuice', 51.541899, -0.146058, 'The Fitness Mosaic, 81-84 Chalk Farm Road, London, NW1 8AR', 'http://goldiesfreshprojuice.com', ''), ('Raw Press at Wolf & Badger', 51.514122, -0.198761, 'Wolf & Badger, 46 Ledbury Road, London W11 2AB', 'http://www.rawpress.co', ''), ('Elixir Juicery', 51.521371, -0.210583, 'Urban Bliss, 333 Portobello Road, Notting Hill, London W10 5SA', 'http://www.elixirjuicery.com', ''), ('Imbibery London at Mount Street Deli', 51.509753, -0.150542, '100 Mount Street, W1K 2TG', 'http://www.imbiberylondon.com', '+44 20 7499 6843'), ('Imbibery London at The Box Boutique', 51.493665, -0.167818, '104 Draycott Avenue, SW3 3AE', 'http://www.imbiberylondon.com', ''), ('Planet Organic', 51.515546, -0.191101, '42 Westbourne Grove, London W2 5SH', 'http://www.planetorganic.com', '+44 20 7727 2227')]
	return render_template("index.html", juicebars = json.dumps(juicebars))

