sudo su - postgres
. ~/.bashrc
pg_ctl stop -D /var/lib/postgresql/15/main

pg_ctl start
psql