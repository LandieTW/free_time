
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]

# Which are the mean number of connections?

for user in users:
    user_id = user['id']

    num_friends = 0
    for friendship in friendships:
        if friendship[0] == user_id or friendship[1] == user_id:
            num_friends += 1
    user['num_friends'] = num_friends

mean_num_connections = sum(user['num_friends'] for user in users) / len(users)
print(f'Mean number of connections: {mean_num_connections}')

# Who are the most connected people?

num_friends_ranking = sorted(users, 
                             key=lambda user: user['num_friends'], 
                             reverse=True)
print('Most connected people:')
for user in num_friends_ranking:
    print(f"  {user['name']} has {user['num_friends']} friends")

# Suggest new friends based on friends of friends

