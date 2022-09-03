from datetime import date
import os
import pathlib

import jaydebeapi


def main():
    print('Executing Main Function')

    dir_path=pathlib.Path(__file__).parents[1]
    print(dir_path)
    jt400libpath = str(dir_path) + "\lib\jt400.jar"
    print(jt400libpath)

    LIBRARY = "JUSTINC951"
    SCHEMA = USER = "JUSTINC95"
    SYSTEM = "PUB400.COM"
    PASSWORD = "P@ssw0rd"

    conn0 = jaydebeapi.connect("com.ibm.as400.access.AS400JDBCDriver",
                                "jdbc:as400://PUB400.COM:8471/JUSTINC95",
                                ["JUSTINC95","P@ssw0rd"],
                                jt400libpath)
    curs = conn0.cursor()
    curs.execute("SELECT * FROM JUSTINC951.TESTING001")
    curs.fetchall()
    curs.close()
    conn0.close()

if __name__ == "__main__":
    main()
