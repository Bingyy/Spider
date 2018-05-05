

```python
# 获取维基百科某页面内容写法，前面已经多次写到了
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html)
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))



```python
for link in bsObj.findAll('a'): # 打印出页面上的所有连接
    if 'href' in link.attrs:
        print(link.attrs['href'])
```

    /wiki/Wikipedia:Protection_policy#semi
    #mw-head
    #p-search
    /wiki/Kevin_Bacon_(disambiguation)
    /wiki/File:Kevin_Bacon_SDCC_2014.jpg
    /wiki/San_Diego_Comic-Con
    /wiki/Philadelphia
    /wiki/Pennsylvania
    /wiki/Kyra_Sedgwick
    /wiki/Sosie_Bacon
    /wiki/Edmund_Bacon_(architect)
    /wiki/Michael_Bacon_(musician)
    http://baconbros.com/
    #cite_note-1
    #cite_note-actor-2
    /wiki/Footloose_(1984_film)
    /wiki/JFK_(film)
    /wiki/A_Few_Good_Men
    /wiki/Apollo_13_(film)
    /wiki/Mystic_River_(film)
    /wiki/Sleepers
    /wiki/The_Woodsman_(2004_film)
    /wiki/Fox_Broadcasting_Company
    /wiki/The_Following
    /wiki/HBO
    /wiki/Taking_Chance
    /wiki/Golden_Globe_Award
    /wiki/Screen_Actors_Guild_Award
    /wiki/Primetime_Emmy_Award
    /wiki/The_Guardian
    /wiki/Academy_Award
    #cite_note-3
    /wiki/Hollywood_Walk_of_Fame
    #cite_note-4
    /wiki/Social_networks
    /wiki/Six_Degrees_of_Kevin_Bacon
    /wiki/SixDegrees.org
    #cite_note-walk-5
    #Early_life_and_education
    #Acting_career
    #Early_work
    #1980s
    #1990s
    #2000s
    #2010s
    #Advertising_work
    #Personal_life
    #Six_Degrees_of_Kevin_Bacon
    #Music
    #Awards_and_nominations
    #Filmography
    #See_also
    #References
    #External_links
    /wiki/Philadelphia
    #cite_note-actor-2
    #cite_note-actor-2
    /wiki/Edmund_Bacon_(architect)
    #cite_note-bacon-6
    /wiki/Pennsylvania_Governor%27s_School_for_the_Arts
    /wiki/Bucknell_University
    #cite_note-7
    /wiki/Glory_Van_Scott
    #cite_note-walk-5
    #cite_note-bacon-6
    /wiki/Circle_in_the_Square
    /wiki/Nancy_Mills
    /wiki/Cosmopolitan_(magazine)
    #cite_note-cosmo91-8
    /wiki/Fraternities_and_sororities
    /wiki/Animal_House
    #cite_note-bacon-6
    /wiki/Search_for_Tomorrow
    /wiki/Guiding_Light
    /wiki/Friday_the_13th_(1980_film)
    #cite_note-9
    /wiki/Phoenix_Theater
    /wiki/Flux
    /wiki/Second_Stage_Theatre
    #cite_note-bio-10
    /wiki/Obie_Award
    /wiki/Forty_Deuce
    #cite_note-kevin-11
    /wiki/Slab_Boys
    /wiki/Sean_Penn
    /wiki/Val_Kilmer
    /wiki/Barry_Levinson
    /wiki/Diner_(film)
    /wiki/Steve_Guttenberg
    /wiki/Daniel_Stern_(actor)
    /wiki/Mickey_Rourke
    /wiki/Tim_Daly
    /wiki/Ellen_Barkin
    #cite_note-12
    /wiki/Footloose_(1984_film)
    #cite_note-bio-10
    /wiki/James_Dean
    /wiki/Rebel_Without_a_Cause
    /wiki/Mickey_Rooney
    /wiki/Judy_Garland
    #cite_note-time84-13
    #cite_note-bacon-6
    #cite_note-14
    #cite_note-15
    /wiki/People_(American_magazine)
    /wiki/Typecasting_(acting)
    /wiki/John_Hughes_(filmmaker)
    /wiki/She%27s_Having_a_Baby
    #cite_note-bio-10
    /wiki/The_Big_Picture_(1989_film)
    #cite_note-16
    /wiki/Tremors_(film)
    #cite_note-17
    /wiki/Joel_Schumacher
    /wiki/Flatliners
    #cite_note-bio-10
    /wiki/Elizabeth_Perkins
    /wiki/He_Said,_She_Said
    #cite_note-bio-10
    /wiki/The_New_York_Times
    #cite_note-nyt94-18
    /wiki/Oliver_Stone
    /wiki/JFK_(film)
    #cite_note-19
    /wiki/A_Few_Good_Men_(film)
    #cite_note-20
    /wiki/Michael_Greif
    #cite_note-bio-10
    /wiki/Golden_Globe_Award
    /wiki/The_River_Wild
    #cite_note-bio-10
    /wiki/Meryl_Streep
    /wiki/Murder_in_the_First_(film)
    #cite_note-bio-10
    /wiki/Blockbuster_(entertainment)
    /wiki/Apollo_13_(film)
    #cite_note-21
    /wiki/Sleepers_(film)
    #cite_note-22
    /wiki/Picture_Perfect_(1997_film)
    #cite_note-bio-10
    /wiki/Losing_Chase
    #cite_note-austin-23
    /wiki/Digging_to_China
    #cite_note-bio-10
    /wiki/Payola
    /wiki/Telling_Lies_in_America_(film)
    #cite_note-bio-10
    /wiki/Wild_Things_(film)
    /wiki/Stir_of_Echoes
    /wiki/David_Koepp
    #cite_note-24
    /wiki/File:KevinBaconTakingChanceFeb09.jpg
    /wiki/File:KevinBaconTakingChanceFeb09.jpg
    /wiki/Taking_Chance
    /wiki/Paul_Verhoeven
    /wiki/Hollow_Man
    #cite_note-25
    /wiki/Colin_Firth
    /wiki/Rachel_Blanchard
    /wiki/M%C3%A9nage_%C3%A0_trois
    /wiki/Where_the_Truth_Lies
    #cite_note-26
    /wiki/Atom_Egoyan
    /wiki/MPAA
    /wiki/MPAA_film_rating_system
    #cite_note-27
    /wiki/Sean_Penn
    /wiki/Tim_Robbins
    /wiki/Clint_Eastwood
    /wiki/Mystic_River_(film)
    /wiki/Pedophile
    /wiki/The_Woodsman_(2004_film)
    #cite_note-28
    /wiki/HBO_Films
    /wiki/Taking_Chance
    /wiki/Michael_Strobl
    /wiki/Desert_Storm
    #cite_note-29
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
    /wiki/Matthew_Vaughn
    /wiki/X-Men:_First_Class
    #cite_note-30
    /wiki/Sebastian_Shaw_(comics)
    #cite_note-31
    /wiki/Dustin_Lance_Black
    /wiki/8_(play)
    /wiki/Perry_v._Brown
    /wiki/Proposition_8
    /wiki/Charles_J._Cooper
    #cite_note-8_the_play-32
    /wiki/Wilshire_Ebell_Theatre
    /wiki/American_Foundation_for_Equal_Rights
    #cite_note-8_play_video-33
    #cite_note-34
    /wiki/The_Following
    #cite_note-35
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    #cite_note-36
    /wiki/Huffington_Post
    #cite_note-37
    /wiki/Tremors_(film)
    /wiki/Wikipedia:Citation_needed
    /wiki/Tremors_5:_Bloodline
    /wiki/EE_(telecommunications_company)
    /wiki/United_Kingdom
    #cite_note-38
    #cite_note-39
    /wiki/Egg_as_food
    #cite_note-40
    /wiki/Kyra_Sedgwick
    /wiki/PBS
    /wiki/Lanford_Wilson
    /wiki/Lemon_Sky
    #cite_note-cosmo91-8
    /wiki/Pyrates
    /wiki/Murder_in_the_First_(film)
    /wiki/The_Woodsman_(2004_film)
    /wiki/Loverboy_(2005_film)
    /wiki/Sosie_Bacon
    /wiki/Upper_West_Side
    /wiki/Manhattan
    #cite_note-41
    /wiki/Tracy_Pollan
    #cite_note-42
    #cite_note-43
    #cite_note-44
    /wiki/The_Times
    #cite_note-45
    #cite_note-46
    /wiki/Will.i.am
    /wiki/It%27s_a_New_Day_(Will.i.am_song)
    /wiki/Barack_Obama
    /wiki/Ponzi_scheme
    /wiki/Bernard_Madoff
    #cite_note-financialpost-47
    #cite_note-48
    /wiki/Finding_Your_Roots
    /wiki/Henry_Louis_Gates
    #cite_note-49
    #cite_note-50
    #cite_note-51
    /wiki/Six_Degrees_of_Kevin_Bacon
    /wiki/Trivia
    /wiki/Big_screen
    /wiki/Six_degrees_of_separation
    /wiki/Internet_meme
    /wiki/SixDegrees.org
    #cite_note-52
    /wiki/Bacon_number
    /wiki/Internet_Movie_Database
    #cite_note-53
    /wiki/Paul_Erd%C5%91s
    /wiki/Erd%C5%91s_number
    /wiki/Paul_Erd%C5%91s
    /wiki/Bacon_number
    /wiki/Erd%C5%91s_number
    /wiki/Erd%C5%91s%E2%80%93Bacon_number
    #cite_note-54
    /wiki/The_Bacon_Brothers
    /wiki/Michael_Bacon_(musician)
    /wiki/Music_album
    #cite_note-55
    /wiki/File:Question_book-new.svg
    /wiki/Wikipedia:Citing_sources
    /wiki/Wikipedia:Verifiability
    //en.wikipedia.org/w/index.php?title=Kevin_Bacon&action=edit
    /wiki/Help:Introduction_to_referencing_with_Wiki_Markup/1
    /wiki/Wikipedia:Verifiability#Burden_of_evidence
    /wiki/Help:Maintenance_template_removal
    /wiki/Golden_Globe_Awards
    /wiki/Golden_Globe_Award_for_Best_Supporting_Actor_%E2%80%93_Motion_Picture
    /wiki/The_River_Wild
    /wiki/Broadcast_Film_Critics_Association_Awards
    /wiki/Broadcast_Film_Critics_Association_Award_for_Best_Actor
    /wiki/Murder_in_the_First_(film)
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
    /wiki/Apollo_13_(film)
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Supporting_Role
    /wiki/Murder_in_the_First_(film)
    /wiki/MTV_Movie_Awards
    /wiki/MTV_Movie_Award_for_Best_Villain
    /wiki/Hollow_Man
    /wiki/Boston_Society_of_Film_Critics_Awards
    /wiki/Boston_Society_of_Film_Critics_Award_for_Best_Cast
    /wiki/Mystic_River_(film)
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
    /wiki/Mystic_River_(film)
    /wiki/Satellite_Awards
    /wiki/Satellite_Award_for_Best_Actor_%E2%80%93_Motion_Picture_Drama
    /wiki/The_Woodsman_(2004_film)
    /wiki/Teen_Choice_Awards
    /wiki/Teen_Choice_Awards
    /wiki/Beauty_Shop
    /wiki/Primetime_Emmy_Awards
    /wiki/Primetime_Emmy_Award_for_Outstanding_Lead_Actor_in_a_Miniseries_or_a_Movie
    /wiki/Taking_Chance
    /wiki/Satellite_Awards
    /wiki/Satellite_Award_for_Best_Actor_%E2%80%93_Miniseries_or_Television_Film
    /wiki/Taking_Chance
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
    /wiki/Frost/Nixon_(film)
    /wiki/Golden_Globe_Awards
    /wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Miniseries_or_Television_Film
    /wiki/Taking_Chance
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
    /wiki/Taking_Chance
    /wiki/Teen_Choice_Awards
    /wiki/Teen_Choice_Awards
    /wiki/X-Men:_First_Class
    /wiki/Saturn_Awards
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/The_Following
    /wiki/People%27s_Choice_Awards
    /wiki/People%27s_Choice_Awards
    /wiki/The_Following
    /wiki/Saturn_Awards
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/The_Following
    /wiki/Golden_Globe_Awards
    /wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Television_Series_Musical_or_Comedy
    /wiki/I_Love_Dick_(TV_series)
    #cite_note-56
    #cite_note-57
    #cite_note-58
    #cite_note-59
    /wiki/Kevin_Bacon_filmography
    /wiki/List_of_actors_with_Hollywood_Walk_of_Fame_motion_picture_stars
    #cite_ref-1
    https://web.archive.org/web/20090113222205/http://www.newenglandancestors.org/research/services/articles_gbr78.asp
    http://www.newenglandancestors.org/research/services/articles_gbr78.asp
    #cite_ref-actor_2-0
    #cite_ref-actor_2-1
    #cite_ref-actor_2-2
    http://www.biography.com/people/kevin-bacon-9542173
    #cite_ref-3
    https://www.theguardian.com/film/filmblog/2009/feb/19/best-actors-never-nominated-for-oscars
    #cite_ref-4
    http://www.walkoffame.com/kevin-bacon
    #cite_ref-walk_5-0
    #cite_ref-walk_5-1
    https://web.archive.org/web/20141016202657/http://www.thebiographychannel.co.uk/biographies/kevin-bacon.html
    http://www.thebiographychannel.co.uk/biographies/kevin-bacon.html
    #cite_ref-bacon_6-0
    #cite_ref-bacon_6-1
    #cite_ref-bacon_6-2
    #cite_ref-bacon_6-3
    http://www.biography.com/news/kevin-bacon-biography-facts
    #cite_ref-7
    https://movies.yahoo.com/person/kevin-bacon/biography.html
    #cite_ref-cosmo91_8-0
    #cite_ref-cosmo91_8-1
    #cite_ref-9
    http://www.nydailynews.com/entertainment/happy-halloween-superstars-start-horror-flick-gallery-1.98345
    #cite_ref-bio_10-0
    #cite_ref-bio_10-1
    #cite_ref-bio_10-2
    #cite_ref-bio_10-3
    #cite_ref-bio_10-4
    #cite_ref-bio_10-5
    #cite_ref-bio_10-6
    #cite_ref-bio_10-7
    #cite_ref-bio_10-8
    #cite_ref-bio_10-9
    #cite_ref-bio_10-10
    https://www.pbs.org/wnet/finding-your-roots/profiles/kevin-bacon%C2%A0/
    #cite_ref-kevin_11-0
    http://www.tvguide.com/celebrities/kevin-bacon/bio/160550
    #cite_ref-12
    http://news.moviefone.com/2012/03/02/diner-30th-anniversary/
    #cite_ref-time84_13-0
    http://www.time.com/time/magazine/article/0,9171,950019,00.html
    #cite_ref-14
    http://www.huffingtonpost.com/2014/08/25/kevin-bacon-footloose_n_5710413.html
    #cite_ref-15
    https://web.archive.org/web/20090109152125/http://www.thebiographychannel.co.uk/biography_story/522%3A492/1/Kevin_Bacon.htm
    http://www.thebiographychannel.co.uk/biography_story/522:492/1/Kevin_Bacon.htm
    #cite_ref-16
    https://www.nytimes.com/1994/09/25/movies/a-second-wind-is-blowing-for-kevin-bacon.html
    #cite_ref-17
    https://www.nytimes.com/movie/review?res=9C0CE2DE1631F93AA25752C0A966958260
    #cite_ref-nyt94_18-0
    https://query.nytimes.com/gst/fullpage.html?res=9C07E6D91F3BF936A1575AC0A962958260&sec=&spon=&pagewanted=all
    #cite_ref-19
    http://www.jfk-online.com/jfkbacon.html
    #cite_ref-20
    http://www.tcm.com/this-month/article/143158%7C0/A-Few-Good-Men.html
    #cite_ref-21
    http://collider.com/kevin-bacon-commercials-footloose/
    #cite_ref-22
    http://www.rogerebert.com/reviews/sleepers-1996
    #cite_ref-austin_23-0
    http://www.austinchronicle.com/calendar/film/1997-02-07/283342/
    /wiki/The_Austin_Chronicle
    #cite_ref-24
    http://www.criminalelement.com/blogs/2013/09/under-the-raderhorror-movies-you-may-have-missed-stir-of-echoes
    #cite_ref-25
    http://www.rogerebert.com/reviews/hollow-man-2000
    #cite_ref-26
    http://movies.about.com/od/wherethetruthlies/a/truthkb101305.htm
    #cite_ref-27
    http://jam.canoe.ca/Movies/2005/09/14/1216527.html
    #cite_ref-28
    http://www.latimes.com/entertainment/la-et-kevin-bacon-photo6-photo.html
    #cite_ref-29
    http://www.nydailynews.com/entertainment/tv-movies/kevin-bacon-chance-body-fallen-marine-home-article-1.392226
    #cite_ref-30
    https://web.archive.org/web/20100722010545/http://heatvision.hollywoodreporter.com/2010/07/winters-bone-star-cast-as-mystique-in-xmen-first-class.html
    http://heatvision.hollywoodreporter.com/2010/07/winters-bone-star-cast-as-mystique-in-xmen-first-class.html
    #cite_ref-31
    https://web.archive.org/web/20100720060214/http://www.forcesofgeek.com/2010/07/kevin-bacon-playing-sebastian-shaw-in-x.html
    http://www.forcesofgeek.com/2010/07/kevin-bacon-playing-sebastian-shaw-in-x.html
    #cite_ref-8_the_play_32-0
    http://www.accesshollywood.com/jesse-tyler-ferguson/glee-stars-touched-by-brad-pitt-and-george-clooneys-support-of-8_article_61543
    /wiki/Access_Hollywood
    #cite_ref-8_play_video_33-0
    https://www.youtube.com/watch?v=qlUG8F9uVgM
    #cite_ref-34
    http://www.pinknews.co.uk/2012/03/01/youtube-to-broadcast-proposition-8-play-live/
    #cite_ref-35
    http://www.fox.com/the-following/
    #cite_ref-36
    https://news.yahoo.com/blogs/trending-now/kevin-bacon-gives-millennials-a-history-lesson-about-the--80s-162525915.html
    #cite_ref-37
    http://www.huffingtonpost.com.au/entry/kevin-bacon-tremors-tv-reboot_us_5655b651e4b072e9d1c13a11
    #cite_ref-38
    http://www.campaignlive.co.uk/news/1294856/
    #cite_ref-39
    http://parade.condenast.com/269380/ashleighschmitz/kevin-bacon-reprises-his-most-iconic-film-roles-in-british-commercial/
    #cite_ref-40
    http://money.cnn.com/2015/03/13/media/kevin-bacon-eggs/index.html?iid=HP_LN
    #cite_ref-41
    http://www.nydailynews.com/entertainment/tv-movies/kevin-bacon-loyalty-nyc-philly-origins-peace-bustling-city-article-1.147197
    #cite_ref-42
    http://www.people.com/people/archive/article/0,,20093025,00.html
    #cite_ref-43
    http://www.au.org/media/church-and-state/archives/2008/05/two-thumbs-up.html
    #cite_ref-44
    https://www.washingtonpost.com/wp-dyn/content/article/2008/03/25/AR2008032503852.html
    #cite_ref-45
    #cite_ref-46
    http://www.foxnews.com/story/0,2933,343589,00.html
    #cite_ref-financialpost_47-0
    https://web.archive.org/web/20140314085857/http://economiccrisis.us/2009/06/may-god-spare-mercy-victim-tells-madoff/
    http://economiccrisis.us/2009/06/may-god-spare-mercy-victim-tells-madoff/
    #cite_ref-48
    #cite_ref-49
    http://www.huffingtonpost.com/megan-smolenyak-smolenyak/6-degrees-of-separation-k_b_900707.html
    #cite_ref-50
    https://web.archive.org/web/20130405182304/http://www.drawtheline.org/watch-stuff/
    http://www.drawtheline.org/watch-stuff
    #cite_ref-51
    http://www.drawtheline.org/sign-now/
    #cite_ref-52
    http://www.sixdegrees.org/
    #cite_ref-53
    http://www.webmonkey.com/2012/09/easter-egg-google-connects-the-dots-for-bacon-number-search/
    #cite_ref-54
    https://www.telegraph.co.uk/science/science-news/4768389/And-the-winner-tonight-is.html
    #cite_ref-55
    http://baconbros.com/
    #cite_ref-56
    /wiki/Reuters
    https://www.cbsnews.com/pictures/golden-globes-2018-highlights/50/
    /wiki/CBS_News
    #cite_ref-57
    https://www.theverge.com/2018/1/7/16861812/golden-globes-2018-aziz-ansari-master-of-none-best-actor-tv
    /wiki/The_Verge
    #cite_ref-58
    https://www.hollywoodreporter.com/news/aziz-ansari-wins-best-performance-by-an-actor-a-tv-series-comedy-musical-golden-globes-2018-1072154
    /wiki/The_Hollywood_Reporter
    #cite_ref-59
    http://www.indiewire.com/2018/01/aziz-ansari-wins-golden-globe-best-actor-tv-comedy-1201914235/
    /wiki/Indie_Wire
    https://commons.wikimedia.org/wiki/Category:Kevin_Bacon
    https://www.imdb.com/name/nm0000102/
    /wiki/IMDb
    https://www.ibdb.com/Person/View/90569
    /wiki/Internet_Broadway_Database
    https://www.wikidata.org/wiki/Q3454165#P1220
    http://www.lortel.org/Archives/CreditableEntity/5597
    /wiki/Lortel_Archives
    https://www.allmovie.com/artist/p3164
    /wiki/AllMovie
    http://oracleofbacon.org
    /wiki/Template:Critics%27_Choice_Movie_Award_for_Best_Actor
    /wiki/Template_talk:Critics%27_Choice_Movie_Award_for_Best_Actor
    //en.wikipedia.org/w/index.php?title=Template:Critics%27_Choice_Movie_Award_for_Best_Actor&action=edit
    /wiki/Critics%27_Choice_Movie_Award_for_Best_Actor
    /wiki/Geoffrey_Rush
    /wiki/Jack_Nicholson
    /wiki/Ian_McKellen
    /wiki/Russell_Crowe
    /wiki/Russell_Crowe
    /wiki/Russell_Crowe
    /wiki/Daniel_Day-Lewis
    /wiki/Jack_Nicholson
    /wiki/Sean_Penn
    /wiki/Jamie_Foxx
    /wiki/Philip_Seymour_Hoffman
    /wiki/Forest_Whitaker
    /wiki/Daniel_Day-Lewis
    /wiki/Sean_Penn
    /wiki/Jeff_Bridges
    /wiki/Colin_Firth
    /wiki/George_Clooney
    /wiki/Daniel_Day-Lewis
    /wiki/Matthew_McConaughey
    /wiki/Michael_Keaton
    /wiki/Leonardo_DiCaprio
    /wiki/Casey_Affleck
    /wiki/Gary_Oldman
    /wiki/Template:GoldenGlobeBestActorTVMiniseriesFilm
    /wiki/Template_talk:GoldenGlobeBestActorTVMiniseriesFilm
    //en.wikipedia.org/w/index.php?title=Template:GoldenGlobeBestActorTVMiniseriesFilm&action=edit
    /wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Miniseries_or_Television_Film
    /wiki/Mickey_Rooney
    /wiki/Anthony_Andrews
    /wiki/Richard_Chamberlain
    /wiki/Ted_Danson
    /wiki/Dustin_Hoffman
    /wiki/James_Woods
    /wiki/Randy_Quaid
    /wiki/Michael_Caine
    /wiki/Stacy_Keach
    /wiki/Robert_Duvall
    /wiki/James_Garner
    /wiki/Beau_Bridges
    /wiki/Robert_Duvall
    /wiki/James_Garner
    /wiki/Ra%C3%BAl_Juli%C3%A1
    /wiki/Gary_Sinise
    /wiki/Alan_Rickman
    /wiki/Ving_Rhames
    /wiki/Stanley_Tucci
    /wiki/Jack_Lemmon
    /wiki/Brian_Dennehy
    /wiki/James_Franco
    /wiki/Albert_Finney
    /wiki/Al_Pacino
    /wiki/Geoffrey_Rush
    /wiki/Jonathan_Rhys_Meyers
    /wiki/Bill_Nighy
    /wiki/Jim_Broadbent
    /wiki/Paul_Giamatti
    /wiki/Al_Pacino
    /wiki/Idris_Elba
    /wiki/Kevin_Costner
    /wiki/Michael_Douglas
    /wiki/Billy_Bob_Thornton
    /wiki/Oscar_Isaac
    /wiki/Tom_Hiddleston
    /wiki/Ewan_McGregor
    /wiki/Template:Saturn_Award_for_Best_Actor_on_Television
    /wiki/Template_talk:Saturn_Award_for_Best_Actor_on_Television
    //en.wikipedia.org/w/index.php?title=Template:Saturn_Award_for_Best_Actor_on_Television&action=edit
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/Kyle_Chandler
    /wiki/Steven_Weber_(actor)
    /wiki/Richard_Dean_Anderson
    /wiki/David_Boreanaz
    /wiki/Robert_Patrick
    /wiki/Ben_Browder
    /wiki/David_Boreanaz
    /wiki/David_Boreanaz
    /wiki/Ben_Browder
    /wiki/Matthew_Fox
    /wiki/Michael_C._Hall
    /wiki/Matthew_Fox
    /wiki/Edward_James_Olmos
    /wiki/Josh_Holloway
    /wiki/Stephen_Moyer
    /wiki/Bryan_Cranston
    /wiki/Bryan_Cranston
    /wiki/Mads_Mikkelsen
    /wiki/Hugh_Dancy
    /wiki/Andrew_Lincoln
    /wiki/Bruce_Campbell
    /wiki/Andrew_Lincoln
    /wiki/Template:ScreenActorsGuildAward_MaleTVMiniseriesMovie
    /wiki/Template_talk:ScreenActorsGuildAward_MaleTVMiniseriesMovie
    //en.wikipedia.org/w/index.php?title=Template:ScreenActorsGuildAward_MaleTVMiniseriesMovie&action=edit
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
    /wiki/Ra%C3%BAl_Juli%C3%A1
    /wiki/Gary_Sinise
    /wiki/Alan_Rickman
    /wiki/Gary_Sinise
    /wiki/Christopher_Reeve
    /wiki/Jack_Lemmon
    /wiki/Brian_Dennehy
    /wiki/Ben_Kingsley
    /wiki/William_H._Macy
    /wiki/Al_Pacino
    /wiki/Geoffrey_Rush
    /wiki/Paul_Newman
    /wiki/Jeremy_Irons
    /wiki/Kevin_Kline
    /wiki/Paul_Giamatti
    /wiki/Al_Pacino
    /wiki/Paul_Giamatti
    /wiki/Kevin_Costner
    /wiki/Michael_Douglas
    /wiki/Mark_Ruffalo
    /wiki/Idris_Elba
    /wiki/Bryan_Cranston
    /wiki/Alexander_Skarsg%C3%A5rd
    /wiki/Help:Authority_control
    https://www.worldcat.org/identities/containsVIAFID/39570812
    /wiki/Virtual_International_Authority_File
    https://viaf.org/viaf/39570812
    /wiki/Library_of_Congress_Control_Number
    http://id.loc.gov/authorities/names/n88034930
    /wiki/International_Standard_Name_Identifier
    http://isni.org/isni/0000000121291300
    /wiki/Integrated_Authority_File
    https://d-nb.info/gnd/124109659
    /wiki/Syst%C3%A8me_universitaire_de_documentation
    https://www.idref.fr/084292652
    /wiki/Biblioth%C3%A8que_nationale_de_France
    http://catalogue.bnf.fr/ark:/12148/cb139817766
    http://data.bnf.fr/ark:/12148/cb139817766
    /wiki/MusicBrainz
    https://musicbrainz.org/artist/cc0dbdfc-9b2c-4e31-8448-808412388406
    /wiki/Biblioteca_Nacional_de_Espa%C3%B1a
    http://catalogo.bne.es/uhtbin/authoritybrowse.cgi?action=display&authority_id=XX1298810
    /wiki/SNAC
    http://socialarchive.iath.virginia.edu/ark:/99166/w6w67gw2
    https://en.wikipedia.org/w/index.php?title=Kevin_Bacon&oldid=839045002
    /wiki/Help:Category
    /wiki/Category:1958_births
    /wiki/Category:20th-century_American_male_actors
    /wiki/Category:21st-century_American_male_actors
    /wiki/Category:American_atheists
    /wiki/Category:American_male_film_actors
    /wiki/Category:American_male_soap_opera_actors
    /wiki/Category:American_male_television_actors
    /wiki/Category:American_male_voice_actors
    /wiki/Category:The_Bacon_Brothers_members
    /wiki/Category:Best_Miniseries_or_Television_Movie_Actor_Golden_Globe_winners
    /wiki/Category:Circle_in_the_Square_Theatre_School_alumni
    /wiki/Category:Living_people
    /wiki/Category:Male_actors_from_Philadelphia
    /wiki/Category:Obie_Award_recipients
    /wiki/Category:Outstanding_Performance_by_a_Cast_in_a_Motion_Picture_Screen_Actors_Guild_Award_winners
    /wiki/Category:Sedgwick_family
    /wiki/Category:Wikipedia_indefinitely_semi-protected_biographies_of_living_people
    /wiki/Category:Use_mdy_dates_from_October_2016
    /wiki/Category:Articles_with_hCards
    /wiki/Category:All_articles_with_unsourced_statements
    /wiki/Category:Articles_with_unsourced_statements_from_January_2016
    /wiki/Category:Articles_needing_additional_references_from_October_2017
    /wiki/Category:All_articles_needing_additional_references
    /wiki/Category:Articles_with_IBDb_links
    /wiki/Category:Wikipedia_articles_with_VIAF_identifiers
    /wiki/Category:Wikipedia_articles_with_LCCN_identifiers
    /wiki/Category:Wikipedia_articles_with_ISNI_identifiers
    /wiki/Category:Wikipedia_articles_with_GND_identifiers
    /wiki/Category:Wikipedia_articles_with_BNF_identifiers
    /wiki/Category:Wikipedia_articles_with_MusicBrainz_identifiers
    /wiki/Category:Wikipedia_articles_with_SNAC-ID_identifiers
    /wiki/Special:MyTalk
    /wiki/Special:MyContributions
    /w/index.php?title=Special:CreateAccount&returnto=Kevin+Bacon
    /w/index.php?title=Special:UserLogin&returnto=Kevin+Bacon
    /wiki/Kevin_Bacon
    /wiki/Talk:Kevin_Bacon
    /wiki/Kevin_Bacon
    /w/index.php?title=Kevin_Bacon&action=edit
    /w/index.php?title=Kevin_Bacon&action=history
    /wiki/Main_Page
    /wiki/Main_Page
    /wiki/Portal:Contents
    /wiki/Portal:Featured_content
    /wiki/Portal:Current_events
    /wiki/Special:Random
    https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en
    //shop.wikimedia.org
    /wiki/Help:Contents
    /wiki/Wikipedia:About
    /wiki/Wikipedia:Community_portal
    /wiki/Special:RecentChanges
    //en.wikipedia.org/wiki/Wikipedia:Contact_us
    /wiki/Special:WhatLinksHere/Kevin_Bacon
    /wiki/Special:RecentChangesLinked/Kevin_Bacon
    /wiki/Wikipedia:File_Upload_Wizard
    /wiki/Special:SpecialPages
    /w/index.php?title=Kevin_Bacon&oldid=839045002
    /w/index.php?title=Kevin_Bacon&action=info
    https://www.wikidata.org/wiki/Special:EntityPage/Q3454165
    /w/index.php?title=Special:CiteThisPage&page=Kevin_Bacon&id=839045002
    /w/index.php?title=Special:Book&bookcmd=book_creator&referer=Kevin+Bacon
    /w/index.php?title=Special:ElectronPdf&page=Kevin+Bacon&action=show-download-screen
    /w/index.php?title=Kevin_Bacon&printable=yes
    https://commons.wikimedia.org/wiki/Category:Kevin_Bacon
    https://af.wikipedia.org/wiki/Kevin_Bacon
    https://ar.wikipedia.org/wiki/%D9%83%D9%8A%D9%81%D9%8A%D9%86_%D8%A8%D9%8A%D9%83%D9%86
    https://an.wikipedia.org/wiki/Kevin_Bacon
    https://ast.wikipedia.org/wiki/Kevin_Bacon
    https://azb.wikipedia.org/wiki/%DA%A9%D9%88%DB%8C%D9%86_%D8%A8%DB%8C%DA%A9%D9%86
    https://zh-min-nan.wikipedia.org/wiki/Kevin_Bacon
    https://bi.wikipedia.org/wiki/Kevin_Bacon
    https://bg.wikipedia.org/wiki/%D0%9A%D0%B5%D0%B2%D0%B8%D0%BD_%D0%91%D0%B5%D0%B9%D0%BA%D1%8A%D0%BD
    https://bs.wikipedia.org/wiki/Kevin_Bacon
    https://ca.wikipedia.org/wiki/Kevin_Bacon
    https://cs.wikipedia.org/wiki/Kevin_Bacon
    https://da.wikipedia.org/wiki/Kevin_Bacon
    https://de.wikipedia.org/wiki/Kevin_Bacon
    https://el.wikipedia.org/wiki/%CE%9A%CE%AD%CE%B2%CE%B9%CE%BD_%CE%9C%CF%80%CE%AD%CE%B9%CE%BA%CE%BF%CE%BD
    https://eml.wikipedia.org/wiki/Kevin_Bacon
    https://es.wikipedia.org/wiki/Kevin_Bacon
    https://eu.wikipedia.org/wiki/Kevin_Bacon
    https://fa.wikipedia.org/wiki/%DA%A9%D9%88%DB%8C%D9%86_%D8%A8%DB%8C%DA%A9%D9%86
    https://fr.wikipedia.org/wiki/Kevin_Bacon
    https://gl.wikipedia.org/wiki/Kevin_Bacon
    https://ko.wikipedia.org/wiki/%EC%BC%80%EB%B9%88_%EB%B2%A0%EC%9D%B4%EC%BB%A8
    https://hy.wikipedia.org/wiki/%D5%94%D6%87%D5%AB%D5%B6_%D4%B2%D5%A5%D5%B5%D6%84%D5%B8%D5%B6
    https://hr.wikipedia.org/wiki/Kevin_Bacon
    https://io.wikipedia.org/wiki/Kevin_Bacon
    https://id.wikipedia.org/wiki/Kevin_Bacon
    https://it.wikipedia.org/wiki/Kevin_Bacon
    https://he.wikipedia.org/wiki/%D7%A7%D7%95%D7%95%D7%99%D7%9F_%D7%91%D7%99%D7%99%D7%A7%D7%95%D7%9F
    https://ka.wikipedia.org/wiki/%E1%83%99%E1%83%94%E1%83%95%E1%83%98%E1%83%9C_%E1%83%91%E1%83%94%E1%83%98%E1%83%99%E1%83%9D%E1%83%9C%E1%83%98
    https://kk.wikipedia.org/wiki/%D0%9A%D0%B5%D0%B2%D0%B8%D0%BD_%D0%91%D1%8D%D0%B9%D0%BA%D0%BE%D0%BD
    https://lv.wikipedia.org/wiki/Kevins_B%C4%93kons
    https://hu.wikipedia.org/wiki/Kevin_Bacon
    https://xmf.wikipedia.org/wiki/%E1%83%99%E1%83%94%E1%83%95%E1%83%98%E1%83%9C_%E1%83%91%E1%83%94%E1%83%98%E1%83%99%E1%83%9D%E1%83%9C%E1%83%98
    https://mn.wikipedia.org/wiki/%D0%9A%D0%B5%D0%B2%D0%B8%D0%BD_%D0%91%D1%8D%D0%B9%D0%BA%D0%BE%D0%BD
    https://nl.wikipedia.org/wiki/Kevin_Bacon
    https://ja.wikipedia.org/wiki/%E3%82%B1%E3%83%B4%E3%82%A3%E3%83%B3%E3%83%BB%E3%83%99%E3%83%BC%E3%82%B3%E3%83%B3
    https://no.wikipedia.org/wiki/Kevin_Bacon
    https://oc.wikipedia.org/wiki/Kevin_Bacon
    https://pl.wikipedia.org/wiki/Kevin_Bacon
    https://pt.wikipedia.org/wiki/Kevin_Bacon
    https://ro.wikipedia.org/wiki/Kevin_Bacon
    https://ru.wikipedia.org/wiki/%D0%91%D0%B5%D0%B9%D0%BA%D0%BE%D0%BD,_%D0%9A%D0%B5%D0%B2%D0%B8%D0%BD
    https://sco.wikipedia.org/wiki/Kevin_Bacon
    https://simple.wikipedia.org/wiki/Kevin_Bacon
    https://sk.wikipedia.org/wiki/Kevin_Bacon
    https://ckb.wikipedia.org/wiki/%DA%A9%DB%8E%DA%A4%D9%86_%D8%A8%DB%95%DB%8C%DA%A9%D9%86
    https://sr.wikipedia.org/wiki/%D0%9A%D0%B5%D0%B2%D0%B8%D0%BD_%D0%91%D0%B5%D1%98%D0%BA%D0%BE%D0%BD
    https://sh.wikipedia.org/wiki/Kevin_Bacon
    https://fi.wikipedia.org/wiki/Kevin_Bacon
    https://sv.wikipedia.org/wiki/Kevin_Bacon
    https://th.wikipedia.org/wiki/%E0%B9%80%E0%B8%84%E0%B8%A7%E0%B8%B4%E0%B8%99_%E0%B9%80%E0%B8%9A%E0%B8%84%E0%B8%AD%E0%B8%99
    https://tr.wikipedia.org/wiki/Kevin_Bacon
    https://uk.wikipedia.org/wiki/%D0%9A%D0%B5%D0%B2%D1%96%D0%BD_%D0%91%D0%B5%D0%B9%D0%BA%D0%BE%D0%BD
    https://vi.wikipedia.org/wiki/Kevin_Bacon
    https://zh.wikipedia.org/wiki/%E5%87%AF%E6%96%87%C2%B7%E8%B4%9D%E8%82%AF
    https://www.wikidata.org/wiki/Special:EntityPage/Q3454165#sitelinks-wikipedia
    //en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License
    //creativecommons.org/licenses/by-sa/3.0/
    //wikimediafoundation.org/wiki/Terms_of_Use
    //wikimediafoundation.org/wiki/Privacy_policy
    //www.wikimediafoundation.org/
    https://wikimediafoundation.org/wiki/Privacy_policy
    /wiki/Wikipedia:About
    /wiki/Wikipedia:General_disclaimer
    //en.wikipedia.org/wiki/Wikipedia:Contact_us
    https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute
    https://wikimediafoundation.org/wiki/Cookie_statement
    //en.m.wikipedia.org/w/index.php?title=Kevin_Bacon&mobileaction=toggle_view_mobile
    https://wikimediafoundation.org/
    //www.mediawiki.org/


上面的写法虽然能够拿到需要的连接，但是有些是我们不需要的，因此需要加过滤。


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html)

for link in bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')): # 以/wiki/开头
    if 'href' in link.attrs:
        print(link.attrs['href'])
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))


    /wiki/Kevin_Bacon_(disambiguation)
    /wiki/San_Diego_Comic-Con
    /wiki/Philadelphia
    /wiki/Pennsylvania
    /wiki/Kyra_Sedgwick
    /wiki/Sosie_Bacon
    /wiki/Edmund_Bacon_(architect)
    /wiki/Michael_Bacon_(musician)
    /wiki/Footloose_(1984_film)
    /wiki/JFK_(film)
    /wiki/A_Few_Good_Men
    /wiki/Apollo_13_(film)
    /wiki/Mystic_River_(film)
    /wiki/Sleepers
    /wiki/The_Woodsman_(2004_film)
    /wiki/Fox_Broadcasting_Company
    /wiki/The_Following
    /wiki/HBO
    /wiki/Taking_Chance
    /wiki/Golden_Globe_Award
    /wiki/Screen_Actors_Guild_Award
    /wiki/Primetime_Emmy_Award
    /wiki/The_Guardian
    /wiki/Academy_Award
    /wiki/Hollywood_Walk_of_Fame
    /wiki/Social_networks
    /wiki/Six_Degrees_of_Kevin_Bacon
    /wiki/SixDegrees.org
    /wiki/Philadelphia
    /wiki/Edmund_Bacon_(architect)
    /wiki/Pennsylvania_Governor%27s_School_for_the_Arts
    /wiki/Bucknell_University
    /wiki/Glory_Van_Scott
    /wiki/Circle_in_the_Square
    /wiki/Nancy_Mills
    /wiki/Cosmopolitan_(magazine)
    /wiki/Fraternities_and_sororities
    /wiki/Animal_House
    /wiki/Search_for_Tomorrow
    /wiki/Guiding_Light
    /wiki/Friday_the_13th_(1980_film)
    /wiki/Phoenix_Theater
    /wiki/Flux
    /wiki/Second_Stage_Theatre
    /wiki/Obie_Award
    /wiki/Forty_Deuce
    /wiki/Slab_Boys
    /wiki/Sean_Penn
    /wiki/Val_Kilmer
    /wiki/Barry_Levinson
    /wiki/Diner_(film)
    /wiki/Steve_Guttenberg
    /wiki/Daniel_Stern_(actor)
    /wiki/Mickey_Rourke
    /wiki/Tim_Daly
    /wiki/Ellen_Barkin
    /wiki/Footloose_(1984_film)
    /wiki/James_Dean
    /wiki/Rebel_Without_a_Cause
    /wiki/Mickey_Rooney
    /wiki/Judy_Garland
    /wiki/People_(American_magazine)
    /wiki/Typecasting_(acting)
    /wiki/John_Hughes_(filmmaker)
    /wiki/She%27s_Having_a_Baby
    /wiki/The_Big_Picture_(1989_film)
    /wiki/Tremors_(film)
    /wiki/Joel_Schumacher
    /wiki/Flatliners
    /wiki/Elizabeth_Perkins
    /wiki/He_Said,_She_Said
    /wiki/The_New_York_Times
    /wiki/Oliver_Stone
    /wiki/JFK_(film)
    /wiki/A_Few_Good_Men_(film)
    /wiki/Michael_Greif
    /wiki/Golden_Globe_Award
    /wiki/The_River_Wild
    /wiki/Meryl_Streep
    /wiki/Murder_in_the_First_(film)
    /wiki/Blockbuster_(entertainment)
    /wiki/Apollo_13_(film)
    /wiki/Sleepers_(film)
    /wiki/Picture_Perfect_(1997_film)
    /wiki/Losing_Chase
    /wiki/Digging_to_China
    /wiki/Payola
    /wiki/Telling_Lies_in_America_(film)
    /wiki/Wild_Things_(film)
    /wiki/Stir_of_Echoes
    /wiki/David_Koepp
    /wiki/Taking_Chance
    /wiki/Paul_Verhoeven
    /wiki/Hollow_Man
    /wiki/Colin_Firth
    /wiki/Rachel_Blanchard
    /wiki/M%C3%A9nage_%C3%A0_trois
    /wiki/Where_the_Truth_Lies
    /wiki/Atom_Egoyan
    /wiki/MPAA
    /wiki/MPAA_film_rating_system
    /wiki/Sean_Penn
    /wiki/Tim_Robbins
    /wiki/Clint_Eastwood
    /wiki/Mystic_River_(film)
    /wiki/Pedophile
    /wiki/The_Woodsman_(2004_film)
    /wiki/HBO_Films
    /wiki/Taking_Chance
    /wiki/Michael_Strobl
    /wiki/Desert_Storm
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
    /wiki/Matthew_Vaughn
    /wiki/Sebastian_Shaw_(comics)
    /wiki/Dustin_Lance_Black
    /wiki/8_(play)
    /wiki/Perry_v._Brown
    /wiki/Proposition_8
    /wiki/Charles_J._Cooper
    /wiki/Wilshire_Ebell_Theatre
    /wiki/American_Foundation_for_Equal_Rights
    /wiki/The_Following
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/Huffington_Post
    /wiki/Tremors_(film)
    /wiki/EE_(telecommunications_company)
    /wiki/United_Kingdom
    /wiki/Egg_as_food
    /wiki/Kyra_Sedgwick
    /wiki/PBS
    /wiki/Lanford_Wilson
    /wiki/Lemon_Sky
    /wiki/Pyrates
    /wiki/Murder_in_the_First_(film)
    /wiki/The_Woodsman_(2004_film)
    /wiki/Loverboy_(2005_film)
    /wiki/Sosie_Bacon
    /wiki/Upper_West_Side
    /wiki/Manhattan
    /wiki/Tracy_Pollan
    /wiki/The_Times
    /wiki/Will.i.am
    /wiki/It%27s_a_New_Day_(Will.i.am_song)
    /wiki/Barack_Obama
    /wiki/Ponzi_scheme
    /wiki/Bernard_Madoff
    /wiki/Finding_Your_Roots
    /wiki/Henry_Louis_Gates
    /wiki/Six_Degrees_of_Kevin_Bacon
    /wiki/Trivia
    /wiki/Big_screen
    /wiki/Six_degrees_of_separation
    /wiki/Internet_meme
    /wiki/SixDegrees.org
    /wiki/Bacon_number
    /wiki/Internet_Movie_Database
    /wiki/Paul_Erd%C5%91s
    /wiki/Erd%C5%91s_number
    /wiki/Paul_Erd%C5%91s
    /wiki/Bacon_number
    /wiki/Erd%C5%91s_number
    /wiki/Erd%C5%91s%E2%80%93Bacon_number
    /wiki/The_Bacon_Brothers
    /wiki/Michael_Bacon_(musician)
    /wiki/Music_album
    /wiki/Golden_Globe_Awards
    /wiki/Golden_Globe_Award_for_Best_Supporting_Actor_%E2%80%93_Motion_Picture
    /wiki/The_River_Wild
    /wiki/Broadcast_Film_Critics_Association_Awards
    /wiki/Broadcast_Film_Critics_Association_Award_for_Best_Actor
    /wiki/Murder_in_the_First_(film)
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
    /wiki/Apollo_13_(film)
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Supporting_Role
    /wiki/Murder_in_the_First_(film)
    /wiki/MTV_Movie_Awards
    /wiki/MTV_Movie_Award_for_Best_Villain
    /wiki/Hollow_Man
    /wiki/Boston_Society_of_Film_Critics_Awards
    /wiki/Boston_Society_of_Film_Critics_Award_for_Best_Cast
    /wiki/Mystic_River_(film)
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
    /wiki/Mystic_River_(film)
    /wiki/Satellite_Awards
    /wiki/Satellite_Award_for_Best_Actor_%E2%80%93_Motion_Picture_Drama
    /wiki/The_Woodsman_(2004_film)
    /wiki/Teen_Choice_Awards
    /wiki/Teen_Choice_Awards
    /wiki/Beauty_Shop
    /wiki/Primetime_Emmy_Awards
    /wiki/Primetime_Emmy_Award_for_Outstanding_Lead_Actor_in_a_Miniseries_or_a_Movie
    /wiki/Taking_Chance
    /wiki/Satellite_Awards
    /wiki/Satellite_Award_for_Best_Actor_%E2%80%93_Miniseries_or_Television_Film
    /wiki/Taking_Chance
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Cast_in_a_Motion_Picture
    /wiki/Frost/Nixon_(film)
    /wiki/Golden_Globe_Awards
    /wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Miniseries_or_Television_Film
    /wiki/Taking_Chance
    /wiki/Screen_Actors_Guild_Awards
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
    /wiki/Taking_Chance
    /wiki/Teen_Choice_Awards
    /wiki/Teen_Choice_Awards
    /wiki/Saturn_Awards
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/The_Following
    /wiki/People%27s_Choice_Awards
    /wiki/People%27s_Choice_Awards
    /wiki/The_Following
    /wiki/Saturn_Awards
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/The_Following
    /wiki/Golden_Globe_Awards
    /wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Television_Series_Musical_or_Comedy
    /wiki/I_Love_Dick_(TV_series)
    /wiki/Kevin_Bacon_filmography
    /wiki/List_of_actors_with_Hollywood_Walk_of_Fame_motion_picture_stars
    /wiki/The_Austin_Chronicle
    /wiki/Access_Hollywood
    /wiki/Reuters
    /wiki/CBS_News
    /wiki/The_Verge
    /wiki/The_Hollywood_Reporter
    /wiki/Indie_Wire
    /wiki/IMDb
    /wiki/Internet_Broadway_Database
    /wiki/Lortel_Archives
    /wiki/AllMovie
    /wiki/Critics%27_Choice_Movie_Award_for_Best_Actor
    /wiki/Geoffrey_Rush
    /wiki/Jack_Nicholson
    /wiki/Ian_McKellen
    /wiki/Russell_Crowe
    /wiki/Russell_Crowe
    /wiki/Russell_Crowe
    /wiki/Daniel_Day-Lewis
    /wiki/Jack_Nicholson
    /wiki/Sean_Penn
    /wiki/Jamie_Foxx
    /wiki/Philip_Seymour_Hoffman
    /wiki/Forest_Whitaker
    /wiki/Daniel_Day-Lewis
    /wiki/Sean_Penn
    /wiki/Jeff_Bridges
    /wiki/Colin_Firth
    /wiki/George_Clooney
    /wiki/Daniel_Day-Lewis
    /wiki/Matthew_McConaughey
    /wiki/Michael_Keaton
    /wiki/Leonardo_DiCaprio
    /wiki/Casey_Affleck
    /wiki/Gary_Oldman
    /wiki/Golden_Globe_Award_for_Best_Actor_%E2%80%93_Miniseries_or_Television_Film
    /wiki/Mickey_Rooney
    /wiki/Anthony_Andrews
    /wiki/Richard_Chamberlain
    /wiki/Ted_Danson
    /wiki/Dustin_Hoffman
    /wiki/James_Woods
    /wiki/Randy_Quaid
    /wiki/Michael_Caine
    /wiki/Stacy_Keach
    /wiki/Robert_Duvall
    /wiki/James_Garner
    /wiki/Beau_Bridges
    /wiki/Robert_Duvall
    /wiki/James_Garner
    /wiki/Ra%C3%BAl_Juli%C3%A1
    /wiki/Gary_Sinise
    /wiki/Alan_Rickman
    /wiki/Ving_Rhames
    /wiki/Stanley_Tucci
    /wiki/Jack_Lemmon
    /wiki/Brian_Dennehy
    /wiki/James_Franco
    /wiki/Albert_Finney
    /wiki/Al_Pacino
    /wiki/Geoffrey_Rush
    /wiki/Jonathan_Rhys_Meyers
    /wiki/Bill_Nighy
    /wiki/Jim_Broadbent
    /wiki/Paul_Giamatti
    /wiki/Al_Pacino
    /wiki/Idris_Elba
    /wiki/Kevin_Costner
    /wiki/Michael_Douglas
    /wiki/Billy_Bob_Thornton
    /wiki/Oscar_Isaac
    /wiki/Tom_Hiddleston
    /wiki/Ewan_McGregor
    /wiki/Saturn_Award_for_Best_Actor_on_Television
    /wiki/Kyle_Chandler
    /wiki/Steven_Weber_(actor)
    /wiki/Richard_Dean_Anderson
    /wiki/David_Boreanaz
    /wiki/Robert_Patrick
    /wiki/Ben_Browder
    /wiki/David_Boreanaz
    /wiki/David_Boreanaz
    /wiki/Ben_Browder
    /wiki/Matthew_Fox
    /wiki/Michael_C._Hall
    /wiki/Matthew_Fox
    /wiki/Edward_James_Olmos
    /wiki/Josh_Holloway
    /wiki/Stephen_Moyer
    /wiki/Bryan_Cranston
    /wiki/Bryan_Cranston
    /wiki/Mads_Mikkelsen
    /wiki/Hugh_Dancy
    /wiki/Andrew_Lincoln
    /wiki/Bruce_Campbell
    /wiki/Andrew_Lincoln
    /wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Miniseries_or_Television_Movie
    /wiki/Ra%C3%BAl_Juli%C3%A1
    /wiki/Gary_Sinise
    /wiki/Alan_Rickman
    /wiki/Gary_Sinise
    /wiki/Christopher_Reeve
    /wiki/Jack_Lemmon
    /wiki/Brian_Dennehy
    /wiki/Ben_Kingsley
    /wiki/William_H._Macy
    /wiki/Al_Pacino
    /wiki/Geoffrey_Rush
    /wiki/Paul_Newman
    /wiki/Jeremy_Irons
    /wiki/Kevin_Kline
    /wiki/Paul_Giamatti
    /wiki/Al_Pacino
    /wiki/Paul_Giamatti
    /wiki/Kevin_Costner
    /wiki/Michael_Douglas
    /wiki/Mark_Ruffalo
    /wiki/Idris_Elba
    /wiki/Bryan_Cranston
    /wiki/Alexander_Skarsg%C3%A5rd
    /wiki/Virtual_International_Authority_File
    /wiki/Library_of_Congress_Control_Number
    /wiki/International_Standard_Name_Identifier
    /wiki/Integrated_Authority_File
    /wiki/Syst%C3%A8me_universitaire_de_documentation
    /wiki/Biblioth%C3%A8que_nationale_de_France
    /wiki/MusicBrainz
    /wiki/Biblioteca_Nacional_de_Espa%C3%B1a
    /wiki/SNAC


硬编码的爬虫，在实际中使用是很无用的，下面是改进的写法。


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')

while(len(links)) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))


    /wiki/Apollo_13_(film)
    /wiki/Charlie_Rose_(TV_series)
    /wiki/CNN
    /wiki/HBO_Hits
    /wiki/DreamWorks
    /wiki/CNBC_Europe
    /wiki/Cablecom
    /wiki/Canal_(TV_Provider)
    /wiki/Evo_TV
    /wiki/Fox_Broadcasting_Company
    /wiki/Fox_(Norway)
    /wiki/WNYW
    /wiki/Shine_Group
    /wiki/Star_World_India
    /wiki/Fox_(Norway)
    /wiki/TCM_Nordic
    /wiki/Viasat_Series
    /wiki/Viasat_Film_Family
    /wiki/Eurosport_2
    /wiki/192TV
    /wiki/Nickelodeon_(Netherlands)
    /wiki/MTV_Sweden
    /wiki/VidCon
    /wiki/Nick_Records
    /wiki/Bellator_Kickboxing
    /wiki/Kickboxing
    /wiki/Muay_Thai#Knee
    /wiki/Pra_Jiad
    /wiki/Clothing
    /wiki/Fur_farming
    /wiki/Medicinal_fungi
    /wiki/PubMed_Identifier
    /wiki/PubMed_Identifier
    /wiki/Entrez
    /wiki/Epidemiology
    /wiki/Asymptomatic_carrier
    /wiki/Family_planning
    /wiki/Abortion_in_Panama#Alternatives_to_abortion
    /wiki/Abortion_in_Northern_Cyprus
    /wiki/Late-term_abortion#Legal_restrictions_on_later_abortion
    /wiki/Birth_control
    /wiki/Hormone_replacement_therapy
    /wiki/Esterified_estrogens
    /wiki/Brilanestrant
    /wiki/Quercetin
    /wiki/Karanjachromene
    /wiki/Xanthorhamnin
    /wiki/Quercetin_3,4%27-diglucoside
    /wiki/Xanthorhamnin
    /wiki/Quercetagetin
    /wiki/Rhamnazin
    /wiki/3,7-dimethylquercetin_4%27-O-methyltransferase
    /wiki/Betaine-homocysteine_S-methyltransferase
    /wiki/Glutaryl-CoA_dehydrogenase
    /wiki/Glutathione_synthetase
    /wiki/Ligase
    /wiki/Tyrosine%E2%80%94tRNA_ligase
    /wiki/Holocarboxylase_synthetase
    /wiki/Locus_(genetics)
    /wiki/Heterozygote
    /wiki/True_breeding_organism
    /wiki/Allele
    /wiki/Blood_transfusion
    /wiki/Sodium_phosphates
    /wiki/Sodium_ferrocyanide
    /wiki/Sodium_acetate
    /wiki/Ion
    /wiki/Radical_(chemistry)
    /wiki/Unpaired_electron
    /wiki/Atom
    /wiki/International_Standard_Book_Number
    /wiki/ISO_9660
    /wiki/PDF/E
    /wiki/ISO_15924
    /wiki/ISO/IEC_8859
    /wiki/ISO_26000
    /wiki/ISO/IEC_19752
    /wiki/ISO/IEC_9126
    /wiki/ISO/IEC_14443
    /wiki/ISO_31-0
    /wiki/ISO_704
    /wiki/ISO/IEC_10967
    /wiki/ISO_2145
    /wiki/ISO_5427
    /wiki/Digital_object_identifier
    /wiki/ISO/IEC_11179
    /wiki/Romanization_of_Georgian
    /wiki/ISO/IEC_9126
    /wiki/Shoe_size
    /wiki/ISO_11784_%26_11785
    /wiki/ISO_999
    /wiki/PDF/A
    /wiki/ISO_8501-1
    /wiki/ISO/IEC_18000
    /wiki/Kappa_number
    /wiki/Pulp_and_paper_industry_in_the_United_States
    /wiki/Felling
    /wiki/Deforestation
    /wiki/Madagascar
    /wiki/International_Standard_Book_Number
    /wiki/Library_of_Congress
    /wiki/Congressional_caucus
    /wiki/United_States_congressional_committee
    /wiki/Sponsor_(legislative)
    /wiki/Markup_(legislation)
    /wiki/Senatorial_courtesy
    /wiki/National_Statuary_Hall
    /wiki/John_Sevier
    /wiki/Tipton-Haynes_State_Historic_Site
    /wiki/National_Register_of_Historic_Places_listings_in_American_Samoa
    /wiki/National_Register_of_Historic_Places_listings_in_Missouri
    /wiki/National_Register_of_Historic_Places_listings_in_California
    /wiki/National_Register_of_Historic_Places_listings_in_San_Francisco,_California
    /wiki/Western_Addition,_San_Francisco,_California
    /wiki/Scott_Wiener
    /wiki/Bob_Wieckowski
    /wiki/Incumbent
    /wiki/International_Standard_Serial_Number
    /wiki/ISO_6344
    /wiki/JBIG
    /wiki/ISO_15926
    /wiki/ISO_7027
    /wiki/ISO_14651
    /wiki/ISO_19114
    /wiki/ISO_28000
    /wiki/British_Standard_Pipe
    /wiki/ISO_9000
    /wiki/On-board_diagnostics
    /wiki/Multibus
    /wiki/ACCESS.bus
    /wiki/System_Management_Bus
    /wiki/Serial_Digital_Video_Out
    /wiki/Tablet_computer#Intel_tablet_platforms
    /wiki/2-in-1_PC
    /wiki/Calculator
    /wiki/Reverse_Polish_notation
    /wiki/HP-12C
    /wiki/Liquid_crystal_display
    /wiki/Computer_monitor
    /wiki/Color_difference
    /wiki/White
    /wiki/Trinity_Sunday
    /wiki/Andrei_Rublev
    /wiki/Theotokos
    /wiki/Feast_of_Our_Lady_of_Snows
    /wiki/Latin_language
    /wiki/Frontinus
    /wiki/The_Silver_Pigs
    /wiki/The_year_of_the_four_emperors
    /wiki/Roman_governors_of_Germania_Inferior
    /wiki/Lucius_Neratius_Priscus
    /wiki/Chiron_(journal)
    /wiki/Verlag_C._H._Beck
    /wiki/Outline_of_books#Countries_and_books
    /wiki/History_of_the_book_in_Brazil
    /wiki/Coastline_of_Brazil
    /wiki/Santa_Catarina_(island)
    /wiki/Pirajuba%C3%A9_Marine_Extractive_Reserve
    /wiki/Chico_Mendes_Institute_for_Biodiversity_Conservation
    /wiki/Chico_Mendes
    /wiki/Marxism
    /wiki/Marxist_archaeology



    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-6-5923deb220a6> in <module>()
         17     newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
         18     print(newArticle)
    ---> 19     links = getLinks(newArticle)
    

    <ipython-input-6-5923deb220a6> in getLinks(articleUrl)
          9 def getLinks(articleUrl):
         10     html = urlopen('http://en.wikipedia.org' + articleUrl)
    ---> 11     bsObj = BeautifulSoup(html)
         12     return bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
         13 


    ~/anaconda3/lib/python3.6/site-packages/bs4/__init__.py in __init__(self, markup, features, builder, parse_only, from_encoding, exclude_encodings, **kwargs)
        189 
        190         if hasattr(markup, 'read'):        # It's a file-type object.
    --> 191             markup = markup.read()
        192         elif len(markup) <= 256 and (
        193                 (isinstance(markup, bytes) and not b'<' in markup)


    ~/anaconda3/lib/python3.6/http/client.py in read(self, amt)
        460             else:
        461                 try:
    --> 462                     s = self._safe_read(self.length)
        463                 except IncompleteRead:
        464                     self._close_conn()


    ~/anaconda3/lib/python3.6/http/client.py in _safe_read(self, amt)
        610         s = []
        611         while amt > 0:
    --> 612             chunk = self.fp.read(min(amt, MAXAMOUNT))
        613             if not chunk:
        614                 raise IncompleteRead(b''.join(s), amt)


    ~/anaconda3/lib/python3.6/socket.py in readinto(self, b)
        584         while True:
        585             try:
    --> 586                 return self._sock.recv_into(b)
        587             except timeout:
        588                 self._timeout_occurred = True


    ~/anaconda3/lib/python3.6/ssl.py in recv_into(self, buffer, nbytes, flags)
       1007                   "non-zero flags not allowed in calls to recv_into() on %s" %
       1008                   self.__class__)
    -> 1009             return self.read(nbytes, buffer)
       1010         else:
       1011             return socket.recv_into(self, buffer, nbytes, flags)


    ~/anaconda3/lib/python3.6/ssl.py in read(self, len, buffer)
        869             raise ValueError("Read on closed or unwrapped SSL socket.")
        870         try:
    --> 871             return self._sslobj.read(len, buffer)
        872         except SSLError as x:
        873             if x.args[0] == SSL_ERROR_EOF and self.suppress_ragged_eofs:


    ~/anaconda3/lib/python3.6/ssl.py in read(self, len, buffer)
        629         """
        630         if buffer is not None:
    --> 631             v = self._sslobj.read(len, buffer)
        632         else:
        633             v = self._sslobj.read(len)


    KeyboardInterrupt: 


### 整站爬取有什么用途？

- 生成全站地图
- 收集数据

### 方法

通常是先从顶层页面爬取，比如主页，然后搜寻该页面上的所有链接，然后爬取这些链接，每一个链接对应的页面上还有一些其他链接。可以用队列来组织。一轮一轮去爬取。

显然，如果这样去直接执行，不做过滤，任务量是要爆炸的。而这些链接的链接，很多是重复的，加上判重的逻辑，能够大量减轻任务量，但是只是用简单的循环判重，这个任务量也是很重的，所以有个神器就是：布隆过滤器。


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set() # 集合有去重特效

def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html)
    
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: # 用的是集合，这步不多余吗
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage) 
getLinks('')
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))


    /wiki/Wikipedia
    /wiki/Wikipedia:Protection_policy#semi
    /wiki/Wikipedia:Requests_for_page_protection
    /wiki/Wikipedia:Requests_for_permissions
    /wiki/Wikipedia:Requesting_copyright_permission
    /wiki/Wikipedia:User_access_levels
    /wiki/Wikipedia:Requests_for_adminship
    /wiki/Wikipedia:Protection_policy#extended
    /wiki/Wikipedia:Lists_of_protected_pages
    /wiki/Wikipedia:Protection_policy
    /wiki/Wikipedia:Perennial_proposals
    /wiki/Wikipedia:Project_namespace#How-to_and_information_pages
    /wiki/Wikipedia:Protection_policy#move
    /wiki/Wikipedia:WPPP
    /wiki/File:People_icon.svg
    /wiki/Special:WhatLinksHere/File:People_icon.svg
    /wiki/Help:What_links_here
    /wiki/Wikipedia:Policies_and_guidelines
    /wiki/Wikipedia:Shortcut
    /wiki/Wikipedia:Keyboard_shortcuts
    /wiki/Wikipedia:WikiProject_Kansas
    /wiki/Wikipedia:WikiProject
    /wiki/Wikipedia:Wikimedia_sister_projects
    /wiki/Help:Interwikimedia_links
    /wiki/Help:Interlanguage_links
    /wiki/List_of_ISO_639-1_codes
    /wiki/File:Question_book-new.svg
    /wiki/Wikipedia:Protection_policy#full
    /wiki/Wikipedia:Child_protection
    /wiki/Wikipedia:Biographies_of_living_persons
    /wiki/Wikipedia:Biographies_of_living_persons/Noticeboard
    /wiki/Template:Noticeboard_links



    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-10-1001c09b2061> in <module>()
         17                 pages.add(newPage)
         18                 getLinks(newPage)
    ---> 19 getLinks('')
    

    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
         16                 print(newPage)
         17                 pages.add(newPage)
    ---> 18                 getLinks(newPage)
         19 getLinks('')


    <ipython-input-10-1001c09b2061> in getLinks(pageUrl)
          7 def getLinks(pageUrl):
          8     global pages
    ----> 9     html = urlopen('http://en.wikipedia.org' + pageUrl)
         10     bsObj = BeautifulSoup(html)
         11 


    ~/anaconda3/lib/python3.6/urllib/request.py in urlopen(url, data, timeout, cafile, capath, cadefault, context)
        221     else:
        222         opener = _opener
    --> 223     return opener.open(url, data, timeout)
        224 
        225 def install_opener(opener):


    ~/anaconda3/lib/python3.6/urllib/request.py in open(self, fullurl, data, timeout)
        524             req = meth(req)
        525 
    --> 526         response = self._open(req, data)
        527 
        528         # post-process response


    ~/anaconda3/lib/python3.6/urllib/request.py in _open(self, req, data)
        542         protocol = req.type
        543         result = self._call_chain(self.handle_open, protocol, protocol +
    --> 544                                   '_open', req)
        545         if result:
        546             return result


    ~/anaconda3/lib/python3.6/urllib/request.py in _call_chain(self, chain, kind, meth_name, *args)
        502         for handler in handlers:
        503             func = getattr(handler, meth_name)
    --> 504             result = func(*args)
        505             if result is not None:
        506                 return result


    ~/anaconda3/lib/python3.6/urllib/request.py in http_open(self, req)
       1344 
       1345     def http_open(self, req):
    -> 1346         return self.do_open(http.client.HTTPConnection, req)
       1347 
       1348     http_request = AbstractHTTPHandler.do_request_


    ~/anaconda3/lib/python3.6/urllib/request.py in do_open(self, http_class, req, **http_conn_args)
       1316             try:
       1317                 h.request(req.get_method(), req.selector, req.data, headers,
    -> 1318                           encode_chunked=req.has_header('Transfer-encoding'))
       1319             except OSError as err: # timeout error
       1320                 raise URLError(err)


    ~/anaconda3/lib/python3.6/http/client.py in request(self, method, url, body, headers, encode_chunked)
       1237                 encode_chunked=False):
       1238         """Send a complete request to the server."""
    -> 1239         self._send_request(method, url, body, headers, encode_chunked)
       1240 
       1241     def _send_request(self, method, url, body, headers, encode_chunked):


    ~/anaconda3/lib/python3.6/http/client.py in _send_request(self, method, url, body, headers, encode_chunked)
       1283             # default charset of iso-8859-1.
       1284             body = _encode(body, 'body')
    -> 1285         self.endheaders(body, encode_chunked=encode_chunked)
       1286 
       1287     def getresponse(self):


    ~/anaconda3/lib/python3.6/http/client.py in endheaders(self, message_body, encode_chunked)
       1232         else:
       1233             raise CannotSendHeader()
    -> 1234         self._send_output(message_body, encode_chunked=encode_chunked)
       1235 
       1236     def request(self, method, url, body=None, headers={}, *,


    ~/anaconda3/lib/python3.6/http/client.py in _send_output(self, message_body, encode_chunked)
       1024         msg = b"\r\n".join(self._buffer)
       1025         del self._buffer[:]
    -> 1026         self.send(msg)
       1027 
       1028         if message_body is not None:


    ~/anaconda3/lib/python3.6/http/client.py in send(self, data)
        962         if self.sock is None:
        963             if self.auto_open:
    --> 964                 self.connect()
        965             else:
        966                 raise NotConnected()


    ~/anaconda3/lib/python3.6/http/client.py in connect(self)
        934         """Connect to the host and port specified in __init__."""
        935         self.sock = self._create_connection(
    --> 936             (self.host,self.port), self.timeout, self.source_address)
        937         self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        938 


    ~/anaconda3/lib/python3.6/socket.py in create_connection(address, timeout, source_address)
        711             if source_address:
        712                 sock.bind(source_address)
    --> 713             sock.connect(sa)
        714             # Break explicitly a reference cycle
        715             err = None


    KeyboardInterrupt: 


# 爬 + 取数据


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('Something missed in this page!')
    for link in bsObj.findAll('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('--------\n' + newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))


    Main Page
    <p><b><a href="/wiki/Naruto_Uzumaki" title="Naruto Uzumaki">Naruto Uzumaki</a></b> is the fictional <a href="/wiki/Protagonist" title="Protagonist">protagonist</a> of the Japanese <a href="/wiki/Manga" title="Manga">manga</a> series <i><a href="/wiki/Naruto" title="Naruto">Naruto</a></i>, created by <a href="/wiki/Masashi_Kishimoto" title="Masashi Kishimoto">Masashi Kishimoto</a>. A carefree, optimistic and boisterous teen <a href="/wiki/Ninja" title="Ninja">ninja</a> who befriends other ninja, he aspires to become the leader of his fictional village, <a class="mw-redirect" href="/wiki/World_of_Naruto#Konohagakure" title="World of Naruto">Konohagakure</a>. He appears in <a href="/wiki/Anime" title="Anime">anime</a>, films, video games and <a href="/wiki/Original_video_animation" title="Original video animation">original video animations</a>, as well as a sequel <i><a href="/wiki/Boruto:_Naruto_Next_Generations" title="Boruto: Naruto Next Generations">Boruto: Naruto Next Generations</a></i>, with his son <a href="/wiki/Boruto_Uzumaki" title="Boruto Uzumaki">Boruto Uzumaki</a> as the protagonist. Kishimoto initially aimed to keep the character "simple and stupid", while giving him many attributes of an ideal hero, and a tragic past. The author has revised Naruto's image many times, providing the character with different clothes intended to appeal to Western audiences and to make him easier to illustrate. Naruto is voiced by <a href="/wiki/Junko_Takeuchi" title="Junko Takeuchi">Junko Takeuchi</a> <i>(pictured)</i> in the original animated series and <a href="/wiki/Maile_Flanagan" title="Maile Flanagan">Maile Flanagan</a> in the English adaptations. The character's development has been praised by anime and manga publications, and has drawn scholarly attention. (<a href="/wiki/Naruto_Uzumaki" title="Naruto Uzumaki"><b>Full article...</b></a>)</p>
    Something missed in this page!
    --------
    /wiki/Wikipedia
    Wikipedia
    <p><b>Wikipedia</b> (<span class="nowrap"><span class="IPA nopopups noexcerpt"><a href="/wiki/Help:IPA/English" title="Help:IPA/English">/<span style="border-bottom:1px dotted"><span title="/ˌ/: secondary stress follows">ˌ</span><span title="'w' in 'wind'">w</span><span title="/ɪ/: 'i' in 'kit'">ɪ</span><span title="'k' in 'kind'">k</span><span title="/ɪ/: 'i' in 'kit'">ɪ</span><span title="/ˈ/: primary stress follows">ˈ</span><span title="'p' in 'pie'">p</span><span title="/iː/: 'ee' in 'fleece'">iː</span><span title="'d' in 'dye'">d</span><span title="/i/: 'y' in 'happy'">i</span><span title="/ə/: 'a' in 'about'">ə</span></span>/</a></span><small class="nowrap"> (<span class="unicode haudio"><span class="fn"><span style="white-space:nowrap"><a href="/wiki/File:En-uk-Wikipedia.ogg" title="About this sound"><img alt="About this sound" data-file-height="20" data-file-width="20" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/11px-Loudspeaker.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/17px-Loudspeaker.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/22px-Loudspeaker.svg.png 2x" width="11"/></a> </span><a class="internal" href="//upload.wikimedia.org/wikipedia/commons/c/c5/En-uk-Wikipedia.ogg" title="En-uk-Wikipedia.ogg">listen</a></span></span>)</small></span>, <span class="nowrap"><span class="IPA nopopups noexcerpt"><a href="/wiki/Help:IPA/English" title="Help:IPA/English">/<span style="border-bottom:1px dotted"><span title="/ˌ/: secondary stress follows">ˌ</span><span title="'w' in 'wind'">w</span><span title="/ɪ/: 'i' in 'kit'">ɪ</span><span title="'k' in 'kind'">k</span><span title="/i/: 'y' in 'happy'">i</span><span title="/ˈ/: primary stress follows">ˈ</span><span title="'p' in 'pie'">p</span><span title="/iː/: 'ee' in 'fleece'">iː</span><span title="'d' in 'dye'">d</span><span title="/i/: 'y' in 'happy'">i</span><span title="/ə/: 'a' in 'about'">ə</span></span>/</a></span><small class="nowrap"> (<span class="unicode haudio"><span class="fn"><span style="white-space:nowrap"><a href="/wiki/File:En-us-Wikipedia.ogg" title="About this sound"><img alt="About this sound" data-file-height="20" data-file-width="20" height="11" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/11px-Loudspeaker.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/17px-Loudspeaker.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/22px-Loudspeaker.svg.png 2x" width="11"/></a> </span><a class="internal" href="//upload.wikimedia.org/wikipedia/commons/2/2e/En-us-Wikipedia.ogg" title="En-us-Wikipedia.ogg">listen</a></span></span>)</small></span> <a href="/wiki/Help:Pronunciation_respelling_key" title="Help:Pronunciation respelling key"><i title="English pronunciation respelling"><span style="font-size:90%">WIK</span>-ih-<span style="font-size:90%">PEE</span>-dee-ə</i></a>) is a multilingual, web-based, free-content <a href="/wiki/Encyclopedia" title="Encyclopedia">encyclopedia</a> that is based on a model of openly editable content. It is the largest and most-popular general reference work on the Internet,<sup class="reference" id="cite_ref-Tancer_5-0"><a href="#cite_note-Tancer-5">[3]</a></sup><sup class="reference" id="cite_ref-Woodson_6-0"><a href="#cite_note-Woodson-6">[4]</a></sup><sup class="reference" id="cite_ref-7"><a href="#cite_note-7">[5]</a></sup> and is named as one of the most popular websites.<sup class="reference" id="cite_ref-Alexa_siteinfo_8-0"><a href="#cite_note-Alexa_siteinfo-8">[6]</a></sup> It is owned and supported by the <a href="/wiki/Wikimedia_Foundation" title="Wikimedia Foundation">Wikimedia Foundation</a>, a <a href="/wiki/501(c)(3)_organization" title="501(c)(3) organization">non-profit organization</a> which operates on whatever money it receives from its annual fund drives.<sup class="reference" id="cite_ref-9"><a href="#cite_note-9">[7]</a></sup><sup class="reference" id="cite_ref-10"><a href="#cite_note-10">[8]</a></sup><sup class="reference" id="cite_ref-11"><a href="#cite_note-11">[9]</a></sup></p>
    Something missed in this page!
    --------
    /wiki/Wikipedia:Protection_policy#semi
    Wikipedia:Protection policy
    <p>Wikipedia is built around the principle that <a href="/wiki/Wiki" title="Wiki">anyone can edit it</a>, and it therefore aims to have as many of its pages as possible open for public editing so that anyone can add material and correct errors. However, in some particular circumstances, because of a specifically identified likelihood of damage resulting if editing is left open, some individual pages may need to be subject to technical restrictions (often only temporary but sometimes indefinitely) on who is permitted to modify them. The placing of such restrictions on pages is called <b>protection</b>.</p>
    Something missed in this page!
    --------
    /wiki/Wikipedia:Requests_for_page_protection
    Wikipedia:Requests for page protection
    <p>This page is for requesting that a page, file or template be <b>fully protected</b>, <b>create protected</b> (<a href="/wiki/Wikipedia:Protection_policy#Creation_protection" title="Wikipedia:Protection policy">salted</a>), <b>extended confirmed protected</b>, <b>semi-protected</b>, added to <b>pending changes</b>, <b>move-protected</b>, <b>template protected</b> (template-specific), <b>upload protected</b> (file-specific), or <b>unprotected</b>. Please read up on the <a href="/wiki/Wikipedia:Protection_policy" title="Wikipedia:Protection policy">protection policy</a>. Full protection is used to stop edit warring between multiple users or to prevent vandalism to <a href="/wiki/Wikipedia:High-risk_templates" title="Wikipedia:High-risk templates">high-risk templates</a>; semi-protection and pending changes are usually used only to prevent IP and new user vandalism (see the <a href="/wiki/Wikipedia:Rough_guide_to_semi-protection" title="Wikipedia:Rough guide to semi-protection">rough guide to semi-protection</a>); and move protection is used to stop <a href="/wiki/Wikipedia:Moving_a_page" title="Wikipedia:Moving a page">pagemove</a> revert wars. Extended confirmed protection is used where semi-protection has proved insufficient (see the <a href="/wiki/Wikipedia:Rough_guide_to_extended_confirmed_protection" title="Wikipedia:Rough guide to extended confirmed protection">rough guide to extended confirmed protection</a>)</p>
    /w/index.php?title=Wikipedia:Requests_for_page_protection&action=edit
    --------
    /wiki/Wikipedia:Requests_for_permissions
    Wikipedia:Requests for permissions
    <p><span class="sysop-show" id="coordinates"><a href="/wiki/Wikipedia:Requests_for_permissions/Administrator_instructions" title="Wikipedia:Requests for permissions/Administrator instructions">Administrator instructions</a></span></p>
    Something missed in this page!
    --------
    /wiki/Wikipedia:Requesting_copyright_permission
    Wikipedia:Requesting copyright permission
    <p>To use copyrighted material on Wikipedia, it is <i>not enough</i> that we have permission to use it on Wikipedia alone. That's because Wikipedia itself states all its material may be used by anyone, for any purpose. So we have to be sure all material is in fact licensed for that purpose, whoever provided it.</p>
    Something missed in this page!
    --------
    /wiki/Wikipedia:User_access_levels
    Wikipedia:User access levels
    <p>The <b>user access level</b> of editors affects their abilities to perform certain actions on Wikipedia; it depends on which <i>rights</i> (also called <i>permissions</i>, <i><a href="/wiki/Internet_forum#User_groups" title="Internet forum">user groups</a></i>, <a class="mw-redirect" href="/wiki/Bit_(computing)" title="Bit (computing)"><i>bits</i></a> or <a class="mw-redirect" href="/wiki/Flag_(computing)" title="Flag (computing)"><i>flags</i></a>) are assigned to accounts. This is determined by whether the editor is <a class="mw-redirect" href="/wiki/Wikipedia:Logging_in" title="Wikipedia:Logging in">logged into</a> an account, and whether the account has a sufficient age and number of edits for certain automatic rights, and what additional rights have been assigned manually to the account.</p>
    Something missed in this page!
    --------
    /wiki/Wikipedia:Requests_for_adminship
    Wikipedia:Requests for adminship
    <p><input class="mw-inputbox-input searchboxInput mw-ui-input mw-ui-input-inline" dir="ltr" name="search" placeholder="" size="30" type="text" value=""/><input name="prefix" type="hidden" value="Wikipedia:Requests for adminship/"/><br/>
    <input class="mw-ui-button" name="fulltext" type="submit" value="Search RfA"/><input name="fulltext" type="hidden" value="Search"/></p>
    Something missed in this page!
    --------
    /wiki/Wikipedia:Protection_policy#extended
    Wikipedia:Protection policy
    <p>Wikipedia is built around the principle that <a href="/wiki/Wiki" title="Wiki">anyone can edit it</a>, and it therefore aims to have as many of its pages as possible open for public editing so that anyone can add material and correct errors. However, in some particular circumstances, because of a specifically identified likelihood of damage resulting if editing is left open, some individual pages may need to be subject to technical restrictions (often only temporary but sometimes indefinitely) on who is permitted to modify them. The placing of such restrictions on pages is called <b>protection</b>.</p>
    Something missed in this page!
    --------
    /wiki/Wikipedia:Lists_of_protected_pages
    Wikipedia:Lists of protected pages
    <p>This is a list of resources available that list pages that are <b><a href="/wiki/Wikipedia:Protection_policy" title="Wikipedia:Protection policy">protected</a></b>, <b><a href="/wiki/Wikipedia:Protection_policy#Semi-protection" title="Wikipedia:Protection policy">semi-protected</a></b> or <b><a href="/wiki/Wikipedia:Protection_policy#Move_protected" title="Wikipedia:Protection policy">move protected</a>.</b></p>
    Something missed in this page!
    --------
    /wiki/Wikipedia:Protection_policy
    Wikipedia:Protection policy
    <p>Wikipedia is built around the principle that <a href="/wiki/Wiki" title="Wiki">anyone can edit it</a>, and it therefore aims to have as many of its pages as possible open for public editing so that anyone can add material and correct errors. However, in some particular circumstances, because of a specifically identified likelihood of damage resulting if editing is left open, some individual pages may need to be subject to technical restrictions (often only temporary but sometimes indefinitely) on who is permitted to modify them. The placing of such restrictions on pages is called <b>protection</b>.</p>
    Something missed in this page!
    --------
    /wiki/Wikipedia:Perennial_proposals
    Wikipedia:Perennial proposals
    <p>This is a list of things that are frequently proposed on Wikipedia, and have been <a class="mw-redirect" href="/wiki/Wikipedia:Rejected_proposals" title="Wikipedia:Rejected proposals">rejected by the community</a> several times in the past. It should be noted that merely listing something on this page does not mean it will never happen, but that it has been discussed before and never met consensus. <a class="mw-redirect" href="/wiki/Wikipedia:Consensus_can_change" title="Wikipedia:Consensus can change">Consensus can change</a>, and some proposals that remained on this page for a long time have finally been proposed in a way that reached consensus, but you should address rebuttals raised in the past if you make a proposal along these lines. If you feel you would still like to do one of these proposals, then raise it at the <a href="/wiki/Wikipedia:Village_pump" title="Wikipedia:Village pump">Wikipedia:Village pump</a>.</p>
    /w/index.php?title=Wikipedia:Perennial_proposals&action=edit
    --------
    /wiki/Wikipedia:Project_namespace#How-to_and_information_pages



    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-12-dc8e1aeb1c0b> in <module>()
         21                 pages.add(newPage)
         22                 getLinks(newPage)
    ---> 23 getLinks('')
    

    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
         20                 print('--------\n' + newPage)
         21                 pages.add(newPage)
    ---> 22                 getLinks(newPage)
         23 getLinks('')


    <ipython-input-12-dc8e1aeb1c0b> in getLinks(pageUrl)
          6 def getLinks(pageUrl):
          7     global pages
    ----> 8     html = urlopen('http://en.wikipedia.org' + pageUrl)
          9     bsObj = BeautifulSoup(html)
         10     try:


    ~/anaconda3/lib/python3.6/urllib/request.py in urlopen(url, data, timeout, cafile, capath, cadefault, context)
        221     else:
        222         opener = _opener
    --> 223     return opener.open(url, data, timeout)
        224 
        225 def install_opener(opener):


    ~/anaconda3/lib/python3.6/urllib/request.py in open(self, fullurl, data, timeout)
        524             req = meth(req)
        525 
    --> 526         response = self._open(req, data)
        527 
        528         # post-process response


    ~/anaconda3/lib/python3.6/urllib/request.py in _open(self, req, data)
        542         protocol = req.type
        543         result = self._call_chain(self.handle_open, protocol, protocol +
    --> 544                                   '_open', req)
        545         if result:
        546             return result


    ~/anaconda3/lib/python3.6/urllib/request.py in _call_chain(self, chain, kind, meth_name, *args)
        502         for handler in handlers:
        503             func = getattr(handler, meth_name)
    --> 504             result = func(*args)
        505             if result is not None:
        506                 return result


    ~/anaconda3/lib/python3.6/urllib/request.py in http_open(self, req)
       1344 
       1345     def http_open(self, req):
    -> 1346         return self.do_open(http.client.HTTPConnection, req)
       1347 
       1348     http_request = AbstractHTTPHandler.do_request_


    ~/anaconda3/lib/python3.6/urllib/request.py in do_open(self, http_class, req, **http_conn_args)
       1319             except OSError as err: # timeout error
       1320                 raise URLError(err)
    -> 1321             r = h.getresponse()
       1322         except:
       1323             h.close()


    ~/anaconda3/lib/python3.6/http/client.py in getresponse(self)
       1329         try:
       1330             try:
    -> 1331                 response.begin()
       1332             except ConnectionError:
       1333                 self.close()


    ~/anaconda3/lib/python3.6/http/client.py in begin(self)
        295         # read until we get a non-100 response
        296         while True:
    --> 297             version, status, reason = self._read_status()
        298             if status != CONTINUE:
        299                 break


    ~/anaconda3/lib/python3.6/http/client.py in _read_status(self)
        256 
        257     def _read_status(self):
    --> 258         line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
        259         if len(line) > _MAXLINE:
        260             raise LineTooLong("status line")


    ~/anaconda3/lib/python3.6/socket.py in readinto(self, b)
        584         while True:
        585             try:
    --> 586                 return self._sock.recv_into(b)
        587             except timeout:
        588                 self._timeout_occurred = True


    KeyboardInterrupt: 


到目前为止，数据都没有真正保存，而是通过`print`打印出来看看，在第五章会重点学习如何存储数据。

### 爬取互联网

一个小目标：如何创建谷歌？答案是分成两步：

- 有足够的钱买大量的数据仓库
- 构建爬虫

所以本质上，搜索引擎谷歌是个爬虫公司。

1994年谷歌刚刚创建时，他们只有一个老的服务器和一个Python爬虫。

严肃一点说，爬虫是许许多多现代web技术的核心。

## 下面是更灵活的一个爬虫写法


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set() # 仍然用集合的方法
random.seed(datetime.datetime.now())

# 从页面上提取内部链接
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找到以`/`开头的链接或者是`.`开头的
    for link in bsObj.findAll('a',href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 从页面上提取所有的外部链接
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 寻找以www或者http开头且不包含当前链接的链接
    for link in bsObj.findAll('a',href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace('http://','').split('/')
    return addressParts

# 返回一个单个链接
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj,splitAddress(startingPage)[0])
    if len(externalLinks) == 0: # 如果当前页面不包含外部链接，再随机从内部链接中取得外部链接
        internalLinks = getInternalLinks(startingPage,splitAddress(startingPage)[0])
        return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks) - 1)] # 否则就随机选择一个输出即可
def getNextExternalLink():
    pass

def followExternalOnly(startingPage):
    externalLink = getRandomExternalLink(startingPage)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink) # 递归调用

followExternalOnly('http://oreilly.com')
    
```

    /Users/rick/anaconda3/lib/python3.6/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    The code that caused this warning is on line 193 of the file /Users/rick/anaconda3/lib/python3.6/runpy.py. To get rid of this warning, change code that looks like this:
    
     BeautifulSoup(YOUR_MARKUP})
    
    to this:
    
     BeautifulSoup(YOUR_MARKUP, "lxml")
    
      markup_type=markup_type))


    Random external link is: https://www.youtube.com/user/OreillyMedia



    ---------------------------------------------------------------------------

    TimeoutError                              Traceback (most recent call last)

    ~/anaconda3/lib/python3.6/urllib/request.py in do_open(self, http_class, req, **http_conn_args)
       1317                 h.request(req.get_method(), req.selector, req.data, headers,
    -> 1318                           encode_chunked=req.has_header('Transfer-encoding'))
       1319             except OSError as err: # timeout error


    ~/anaconda3/lib/python3.6/http/client.py in request(self, method, url, body, headers, encode_chunked)
       1238         """Send a complete request to the server."""
    -> 1239         self._send_request(method, url, body, headers, encode_chunked)
       1240 


    ~/anaconda3/lib/python3.6/http/client.py in _send_request(self, method, url, body, headers, encode_chunked)
       1284             body = _encode(body, 'body')
    -> 1285         self.endheaders(body, encode_chunked=encode_chunked)
       1286 


    ~/anaconda3/lib/python3.6/http/client.py in endheaders(self, message_body, encode_chunked)
       1233             raise CannotSendHeader()
    -> 1234         self._send_output(message_body, encode_chunked=encode_chunked)
       1235 


    ~/anaconda3/lib/python3.6/http/client.py in _send_output(self, message_body, encode_chunked)
       1025         del self._buffer[:]
    -> 1026         self.send(msg)
       1027 


    ~/anaconda3/lib/python3.6/http/client.py in send(self, data)
        963             if self.auto_open:
    --> 964                 self.connect()
        965             else:


    ~/anaconda3/lib/python3.6/http/client.py in connect(self)
       1391 
    -> 1392             super().connect()
       1393 


    ~/anaconda3/lib/python3.6/http/client.py in connect(self)
        935         self.sock = self._create_connection(
    --> 936             (self.host,self.port), self.timeout, self.source_address)
        937         self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)


    ~/anaconda3/lib/python3.6/socket.py in create_connection(address, timeout, source_address)
        723     if err is not None:
    --> 724         raise err
        725     else:


    ~/anaconda3/lib/python3.6/socket.py in create_connection(address, timeout, source_address)
        712                 sock.bind(source_address)
    --> 713             sock.connect(sa)
        714             # Break explicitly a reference cycle


    TimeoutError: [Errno 60] Operation timed out

    
    During handling of the above exception, another exception occurred:


    URLError                                  Traceback (most recent call last)

    <ipython-input-4-cc24a0fc5dc5> in <module>()
         50     followExternalOnly(externalLink) # 递归调用
         51 
    ---> 52 followExternalOnly('http://oreilly.com')
         53 


    <ipython-input-4-cc24a0fc5dc5> in followExternalOnly(startingPage)
         48     externalLink = getRandomExternalLink(startingPage)
         49     print("Random external link is: " + externalLink)
    ---> 50     followExternalOnly(externalLink) # 递归调用
         51 
         52 followExternalOnly('http://oreilly.com')


    <ipython-input-4-cc24a0fc5dc5> in followExternalOnly(startingPage)
         46 
         47 def followExternalOnly(startingPage):
    ---> 48     externalLink = getRandomExternalLink(startingPage)
         49     print("Random external link is: " + externalLink)
         50     followExternalOnly(externalLink) # 递归调用


    <ipython-input-4-cc24a0fc5dc5> in getRandomExternalLink(startingPage)
         34 # 返回一个单个链接
         35 def getRandomExternalLink(startingPage):
    ---> 36     html = urlopen(startingPage)
         37     bsObj = BeautifulSoup(html)
         38     externalLinks = getExternalLinks(bsObj,splitAddress(startingPage)[0])


    ~/anaconda3/lib/python3.6/urllib/request.py in urlopen(url, data, timeout, cafile, capath, cadefault, context)
        221     else:
        222         opener = _opener
    --> 223     return opener.open(url, data, timeout)
        224 
        225 def install_opener(opener):


    ~/anaconda3/lib/python3.6/urllib/request.py in open(self, fullurl, data, timeout)
        524             req = meth(req)
        525 
    --> 526         response = self._open(req, data)
        527 
        528         # post-process response


    ~/anaconda3/lib/python3.6/urllib/request.py in _open(self, req, data)
        542         protocol = req.type
        543         result = self._call_chain(self.handle_open, protocol, protocol +
    --> 544                                   '_open', req)
        545         if result:
        546             return result


    ~/anaconda3/lib/python3.6/urllib/request.py in _call_chain(self, chain, kind, meth_name, *args)
        502         for handler in handlers:
        503             func = getattr(handler, meth_name)
    --> 504             result = func(*args)
        505             if result is not None:
        506                 return result


    ~/anaconda3/lib/python3.6/urllib/request.py in https_open(self, req)
       1359         def https_open(self, req):
       1360             return self.do_open(http.client.HTTPSConnection, req,
    -> 1361                 context=self._context, check_hostname=self._check_hostname)
       1362 
       1363         https_request = AbstractHTTPHandler.do_request_


    ~/anaconda3/lib/python3.6/urllib/request.py in do_open(self, http_class, req, **http_conn_args)
       1318                           encode_chunked=req.has_header('Transfer-encoding'))
       1319             except OSError as err: # timeout error
    -> 1320                 raise URLError(err)
       1321             r = h.getresponse()
       1322         except:


    URLError: <urlopen error [Errno 60] Operation timed out>


### 使用Scrapy爬取

写爬虫有个很麻烦地方是，任务常常是重复的：
- 找到页面上的所有链接
- 区分外部链接还是内部链接
- 到新的页面上去

Scrapy就是能帮助我们做这些事情的工具，目前支持2.7和3.4以上的Python版本。


### scrapy的简单用法说明

`pip install scrapy` # 安装
`scrapy startproject wikiSpider` # 新建一个项目

#### 项目结构

- scrapy.cfg
- wikiSpider # 自定义的项目名
    - `__init__.py`
    - `items.py`
    - `pipelines.py`
    - `settings.py`
    - `spiders` # 文件夹
        - `__init__.py`
    
为了创建新的爬虫，修改自带的`Items.py`内容如下，并且需要在`spiders`下新建文件，`articleSpider.py`


```python
# -*- coding: utf-8-*-
# Items.py
from scrapy import Item, Field

class Article(Item):
	# 定义项
	title = Field()
```

其中，每个`Item`对象代表一个网页上的元素，比如，content,header,image等等。
下面是`articleSpider.py`的写法。


```python
# -*- coding: utf-8-*-

from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article

class ArticleSpider(Spider):
	name = 'article'
	allowed_domains = ['en.wikipedia.org']
	start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
                  "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
	def parse(self, response):
		item = Article()
		title = response.xpath('//h1/text()')[0].extract()
		print('Title is: ' + title)
		item['title'] = title
		return item
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-8-6ac8199007bd> in <module>()
          3 from scrapy.selector import Selector
          4 from scrapy import Spider
    ----> 5 from wikiSpider.items import Article
          6 
          7 class ArticleSpider(Spider):


    ModuleNotFoundError: No module named 'wikiSpider'


上面的项目组织是有层级的，所以当前无法在这里执行（我还不会~）。
而执行的方法是：

`scrapy crawl article`, 在项目主目录下运行这个命令即可。

`scrapy crawl article -o articles.csv -t csv` 可以把爬取的内容保存到文件中。

```
scrapy crawl article -o articles.json -t json
scrapy crawl article -o articles.xml -t xml
```
这是保存到不同格式中。

Scrapy是个很大的库，能够处理的事情很多，也意味着很重，不够轻量。但是大而全的框架就意味着，你想到的很多需求都能够通过它来实现！


