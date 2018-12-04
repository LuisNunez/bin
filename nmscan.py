
import nmap
import pandas


def scanHost(hostIp,hostPort):
    #hostIp = '192.168.1.1'
    #hostPort = '1720'
    outfile_path = 'out2/'+hostIp+'.xml'
    
    nm = nmap.PortScanner()
    #nm.scan(hostIp, hostPort)
    # Arguments to scan both UDP and TCP
    nm.scan(hostIp, hostPort, arguments=' -sU -sS')
    print(nm.csv())
    outXml = open(outfile_path,'w')
    outXml.write(nm.get_nmap_last_output())
    
    a = nm.scanstats()

    if a['downhosts'] == '1':
        print hostIp + hostPort + "hostdown"
        return hostIp+", " + hostPort+  ", Hostdown"+"\n"
    else:
        return nm.csv()
    #print(hostIp,hostPort)

def readXsl():
     #df = pandas.read_excel('Open_Ports.xlsx')
     #df = pandas.ExcelFile('Open_Ports.xlsx')
     df = pandas.ExcelFile('Openports.xlsx')
     # {sheet_name:df.parse(sheet_name) for sheet_name in df.sheet_names}:
     print df.sheet_names
     print "start"
     #for sheet_name in df.sheet_names:
     #   print sheet_name
     #   readTabs = df.parse(sheet_name)
        #print readTabs.columns
        #print readTabs
     #   readTabs('US Ports').columns['External IP']
        #print readTabs['External IP'].values
     sheets = df.sheet_names

     for sheet in sheets:
         print sheet
         readTabs = df.parse(sheet)
         print readTabs['External IP'].values
         IPList = readTabs['External IP'].values
         for ip in IPList:
             print ip

def readRow():
    f = open('output2.txt', 'w')
    df = pandas.read_excel('openports.xlsx', sheet_name='sheet1')
    for i in df.index:
        #print(df['External IP'][i])
        #print(df['Port'][i])

        #targetIP = df['External IP'][i]
        #targetPort = df['Port'][i]
        targetIP = df['IP'][i]
        targetPort = df['Port'][i]
        #print "--------------------"
        #print targetIP, targetPort
        targetIP = str(targetIP)
        targetPort = str(targetPort)
        #print(type(targetIP))
        #print(type(targetPort))
        outPut = scanHost(targetIP,targetPort)
        f.write(outPut)
    f.close()
if __name__ == '__main__':
#    main()
    #scanHost('192.168.1.1','22')
    #readXsl()
    readRow()
    