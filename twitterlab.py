users = {}            # username -> user info
posts = []            # list of post dictionaries
post_id = 1           # numbering posts for easy reference
option = ''
 

def create_user():
    username = input('Username: ')
    bio = input('Short bio: ')
    users[username] = {
        'bio': bio,
        'followers': 0
    }
    print('User Created: ' + username)
    print('') #empty line to break code, more visable

def write_post():
    global post_id
    username = input('Username: ')
    post_text = input('Write your text here: ')
    post = {
            'id': post_id,
            'user': username,
            'text': post_text,
            'likes': 0
        }
    post_id += 1
    posts.append(post)
    print('Post Created')
    print('') #empty line to break code, more visable
    
def view_feed():
    for i in posts:
        print('Post ID number ' + str(i['id']) + ' by ' + i['user'] + ':')
        print('"' + i['text'] + '"')
        print('Likes: ' + str(i['likes']))
        print('') #empty line to break code, more visable


def like_post():
    global post_id
    like_id = int(input('Enter the post ID number that you want to like: '))
    for i in posts:
        if like_id == i['id']:
            i['likes'] += 1
            break
    print('') #empty line to break code, more visable

def edit_bio():
    username = input('Enter your username to edit your bio: ')

    if username in users:
        updated_bio = input('Type your updated bio here: ')
        users[username]['bio'] = updated_bio
        print('Bio Changed')
        print('') #empty line to break code, more visable
    else:
        print('Not a valid username')
        print('') #empty line to break code, more visable
    

while True:
    print('1. Create a user')
    print('2. Write a post')
    print('3. View the feed')
    print('4. Like a post')
    print('5. Edit bio')
    print('6. Exit')
    print('') #empty line to break code, more visable
    option = input('Type the number in here: ')
    print('') #empty line to break code, more visable
    if option == '1':
        create_user()
    elif option == '2':
        write_post()
    elif option == '3':
        view_feed()
    elif option == '4':
        like_post()
    elif option == '5':
        edit_bio()
    elif option == '6':
        break
