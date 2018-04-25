# Copyright (c) 2018 Lars Bergmann
#
# GNU GENERAL PUBLIC LICENSE
#    Version 3, 29 June 2007
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import psycopg2


def openDB(host, dbname, user, password):
    connstring = "dbname={dbname} user={user} password={password} host={host}".format(
        dbname=dbname,
        user=user,
        password=password,
        host=host
    )
    print(connstring)
    connection = psycopg2.connect(connstring)
    cursor = connection.cursor()
    return connection, cursor


def closeDB(connection, error=False):
    '''
    Do a final commit/rollback (to avoid leaving behind open transactions) and
    close DB connection
    '''
    if error:
        connection.rollback()
    else:  # default
        connection.commit()

    connection.close()


def addTable(cursor, tablename):

    cursor.execute("begin")
    create_stm = 'CREATE TABLE {tablename} ({tablename}_id serial primary key, ' +\
'{tablename}_modtime timestamp with time zone, {tablename}_author varchar(80))'

    create_stm = create_stm.format(tablename=tablename)
    cursor.execute(create_stm)

    cursor.execute("commit")


def dropTable(cursor, tablename):

    cursor.execute("begin")
    cursor.execute("DROP TABLE IF EXISTS {tablename}".format(tablename=tablename))
    cursor.execute("commit")


def addColumn(cursor, tablename, columnname, columntype):

    add_stm = 'ALTER TABLE {tablename} ADD COLUMN {tablename}_{columnname} {columntype}'.format(
        tablename=tablename,
        columnname=columnname,
        columntype=columntype
    )
    cursor.execute("begin")
    cursor.execute(add_stm)
    cursor.execute("commit")


def dropColumn(cursor, tablename, columnname):
    drop_stm = 'ALTER TABLE {tablename} DROP COLUMN {tablename}_{columnname}'.format(
        tablename=tablename,
        columnname=columnname
    )
    cur.execute("begin")
    cur.execute(drop_stm)
    cur.execute("commit")


def addForeignKey(cursor, tablename, reftablename):

    alter_stm = 'ALTER TABLE {tablename} ADD FOREIGN KEY' +\
    '({tablename}_{reftablename}_id) REFERENCES {reftablename}({reftablename}_id)'.format(
        tablename=tablename,
        reftablename=reftablename
    )

    cursor.execute("begin")
    cursor.execute(alter_stm)
    cursor.execute("commit")


def dropForeignKey(cursor, tablename, reftablename):

    alter_stm = 'ALTER TABLE {tablename} DROP FOREIGN KEY CONSTRAINT {reftablename}_id'.format(
        tablename=tablename,
        reftablename=reftablename
    )

    cur.execute("begin")
    cur.execute(alter_stm)
    cur.execute("commit")


def rollback():
    cur.execute("rollback;")
