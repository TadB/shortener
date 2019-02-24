Python 3.6, Django 2.1.7

## Description
Web application written in Django. The main task is to create shorter URLs from giving one.
Shorter url is stored in the database and available from the Django admin page. 
Anonymous users can run in browser address bar: '<domain-name>/\<short url>' and will be redirected to the original URL.

## Application behavior:
1. The user is informed if added URL exists in the database and there is no need to duplicate database record.

## Data Base Model:
1. Only full_url field has to be unique. Short field is SHA-256 hash, any collisions haven't been found yet.
2. SHA-256 in hex number has 64 characters, so short field is limited to max_length 64.