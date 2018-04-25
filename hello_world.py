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

# put your imports to the top of your script
import time
import logicDB

# connect to the DB created via pgAdmin
connection, cursor = logicDB.openDB(
    host='127.0.0.1',
    dbname='psql_windoof',
    user='lars',
    password='12345'
)

# working with your DB happens here between the openDB and
# the closeDB call

# simple sleep loop to avoid program from closing directly
for i in range(10):
    print('Sleeping')
    time.sleep(1)

logicDB.closeDB(connection)
