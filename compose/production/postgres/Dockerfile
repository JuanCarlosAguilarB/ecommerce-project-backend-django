FROM postgres:15-alpine

COPY ./compose/production/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance

# the scripts in init_database.sql will be executed automated in alphabetical order
COPY ./compose/production/postgres/init_database.sql /docker-entrypoint-initdb.d/init_database.sql
RUN chmod +x /docker-entrypoint-initdb.d/init_database.sql