from app import db

'''
Entities:
Episodes
Movies
Series
Seasons
Content
Genres, ordered list (or main genre, secondary genre)
Users - admin/non-admin
Favorites

Relationships:
A series has at least one episode (1-n)
An episode has one piece of content (1-1)
A movie has one piece of content (1-1)
A series has at least one genre (1-n)
A series has at least one season (1-n)
A movie has at least one genre (1-n)

Tables:
tablename = episodes
id: integer, unique, nonnull
title: text, unique, nonnull
description: text, nonnull
date_released: date, nonnull
genre_id: integer, nonnull
series_id: integer, unique, nonnull
season_id: integer, unique, nonnull

tablename = season
id: integer, unique, nonnull
description: text, nonnull
date_released: date, nonnull
genre_id: integer, nonnull
series_id: integer, unique, nonnull
episodes: text, nonnull

tablename = series
id: integer, unique, nonnull
title: text, unique, nonnull
description: text, nonnull
date_released: date, nonnull
genre_id: integer, nonnull
episodes: list of text, nonnull
image_url: text, nonnull

tablename = movies
id: integer, unique, nonnull
title: text, unique, nonnull
description: text, nonnull
date_released: date, nonnull
genre_id: integer, nonnull
image_url: text, nonnull

tablename = genres
id: integer, unique, nonnull
name: text, unique, nonnull

add favorites, users (admin/non-admin)
'''