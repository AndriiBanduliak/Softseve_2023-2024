users = []
decks = []
cards = []

class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

class Deck:
    def __init__(self, id, name, user_id):
        self.id = id
        self.name = name
        self.user_id = user_id

class Card:
    def __init__(self, id, user_id, word, translation, tip):
        self.id = id
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip

def user_create(name, email, password):
    id = len(users) + 1
    user = User(id, name, email, password)
    users.append(user)
    return user

def user_get_by_id(user_id):
    for user in users:
        if user.id == user_id:
            return user

def user_update_name(user_id, name):
    user = user_get_by_id(user_id)
    if user:
        user.name = name
    return user

def user_change_password(user_id, old_password, new_password):
    user = user_get_by_id(user_id)
    if user and user.password == old_password:
        user.password = new_password
        return True
    return False

def user_delete_by_id(user_id):
    global users
    users = [user for user in users if user.id != user_id]
    return not any(user.id == user_id for user in users)

def deck_create(name, user_id):
    id = len(decks) + 1
    deck = Deck(id, name, user_id)
    decks.append(deck)
    return deck

def deck_get_by_id(deck_id):
    for deck in decks:
        if deck.id == deck_id:
            return deck

def deck_update(deck_id, name):
    deck = deck_get_by_id(deck_id)
    if deck:
        deck.name = name
    return deck

def deck_delete_by_id(deck_id):
    global decks
    decks = [deck for deck in decks if deck.id != deck_id]
    return not any(deck.id == deck_id for deck in decks)

def card_create(user_id, word, translation, tip):
    id = len(cards) + 1
    card = Card(id, user_id, word, translation, tip)
    cards.append(card)
    return card

def card_get_by_id(card_id):
    for card in cards:
        if card.id == card_id:
            return card

def card_filter(sub_word):
    return tuple(card for card in cards if sub_word in card.word or sub_word in card.translation or sub_word in card.tip)

def card_update(card_id, word=None, translation=None, tip=None):
    card = card_get_by_id(card_id)
    if card:
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
    return card

def card_delete_by_id(card_id):
    global cards
    cards = [card for card in cards if card.id != card_id]
    return not any(card.id == card_id for card in cards)
