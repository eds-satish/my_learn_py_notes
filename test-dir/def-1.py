def appHost():
    print('I am in appHost')
    def adminServer():
        print('I am in adminserver')
        def cluster():
            print('Cluster')
            def node():
                print('node')
                def managed_server1():
                    print('ms1')
                    def managed_server2():
                        print('ms2')
    adminServer()
        cluster()
    node()
    managed_server1()
    managed_server2()


appHost()

