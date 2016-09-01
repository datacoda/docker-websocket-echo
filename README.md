dataferret/websocket-echo
=========================

This is a very basic websocket echo server based off the tutorial
http://autobahn.ws/python/tutorials/echo/

Usage
-----

The container is setup with an entrypoint that takes the port as the first argument.  Bind to the corresponding external
point either directly with Docker.

```bash
docker run -p 8080:8080 dataferret/websocket-echo 8080
```

You can also just expose it and use a reverse proxy to do the external access.

```bash
docker run -expose 80 dataferret/websocket-echo 80
```


License
-------

MIT
