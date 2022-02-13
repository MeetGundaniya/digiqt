import pandas as pd
from multiapps.moviesapi.serializers import MovieDBSerializer

df = pd.read_excel('movies.xlsx')

for row in range(len(df)):
  serializer = MovieDBSerializer(data={
    'name': df.loc[row,'movie_name'],
    'rating': float(df.loc[row,'movie_rating']),
    'release': df.loc[row,'movie_release'],
    'duration': f"00:{str(df.loc[row,'movie_duration'])}:00",
    'description': df.loc[row,'movie_desc']
  })

  if serializer.is_valid():
    serializer.save()
  else:
    print(serializer.errors)
