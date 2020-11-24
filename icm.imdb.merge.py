
import os, glob
import pandas as pd

#from IMDB
b = r"C:\Users\56989\Downloads\Cien años sin soledad_ Las mejores peliculas Latin.csv"
#from ICM
a = r"C:\Users\56989\Downloads\cien+anos+sin+soledad+greatest+latin+american+films.csv"



# creating a data frame r para evitar error de /u y enconding para otro error
dficm = pd.read_csv(a, encoding= 'unicode_escape') 
print(dficm.head()) 

dficm.rename(columns = {'imdburl' : 'URL'}, inplace = True)

dficm.drop(['year','rankdifference', 'checkedcount',	'favouritecount', 
'dislikedcount', 'usertoplistcount', 'favorite'	,'disliked',
'watchlist','owned'], axis=1, inplace=True)




dfimdb = pd.read_csv(b, encoding= 'unicode_escape') 
dfimdb.drop(['Created',	'Modified',	'Release Date'], axis=1, inplace=True)
dfimdb['URL'] = dfimdb['URL'].str.replace("https", "http")

print(dfimdb['URL'].head()) 
print(dficm['URL'].head()) 




#convert_dict = {'URL': str} 
#dficm = dficm.astype(convert_dict) 
#dfimdb = dfimdb.astype(convert_dict) 

dfmerged = pd.merge(left=dficm, right=dfimdb, left_on='URL', right_on='URL')

dfmerged.rename(columns = {'Year' : 'year',
                           'URL' : 'imdburl', 
                           'url' : 'icmurl', 
                           'Description' : 'description',
                           'Const' : 'const',
                           'Directors': 'director',
                           'officialtoplistcount': 'official',
                           'Runtime (mins)' : 'runtime', 
                           'IMDb Rating' : 'rating',
                           'Genres' : 'genres', 
                           'Title':'titleimdb', 
                           'Title Type' : 'type',
                           'Position' : 'position',
                           'Num Votes' : 'n_votes',
                           'akatitle' : 'aka'
                           }, 
                inplace = True)
dfmerged = dfmerged[['rank', 'description', 'title', 'year', 'director' ,'runtime','official',
                     'checked','genres','icmurl', 
                     'aka', 'imdburl', 'position', 
                     'const', 'titleimdb', 'type', 'rating', 
                     'n_votes']]



#encoding="utf-8-sig" hace que no salgan malos caracteres
dfmerged.to_csv(r'C:\Users\56989\Downloads\CIEN_AÑOS_SIN_SOLEDAD_imdb_icm.csv', encoding="utf-8-sig" , sep=';' , index = False)
#dfmerged.to_excel(r'C:\Users\56989\Downloads\TSPDT_NOIR_imdb_icm.xlsx', encoding="utf-8", index = False)