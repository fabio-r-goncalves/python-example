from pysnmp.hlapi import *

PORT = 161
HOST = 'localhost'
COMM_STRING = 'public'
SNMP_VERSION = 1
PROCESS_TABLE_OID  = '.1.3.6.1.2.1.25.4.2'
INDEXES_OID = '1.3.6.1.2.1.25.4.2.1.1'

class SNMPHandler():

    
    #Efetua um get next e retorna o valor que foi obtido
    #recebe como argumento um oid valido
    def getNext(self, oid):
        errorIndication, errorStatus, errorIndex, varBinds = next(
            nextCmd(SnmpEngine(),
                CommunityData(COMM_STRING, mpModel=SNMP_VERSION),
                UdpTransportTarget((HOST, PORT)),
                ContextData(),
                ObjectType(ObjectIdentity(oid)))
        )
        if errorIndication:
            print(errorIndication)
            return Null
        return varBinds    
    
    def getProcessList(self):
        i = 10
        snmpHandler = SNMPHandler()
        #flag apenas para terminar o ciclo
        ended = False
        #Armazena o oid da tabela dos processos
        oid = PROCESS_TABLE_OID 
        #Lista para armazenar os oids obtidos
        oids = []
        #lista para armazenar os valores obtidos
        values = []
        while not ended:
            #Variavel para armazenar o valor obtido do comando getNext
            varBinds = self.getNext(oid)
            #Armazena o valor do OID obtido para posterior verificacao
            oid = varBinds[0][0]
            print(oid)
            val = varBinds[0][1]
            #Condicao para vericar se o oid devolvido ainda se encontra na gama de
            #OIDS que queremos ir buscar
            if INDEXES_OID not in str(oid):
                break
            #Armazena os valores obtidos
            oids.append(str(oid))
            values.append(str(val))
            i = i -1
            if(i < 0):
                break
        return oids, values
