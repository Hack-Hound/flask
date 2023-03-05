from server_pkg.app import create_app,db
from flask_migrate import upgrade,migrate,init,stamp
from server_pkg.models import User
from server_pkg.app import bcrypt
from sql import DB_Manager
import os

def deploy():
	"""Run deployment tasks."""
	app = create_app()
	app.app_context().push()
	db.create_all()

	# migrate database to latest revision
	init()
	stamp()
	migrate()
	upgrade()
	
deploy()
	


def init_admin():
	email = input("Enter email for admin\t: ")
	pwd = input("Enter password for admin\t: ")
	username = "admin"

	Admin = User(
		username=username,
		email=email,
		pwd=bcrypt.generate_password_hash(pwd)
	)

	db.session.add(Admin)
	db.session.commit()

init_admin()

def init_db():
	DB_Manager().TableCreation()
	arr = [["Red Planet Pizza", 18, "A delicious pizza made with locally grown Martian vegetables, including purple potatoes, roasted radishes, and caramelized onions. Topped with a flavorful tomato sauce and a blend of cheeses."],
["Mars-Made Pasta", 22, "Homemade pasta crafted with locally grown Martian wheat and served with a rich tomato sauce made with herbs grown on the Red Planet. Served with a side of roasted Martian vegetables."],
["Cosmic Cauliflower Steak", 26, "A hearty vegetarian dish featuring a thick slice of cauliflower, seasoned and seared to perfection. Served with a side of roasted potatoes and a tangy sauce made with locally grown herbs."],
["Martian Garden Salad", 14, "A fresh salad made with locally grown Martian vegetables, including purple potatoes, radishes, and carrots. Topped with a tangy vinaigrette made with herbs grown on the Red Planet."],
["Space BBQ Ribs", 28, "Tender pork ribs cooked low and slow, with a tangy BBQ sauce made with locally sourced ingredients. Served with a side of mashed potatoes made with locally grown Martian potatoes."],
["Terra-Formed Tacos", 16, "A trio of tacos made with locally sourced ingredients, including seasoned beef, roasted vegetables, and a spicy salsa made with Martian-grown chili peppers. Served with a side of black beans."],
["Cosmic Crab Cakes", 30, "A delicious seafood dish made with locally sourced crab meat, seasoned and pan-fried to perfection. Served with a side of roasted Martian vegetables and a creamy sauce made with herbs grown on the Red Planet."],
["Interstellar Ice Cream", 10, "Homemade ice cream made with locally sourced Martian cream and infused with unique flavors like chocolate and vanilla bean. Served with a side of locally grown berries."],
["Martian Meatballs", 20, "Juicy meatballs made with locally sourced Martian beef and seasoned with a blend of Martian-grown spices. Served with a side of roasted vegetables."],
["Red Planet Ramen", 24, "A comforting bowl of ramen made with locally sourced ingredients, including handmade noodles and a flavorful broth made with herbs grown on the Red Planet. Topped with roasted vegetables and a soft-boiled egg."],
["Galactic Gnocchi", 18, "Soft, pillowy gnocchi made with locally grown Martian potatoes and served with a creamy sauce made with locally sourced cream and herbs."],
["Martian Mussels", 32, "Fresh, plump mussels sourced from the waters of Mars and served in a flavorful broth made with locally grown herbs and spices. Served with crusty bread for dipping."],
["Solar System Sushi", 28, "An assortment of sushi rolls made with locally sourced seafood and vegetables, including tuna, crab, avocado, and cucumber. Served with soy sauce and wasabi."],
["Martian Mac and Cheese", 16, "A classic comfort food made with locally sourced Martian cheese and topped with breadcrumbs made from locally grown wheat. Served with a side of roasted vegetables."],
["Interplanetary Quesadilla", 14, "A crispy, cheesy quesadilla made with locally sourced ingredients, including Martian-grown peppers and onions. Served with a side of sour cream and salsa."],
["Cosmic Curry", 20, "A flavorful curry made with locally sourced chicken and a blend of Martian-grown spices. Served with a side of rice and naan bread."],
["Martian Margherita", 14, "A classic Margherita pizza made with locally grown Martian tomatoes, fresh basil, and a blend of Martian cheeses."],
["Red Planet Ravioli", 24, "Handmade ravioli stuffed with a flavorful blend of locally sourced Martian vegetables and topped with a tangy tomato sauce."],
["Out of this World Omelette", 12, "A fluffy omelette made with locally sourced Martian eggs and filled with a variety of veggies, including mushrooms, onions, and peppers. Served with a side of roasted potatoes."],
["Martian Meatloaf", 18, "A hearty meatloaf made with locally sourced Martian beef and seasoned with a blend of Martian-grown herbs and spices. Served with a side of roasted vegetables."],
["Mars Barbecue Chicken", 22, "Tender grilled chicken seasoned with a tangy barbecue sauce made with locally sourced ingredients. Served with a side of mashed Martian potatoes."],
["Galactic Gumbo", 26, "A hearty stew made with locally sourced seafood, including shrimp, crab, and mussels, and a flavorful broth made with Martian-grown herbs and spices. Served with crusty bread for dipping."],
["Martian Margarita", 12, "A refreshing cocktail made with locally sourced Martian lime juice and tequila. Served over ice with a salted rim."],
["Solar System Salad", 16, "A fresh salad made with locally sourced Martian greens, including lettuce and arugula, topped with a variety of veggies and a tangy dressing made with Martian-grown herbs."],
["Red Planet Risotto", 22, "A creamy risotto made with locally grown Martian rice and a blend of Martian-grown herbs and spices. Served with a side of roasted vegetables."],
["Cosmic Calamari", 24, "Crispy fried calamari made with locally sourced Martian squid and served with a tangy dipping sauce made with Martian-grown herbs."],
["Martian Margherita Flatbread", 16, "A thin and crispy flatbread topped with locally grown Martian tomatoes, fresh basil, and a blend of Martian cheeses."],
["Interstellar Stir Fry", 20, "A flavorful stir fry made with locally sourced Martian veggies, including carrots, broccoli, and peppers, and served over a bed of rice."],
["Mars-Made Meatballs", 20, "Juicy meatballs made with locally sourced Martian beef and seasoned with a blend of Martian-grown spices. Served with a side of roasted vegetables."],
["Red Planet Red Velvet Cake", 8, "A decadent red velvet cake made with locally sourced Martian eggs and topped with a creamy frosting made with Martian-grown cream."],
["Martian Meat Lover's Pizza", 20, "A savory pizza topped with a variety of locally sourced Martian meats, including beef, pork, and chicken, and a blend of Martian cheeses."],
["Interplanetary Pad Thai", 22, "A classic Pad Thai made with locally sourced ingredients, including rice noodles, shrimp, peanuts, and a tangy sauce made with Martian-grown ingredients."],
["Martian Margarita Flatbread", 16, "A crispy flatbread topped with locally grown Martian tomatoes, fresh basil, and a blend of Martian cheeses."]]
	
	for i in range(len(arr)):
		DB_Manager().AddItem(arr[i][0],arr[i][1],arr[i][2])

init_db()
