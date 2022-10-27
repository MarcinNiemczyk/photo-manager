## Contents
- [REST API](#photos)
	- [Output fields](#output)
	- [Input fields](#input)
	- [Endpoints](#endpoints)
- [Business logic](#logic)
- [Import from external API](#external)
	- [Disclaimer](#disclaimer)
- [Import from JSON File](#file)


---

### Photos REST API <a name="photos"></a>

#### Output fields <a name="output"></a>
ID, title, album ID, width, length, color, image (url)

```JSON
    {
        "id": 1,
        "title": "photo1",
        "albumId": 120,
        "width": 1920,
        "height": 1080,
        "color": "#aa7553",
        "image": "/photos/184b8f2c10e30326f6ee92b3652408ac.jpg"
    }
```

#### Input fields <a name="input"></a>
title, album ID, URL


```JSON
    {
        "title": "photo1",
        "albumId": 120,
        "url": "https://i.pinimg.com/originals/18/4b/8f/184b8f2c10e30326f6ee92b3652408ac.jpg"
    }
```

#### Endpoints <a name="endpoints"></a>
##### GET
list all photos

`/api/photos`

display single post

`/api/photos/<id>`

##### POST

add photo

`/api/photos`

##### PUT

update photo

`/api/photos/<id>`

##### DELETE

delete photo

`/api/photos/<id>`

### Business logic <a name="logic"></a>
Located in `services.py` contains two functions that are used within serialization:
- Download image from URL input handled by `requests` library and saved as `.jpg` file inside `MEDIA_ROOT` folder.
- Get dominant color from an image using `colorthief`.


### Import photos from external API <a name="external"></a>
To import photos from external API via CLI use `python manage.py loadexternal <url>`

#### Disclaimer <a name="disclaimer"></a>
Some image files might not download properly due to unknown causes.

Files from `https://jsonplaceholder.typicode.com/photos` are one of those files and `requests` library cannot handle them.

BUT most of the files save properly like the one from example above.

### Import photos from JSON File <a name="file"></a>
To import photos from JSON File to database use `python manage.py loadfile <filename.json>`




