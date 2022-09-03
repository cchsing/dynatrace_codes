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

    dir_path = pathlib.Path(__file__).parents[1]
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
    aliasName = "ALIAS3"

    with jaydebeapi.connect(cls_name,
                            jdbc_conn_url,
                            [user, password],
                            jt400libpath) as conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO %s.%s VALUES ('3','Joke','JULIA')"%(db_library,db_table))
            curs.execute("DROP ALIAS %s.%s"%(db_library, aliasName))
            curs.execute(
                "CREATE ALIAS JUSTINC951.ALIAS3 FOR JUSTINC951.TESTING001")
            #curs.execute("SELECT COUNT(FNAME), LNAME FROM JUSTINC951.TESTING001 GROUP BY LNAME")
            curs.execute("SELECT * FROM JUSTINC951.ALIAS3")
            print(curs.fetchall())

    print('Done')


if __name__ == "__main__":
    main()
