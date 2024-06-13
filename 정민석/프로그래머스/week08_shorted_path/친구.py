n = int(input())
friends = [input().strip() for _ in range(n)]


def get_direct_friends(person, n, friends):
    direct_friends = set()
    for other in range(n):
        if friends[person][other] == 'Y':
            direct_friends.add(other)
    return direct_friends

def get_2_friends(person, n, friends):
    direct_friends = get_direct_friends(person, n, friends)
    two_friends = direct_friends.copy()
    for friend in direct_friends:
        friend_of_friend = get_direct_friends(friend, n, friends)
        two_friends.update(friend_of_friend)
    two_friends.discard(person) 
    return len(two_friends)

def find_most_famous_person(n, friends):
    max_2_friends = 0
    for person in range(n):
        max_2_friends = max(max_2_friends, get_2_friends(person, n, friends))
    return max_2_friends

print(find_most_famous_person(n, friends))