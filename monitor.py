from flask_restful import Resource, Api
from snmp_handler import SNMPHandler



class Monitor(Resource):
    #endpoint rest
        def get(self):
            snmpHandler = SNMPHandler()
            oids, values = snmpHandler.getProcessList()
            return {"oids": oids, "values":values}


