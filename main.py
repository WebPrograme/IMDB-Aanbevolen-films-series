from imdb import IMDb

ia = IMDb()
status = True
movies = []
genres = []
keywords = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Get The Movies And Genres
while status == True:
  movie_input = input('Geef een film of serie in: ')
  if movie_input != 'DONE':
    movies.append(ia.search_movie(movie_input)[0])
    movie_id = ia.get_imdbID(movies[-1])
    print(movies[-1])
    movie = ia.get_movie(movie_id)
    try:
      keywordList = ia.get_movie(movie_id, info='keywords')
      keyword = keywordList['keywords']
      genresList = movie['genres'] 
      genres.extend(genresList)
      keywords.append(keyword[0])
    except Exception: 
      print('No keywords')
    print('--------------------------------------')
  else:
    if len(genres) < 3:
      print(f"{bcolors.HEADER}Niet genoeg data, geef nog een film of serie in{bcolors.ENDC}")
      print('--------------------------------------')
    else:
      status = False
    
#Set All Genres In Variabels And A List
genresCountList = []
genreFirst = 0
genreSecond = 0
genreThird = 0

genresCountList.append(genres.count('Action'))
genresCountList.append(genres.count('Comdedy'))
genresCountList.append(genres.count('Family'))
genresCountList.append(genres.count('History'))
genresCountList.append(genres.count('Mystery'))
genresCountList.append(genres.count('Sci-Fi'))
genresCountList.append(genres.count('War'))
genresCountList.append(genres.count('Adventure'))
genresCountList.append(genres.count('Fantasy'))
genresCountList.append(genres.count('Horror'))
genresCountList.append(genres.count('News'))
genresCountList.append(genres.count('Biography'))
genresCountList.append(genres.count('Game-Show'))
genresCountList.append(genres.count('Musical'))
genresCountList.append(genres.count('Romance'))
genresCountList.append(genres.count('Thriller'))
genresCountList.append(genres.count('Western'))
genresCountList.append(genres.count('Crime'))
genresCountList.append(genres.count('Animation'))
genresCountList.append(genres.count('Documentary'))
genresCountList.append(genres.count('Film-Noir'))
genresCountList.append(genres.count('Music'))
genresCountList.append(genres.count('Reality-TV'))
genresCountList.append(genres.count('Talk-Show'))
genresCountList.append(genres.count('Drama'))
genresCountList.append(genres.count('Sport'))
genresCountList = [int(x) for x in genresCountList]
x = 0
genreName = ''

#Function to get genre
def getGenreAgain(x):
  if x == 13:
    result = 'Musical'
    return result
  elif x == 14:
    result = 'Romance'
    return result
  elif x == 15:
    result = 'Thriller'
    return result
  elif x == 16:
    result = 'Western'
    return result
  elif x == 17:
    result = 'Crime'
    return result
  elif x == 18:
    result = 'Animation'
    return result
  elif x == 19:
    result = 'Documentary'
    return result
  elif x == 20:
    result = 'Film-Noir'
    return result
  elif x == 21:
    result = 'Music'
    return result
  elif x == 22:
    result = 'Reality-TV'
    return result
  elif x == 23:
    result = 'Talk-Show'
    return result
  elif x == 24:
    result = 'Drama'
    return result
  elif x == 25:
    result = 'Sport'
    return result

def getGenre(x):
  if x == 0:
    result = 'Action'
    return result
  elif x == 1:
    result = 'Comdedy'
    return result
  elif x == 2:
    result = 'Family'
    return result
  elif x == 3:
    result = 'History'
    return result
  elif x == 4:
    result = 'Mystery'
    return result
  elif x == 5:
    result = 'Sci-Fi'
    return result
  elif x == 6:
    result = 'War'
    return result
  elif x == 7:
    result = 'Adventure'
    return result
  elif x == 8:
    result = 'Fantasy'
    return result
  elif x == 9:
    result = 'Horror'
    return result
  elif x == 10:
    result = 'News'
    return result
  elif x == 11:
    result = 'Biography'
    return result
  elif x == 12:
    result = 'Game-Show'
    return result
  else:
    getGenre2 = getGenreAgain(x)
    return getGenre2

#Check for top genres
while x != 26:
  if genreFirst < genresCountList[x]:
    genreFirst = genresCountList[x]
    genreNameFirst = getGenre(x)
  elif genreSecond < genresCountList[x]:
    genreSecond = genresCountList[x]
    genreNameSecond = getGenre(x)
  elif genreThird < genresCountList[x]:
    genreThird = genresCountList[x]
    genreNameThird = getGenre(x)
  x += 1

#Print genres
print('')
print('GENRES')
print('')

print(f'1. {genreNameFirst}')
print(f'2. {genreNameSecond}')
print(f'3. {genreNameThird}')
print('')

#Set variables
y = 0 
z = 0
w = 0 
i = 0
p = 0
q = 0
titles_title = []
results_titles = []
results_ratings = []

#Get 100 movies
titles = ia.search_movie_advanced(adult=True, results=50)
print('RATING   NAME')

#Filter movies by genres
def searchByGenres(y, p, q):
  while y != range(len(titles)):
    try:
      result_title = titles[y]
      result_genre = result_title['genres']
      result_rating = result_title.get('rating')
    except Exception: 
      print('--------------')
      break
    if result_rating == None:
      result_rating = 0
    if genreNameFirst and genreNameSecond and genreNameThird in result_genre:
      print(result_title)
      if len(results_ratings) == 0:
        results_ratings.append(result_rating)
        results_titles.append(result_title)
        break
      while p != len(results_ratings):
        if float(result_rating) > results_ratings[p]:
          if result_rating == 0:
            result_rating = '|||' 
            results_ratings.insert(-1, result_rating)
            results_titles.insert(-1, result_title)
          else:
            results_ratings.insert(p, result_rating)
            results_titles.insert(p, result_title)
        else:
          results_ratings.insert(-1, result_rating)
          results_titles.insert(-1, result_title)
        p += 1
    else:
      titles.remove(result_title)
    y += 1
  while q != len(results_titles):
    print(f'{results_ratings[q]}      {results_titles[q]}')
    q += 1
    
searchByGenres(y, p, q)

if range(len(titles)) == 0:
  titles = ia.search_movie_advanced(adult=True, results=100)
  searchByGenres(y)

#while z != len(keywords):
#  titles_keyword = ia.search_movie_advanced(keywords[z], results=1000)
#  while w != len(titles_keyword):
#    titles_title = (titles_keyword[w]['title'])
#    w += 1
#  titles.append(titles_title)
#  z += 1

print(' ')
print('DONE')