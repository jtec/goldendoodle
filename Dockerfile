FROM alpine:3.22
ARG DEBIAN_FRONTEND=noninteractive
RUN apk update && apk upgrade
RUN apk add caddy
WORKDIR /app
ENTRYPOINT ["caddy", "reverse-proxy"]