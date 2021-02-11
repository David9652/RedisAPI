""" 
    Used to validate possible sections to get
    server will return server Information, cersions, configs, binary
    clients will return information about connected clients
    memory will return statistics about memory usage and limits
    stats will return information about connection, network, keyspace statistics
    replication will return information about replication settings and status
    cpu will return information about CPU utilization
    cluster will return information about cluster settings and status
 """
INFO = 'info' # Command for getting information about the redis-instance
STATUS = ('server','clients','memory','stats','replication','cpu','cluster')