__author__ = 'SEALiu'
import sqlite3
def createLib():
    'create table: library'
    conn = sqlite3.connect('pymemo.db')
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE library (
                libId text,
                name text,
                libDesc text,
                createTime text,
                maxReviewsPerDay integer,
                newCardsPerDay integer,
                easyInterval integer,
                maxInterval integer,
                maxAnswerTime integer,
                isShowAnswerTime boolean
        )''')