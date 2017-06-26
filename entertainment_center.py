import media
import fresh_tomatoes

#create instances of each movie object
toy_story = media.Movie("Toy Story","A story about a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://youtu.be/NTdKQzVFeis")

avatar = media.Movie("Avatar", "A marine in an alien planet",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://youtu.be/cRdxXPV9GNQ")

august_rush = media.Movie("August Rush","A musically gifted orphan and his adventures in New York",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/August_rush_poster.jpg/220px-August_rush_poster.jpg",
                          "https://youtu.be/N7tl_gvJkQE")

charlie = media.Movie("Charlie and the Chocolate Factory",
                      "When a young boy wins a contest, he goes on the adventure of a lifetime in a chocolate factory",
                      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2PCVjH3ENW3ROhTZRe7U5m_lIpW2MHgi4LxygAxf3UBkqXUJ5G-S3Qg",
                      "https://youtu.be/OFVGCUIXJls")


alcatraz = media.Movie("Escape from Alcatraz", "The infamous of story of the only succesful escape from the island prison Alcatraz",
                       "http://www.gstatic.com/tv/thumb/movieposters/3635/p3635_p_v8_af.jpg",
                       "https://youtu.be/KSS0fH9zzFY")

good_will = media.Movie("Good Will Hunting", "A mathematical genius sturggles to find his purpose" ,
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                        "https://youtu.be/PaZVjZEFkRs")

#create list of movie objects
movies = [toy_story, avatar, august_rush, charlie, alcatraz, good_will]

#pass the list into the open_movies_page function  
fresh_tomatoes.open_movies_page(movies)

