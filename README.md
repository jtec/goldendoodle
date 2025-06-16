# Goldendoodle
Goldendoodle, the, guard dog of Mount Olympus in greek mythology.

Playground for the simplest way to run an HTTPS server.

# Setup
Make sure your DNS records point to your public IP and that ports 80 and 443 are open to the public and directed towards the server.

# Build
```
docker build -t goldendoodle .       
```

# Run
```
docker run goldendoodle --from goldendoodle.art --to :5000   
uv run gunicorn --bind 127.0.0.1:5000 main:app
```