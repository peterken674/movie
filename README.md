# Newsrun
#### Newsrun, 2021.
#### By **Peter Kennedy, Elvis Midigo, Rosemary Tajeu & Floice Nyota **
## Description
A Flask powered application where the user can:
- user can sign up for your subscription service.
- user can input the different genres of movies that he/she is interested in.
- user gets daily movie recommendations straight to their email.
- user can also get Youtube trailer link to watch the movie trailer on Youtube.


## Setup/Installation
On your terminal, clone the project.
    
    $ git clone git@github.com:peterken674/movie.git

Navigate into the cloned project.

    $ cd movie

Create a `start.sh` file.

    $ touch start.sh

Inside `start.sh`, add your API key from [https://www.themoviedb.org/settings/api(https://www.themoviedb.org/settings/api) and the command for executing `manage.py`, which will start the server.

```python
export MOVIE_API_KEY='<YOUR_API_KEY>'

python manage.py server
```
Give the file execution permissions.

    $ chmod a+x start.sh

Run the program.

    $ ./start.sh
## Known Bugs
- UI is not completely responsive to very large screens.
- Does not perform check to see whether the movie request returns something in the response.
## Technologies Used
- Flask(Python)
- Jinja2
- Unittest
## Support and contact details
If you have any suggestions, questions or in case of a fire, you can reach the developer via github and click on the contributors.
### License
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright &copy; 2021