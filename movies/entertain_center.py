import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story","This is the story about bhai","/home/raghvendra/Downloads/IMG_20140609_165231.jpg","https://www.youtube.com/watch?v=4nwAra0mz_Q")

avatar=media.Movie("AVATAR","This the story about underworld called bhai aka avatar","/home/raghvendra/Downloads/IMG_20130606_202136.jpg","https://www.youtube.com/watch?v=4nwAra0mz_Q")

school_of_bhai=media.Movie("BHAI KA SCHOOL","This the story about Bhai in school","/home/raghvendra/Downloads/IMG_20140605_200101.JPG","https://www.youtube.com/watch?v=4nwAra0mz_Q")

bhai_midnight_ka_badshah=media.Movie("BHAI_MIDNIGHT_BADSHAH","This is the story about king of under world","/home/raghvendra/Downloads/little-kid-smoking.jpg","https://www.youtube.com/watch?v=4nwAra0mz_Q")
underworld_games=media.Movie("UNDERWORLD_GAMES","This is the story about innocent guy who become champaign of underworld","/home/raghvendra/Downloads/little-kid-smoking.jpg","https://www.youtube.com/watch?v=4nwAra0mz_Q")
movies=[toy_story,avatar,school_of_bhai,bhai_midnight_ka_badshah,underworld_games]
fresh_tomatoes.open_movies_page(movies)
#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()