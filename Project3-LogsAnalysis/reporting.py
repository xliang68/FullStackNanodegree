#!/usr/bin/env python2
# A reporting tool for log analysis

import psycopg2

DBNAME = "news"


def main():
    print "The most popular three articles are:"
    process_list(get_articles())
    print ""
    print "The most popular article authors are:"
    process_list(get_authors())
    print ""
    print "The following days have more than 1% of requests leading to errors:"
    process_days()


def get_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title, count(*) as viewnumber from articles "
              "inner join log on substring(log.path, 10)=articles.slug "
              "group by title order by viewnumber desc limit 3;")
    return c.fetchall()
    db.close()


def get_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, count(*) as authorview from authors "
              "inner join (select author from articles "
              "inner join log "
              "on substring(log.path, 10)=articles.slug) as temp "
              "on authors.id=temp.author "
              "group by name order by authorview desc;")
    return c.fetchall()
    db.close()


def process_list(lst):
    i = 0
    for item in lst:
        i = i + 1
        print str(i)+". "+item[0]+" -- "+str(item[1])+" views"


def get_days():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select a.date, "
              "round(100.0*a.dailyerrorcount/b.dailycount,2) as errorrate "
              "from (select date(time) as date, count(*) as dailyerrorcount "
              "from log where status = '404 NOT FOUND' group by date) as a "
              "inner join (select date(time) as date, count(*) as dailycount "
              "from log group by date) as b "
              "on a.date=b.date where a.dailyerrorcount > 0.01*b.dailycount;")
    return c.fetchall()
    db.close()


def process_days():
    days = get_days()
    i = 0
    for day in days:
        i = i + 1
        print str(i)+". "+str(day[0])+" -- "+"{}%".format(day[1])+" errors"


if __name__ == '__main__':
    main()
