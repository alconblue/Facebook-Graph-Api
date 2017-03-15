import facebook

token = "token"

graph = facebook.GraphAPI(token)

user = "me"

profile = graph.get_object(user)

friends = graph.get_connections(user, "friends")['data']

user_name = profile['name']

friends_names = [friend['name'] for friend in friends]

print friends_names

friends_posts = { friend['name'] : 0 for friend in friends }

posts_tagged_by_others = graph.get_connections(user, "posts", fields='from')['data']

for posts_tagged_by_other in posts_tagged_by_others:
	name = posts_tagged_by_other['from']['name']
	if user_name != name:
		if name in friends_names:
			friends_posts[name]+=1
		else:
			friends_posts[name]=1	 

friends_photos = { friend['name'] : 0 for friend in friends }

photos_tagged_by_others = graph.get_connections(user, "photos", fields='from')['data']

for photos_tagged_by_other in photos_tagged_by_others:
	name = photos_tagged_by_other['from']['name']
	print name
	if user_name != name:
		if name in friends_names:
			friends_photos[name]+=1
		else:
			friends_photos[name]=1
			friends_names.append(name)			
print friends_posts
print friends_photos
