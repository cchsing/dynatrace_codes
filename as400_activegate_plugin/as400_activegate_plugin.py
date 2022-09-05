from ruxit.api.base_plugin import RemoteBasePlugin
import logging

from datetime import date
import pathlib
import jaydebeapi

logger = logging.getLogger(__name__)

class AS400PluginRemote(RemoteBasePlugin):

    def initialize(self, **kwargs):
        logger.info("Config: %s", self.config)
        self.url=self.config['url']
        

    def query(self, **kwargs):
        
        queries = [
            {"metric": "as400_hourly_transactions", "sql":"SELECT COUNT(*) FROM %s.%s"%(db_library,db_aliasName)}
        ]

        gname = "IBM"
        dname = "AS400"
        group = self.topology_builder.create_group(gname,gname)
        device = group.create_device(dname,dname)

        # date counter 
        d0 = date(2014, 1, 2)
        d1 = date.today()
        deltaD = (d1 - d0)
        date_counter = "M" + "{:09.0f}".format(deltaD.days)

        # Jar file path
        dir_path = pathlib.Path(__file__).parents[1]
        jt400libpath = str(dir_path) + "\lib\jt400.jar"
        print(jt400libpath)

        # variables 
        cls_name = "com.ibm.as400.access.AS400JDBCDriver"
        db_library = self.config['db_library'] # "JUSTINC951"
        db_table = "TESTING001"
        db_schema = db_user = "JUSTINC95"
        db_system = self.config['db_system'] #"PUB400.COM"
        db_password = "P@ssw0rd"
        jdbc_conn_url = "jdbc:as400://" + db_system + "/" + db_schema
        db_aliasName = "ALIAS3"

        with jaydebeapi.connect(cls_name,
                                jdbc_conn_url,
                                [db_user, db_password],
                                jt400libpath) as conn:
            with conn.cursor() as curs:
                curs.execute("DROP ALIAS ")
                curs.execute("CREATE ALIAS")
                for query in self.queries:
                    curs.execute()

        
