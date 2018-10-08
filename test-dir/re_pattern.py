import re

#pattern = """/apps/java/jdk1.8.0_65/jre//bin/java -Dnop -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -Xms3072m -Xmx3072m -Xmn1536m -Xss256k -XX:ParallelGCThreads=2 -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:SurvivorRatio=8 -XX:TargetSurvivorRatio=90 -XX:MaxTenuringThreshold=15 -XX:+AggressiveOpts -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/apps/tomcat/instances/tomcat01/logs/heapdump.hprof -Djvm.name=h118177vaps2041-tomcat01 -Djava.security.egd=file:/dev/./urandom -agentpath:/apps/compuware/dynatrace/dynatrace-4.2.0/agent/lib/libdtagent.so=name=TC01_GAM_Prod_SCS,environmentdetection=no,server=h118177apss3091.att.target.com:8998 -Dclb.library.path=/apps/ekmc/lib/ -Xloggc:/apps/tomcat/instances/tomcat01/logs/gamApp-gc.log -verbose:gc -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=20 -XX:GCLogFileSize=10M -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Djava.library.path=/apps/ekmc/lib:/export/u01/app/oracle/product/11.2.0/client/lib -Djava.net.preferIPv4Stack=true -Dclb.library.path=/apps/ekmc/lib -agentpath:/apps/compuware/dynatrace/dynatrace-4.2.0/agent/lib/libdtagent.so=name=TC01_Checkout_Prod_SCS,environmentdetection=no,server=h118177apss3272.att.target.com:9998 -XX:+TieredCompilation -XX:ReservedCodeCacheSize=256M -XX:+AggressiveOpts -XX:+PrintCommandLineFlags -XX:+PrintStringTableStatistics -Xms2048m -Xmx2048m -Xmn1280m -Xss256k -XX:SurvivorRatio=10 -XX:TargetSurvivorRatio=90 -XX:MaxTenuringThreshold=7 -XX:ParallelGCThreads=3 -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -XX:+CMSParallelRemarkEnabled -XX:+UseCMSInitiatingOccupancyOnly -XX:CMSInitiatingOccupancyFraction=70 -XX:+ScavengeBeforeFullGC -XX:+CMSScavengeBeforeRemark -Xloggc:/apps/tomcat/instances/tomcat01/logs/gc-2017-10-04-08-45.log -verbose:gc -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=20 -XX:GCLogFileSize=10M -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintTenuringDistribution -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/apps/tomcat/instances/tomcat01/logs/heapdump-2017-10-04-08-45.hprof -Djava.security.egd=file:/dev/./urandom -Dbootstrap.property.file=/apps/tomcat/instances/tomcat01/conf/bootstrap.properties -Dcassandra.with.ssl=true -Dservo.enabled=true -DLog4jContextSelector=org.apache.logging.log4j.core.async.AsyncLoggerContextSelector -Dekmc.property.file=/apps/ekmc/conf/ekmcConfigTemplate.properties -Djava.endorsed.dirs=/apps/tomcat/default/endorsed -classpath :/apps/ekmc/lib/LB.jar:/apps/ekmc/lib/LBImpl.jar:/apps/tomcat/default/bin/bootstrap.jar:/apps/tomcat/default/bin/tomcat-juli.jar:/apps/ekmc/lib/LB.jar:/apps/ekmc/lib/LBImpl.jar -Dcatalina.base=/apps/tomcat/instances/tomcat01 -Dcatalina.home=/apps/tomcat/default -Djava.io.tmpdir=/apps/tomcat/instances/tomcat01/temp org.apache.catalina.startup.Bootstrap startup"""

"""
reobj = re.compile(r"-\w+.*?=\w+.*?\s")
res = reobj.findall(pattern)
print('result is: ', res)
print()
jo = ' '.join(res)
print('join is:', jo)
print()
spl = jo.split()
print('spl list is: ',spl)
print()
for num, word in enumerate(spl):
    print(f'{num+1:>3}', f'{word:|<100}')
"""

def jvmfun(p):
    reobj = re.compile(r"-\w+.*?=\w+.*?\s")
    res = reobj.findall(p)
    if isinstance(p, list):
        jo = ' '.join(res)
        spl_l = jo.split()
        for num, word in enumerate(spl_l):
            print(f'{num:>3}', f'{word:<}')
        print('\n{:|^30}'.format('from lissstt'))
    elif isinstance(p, str):
        spl_s = p.split()
        for num, word in enumerate(spl_s):
            print(f'{num:>3}', f'{word:<}')
        print('\n{:|^30}\n'.format('frommmm strrrr'))
    else:
        print('Some error has occured')

#jvmfun(pattern)

    
    
