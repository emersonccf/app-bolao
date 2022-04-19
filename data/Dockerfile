FROM mysql:5.7-debian
# Installing OS Dependencies / update OS Linux container
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y net-tools inetutils-ping \
    && rm -rf /var/lib/apt/lists/*