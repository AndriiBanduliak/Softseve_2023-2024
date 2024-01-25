# Linguist Application

## Overview
In this assignment, you will be creating a Linguist application that aims to facilitate the language learning process. The application will allow users to create decks of flashcards, each containing a word in English and its translation in Ukrainian, along with a tip to help them remember it.

You will create three models: User, Deck, and Card, along with functions to support basic CRUD (Create, Read, Update, Delete) functionality.

## Models

### User
- id (integer)
- name (string)
- email (string)
- password (string)

### Deck
- id (integer)
- name (string)
- user_id (integer)

### Card
- id (integer)
- user_id (integer)
- word (string, English)
- translation (string, Ukrainian)
- tip (string)

## Functions

### User
- `user_create(name, email, password) -> User`: Creates a new user and returns the User object.
- `user_get_by_id(user_id) -> User`: Retrieves a user by their ID and returns the User object.
- `user_update_name(user_id, name) -> User`: Updates the name of a user and returns the User object.
- `user_change_password(user_id, old_password, new_password) -> bool`: Changes the password of a user and returns a Boolean value indicating success or failure.
- `user_delete_by_id(user_id) -> bool`: Deletes a user by their ID and returns a Boolean value indicating success or failure.

### Deck
- `deck_create(name, user_id) -> Deck`: Creates a new deck belonging to a user and returns the Deck object.
- `deck_get_by_id(deck_id) -> Deck`: Retrieves a deck by its ID and returns the Deck object.
- `deck_update(deck_id, name) -> Deck`: Updates the name of a deck and returns the Deck object.
- `deck_delete_by_id(deck_id) -> bool`: Deletes a deck by its ID and returns a Boolean value indicating success or failure.

### Card
- `card_create(user_id, word, translation, tip) -> Card`: Creates a new flashcard and returns the Card object.
- `card_get_by_id(card_id) -> Card`: Retrieves a flashcard by its ID and returns the Card object.
- `card_filter(sub_word) -> tuple[Card]`: Retrieves all flashcards containing a substring in either the word, translation, or tip fields and returns a tuple of Card objects.
- `card_update(card_id, word=None, translation=None, tip=None) -> Card`: Updates the fields of a flashcard and returns the Card object.
- `card_delete_by_id(card_id) -> bool`: Deletes a flashcard by its ID and returns a Boolean value indicating success or failure.

## Instructions
1. Set up a new Python project and create a file named `linguist.py`.
2. Define the User, Deck, and Card models with the appropriate fields.
3. Implement each of the functions listed in the Functions section of this assignment. Use Python docstrings to document each function.
4. Test your functions by writing a separate script that creates users, decks, and flashcards, and performs various CRUD operations. Use Python's assert statement to verify that the expected values are returned by each function.
5. Make any necessary revisions to your implementation based on the results of your testing.
