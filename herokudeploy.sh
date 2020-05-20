if [[ $1 != '' ]]; then
  heroku create $1 --buildpack heroku/python
  if [ $? -eq 0 ]; then
    heroku buildpacks:add heroku/nodejs
    heroku git:remote -a $1
    heroku config:set DJANGO_SETTINGS_MODULE='config.production.settings'
    heroku config:set DISABLE_COLLECTSTATIC=1
    heroku addons:create heroku-postgresql:hobby-dev
    git push heroku master
    heroku run ./manage.py createsuperuser
  else
    echo "The project was not created"
  fi
else
  echo "No name specified"
fi
