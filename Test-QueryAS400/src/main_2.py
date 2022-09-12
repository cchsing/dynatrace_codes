from datetime import date
import pathlib

import jaydebeapi


def main():
    print('Executing Main Function')

    d0 = date(2014, 1, 2)
    d1 = date.today()
    deltaD = (d1 - d0)
    print(deltaD.days)
    daily_counter = "M" + "{:09.0f}".format(deltaD.days)
    print(daily_counter)

    # dir_path = pathlib.Path(__file__).parents[1]
    dir_path = r"C:\Program Files\Java\jdk-18.0.2.1"
    # print(dir_path)
    jt400libpath = str(dir_path) + "\lib\jt400.jar"
    # print(jt400libpath)

    cls_name = "com.ibm.as400.access.AS400JDBCDriver"
    db_library = "JUSTINC951"
    db_table = "TESTING001"
    schema = user = "JUSTINC95"
    system = "PUB400.COM"
    password = "P@ssw0rd"
    jdbc_conn_url = "jdbc:as400://" + system + "/" + schema
    db_aliasName = "ALIAS3"

    with jaydebeapi.connect(cls_name,
                            jdbc_conn_url,
                            [user, password],
                            jt400libpath) as conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO %s.%s VALUES ('43','Test','Counter')" % (
                db_library, db_table))
            curs.execute("DROP ALIAS %s.%s" % (db_library, db_aliasName))
            curs.execute("CREATE ALIAS %s.%s FOR %s.%s" %
                         (db_library, db_aliasName, db_library, db_table))
            #curs.execute("SELECT COUNT(FNAME), LNAME FROM JUSTINC951.TESTING001 GROUP BY LNAME")
            curs.execute("SELECT COUNT(*) AS COUNT FROM JUSTINC951.ALIAS3")
            # print(curs.fetchone())
            output = curs.fetchone()
            print(output[0])

    print('Done')


if __name__ == "__main__":
    main()
