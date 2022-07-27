# "To start app"

```shell
uvicorn main:app
```

# Set up Docker. Will complete later
```shell
    docker build -t testfastapi .  #build image
    docker run -d --name mycontainer -p 80:80 testfastapi  #run image
```
# Go to http://127.0.0.1:80/docs for interactive swagger docs in browser.

# Go to http://127.0.0.1:80/redoc for non-interactive swagger docs in browser
