from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import sys

p=int(sys.argv[1])
q=int(sys.argv[2])


def networkFun():

    network = Mininet( controller=Controller , link=TCLink)  #"develop empty networkwork"
    
    info( '---->>>>Adding controller\n' )
    network.addController( 'cont0' )

    info( '---->>>>Adding hosts\n' )

    even=1
    odd=1
    hosts=[]
    switches=[]
    ipEven='22.0.0.'
    ipOdd='22.0.1.'

    for x in range(0,p*q):
	
	if x%2==0:
            hosts.append(network.addHost('h'+str(x+1), ip=ipEven+str(even)+'/24'))
            even+=1
	else:
	    hosts.append(network.addHost('h'+str(x+1), ip=ipOdd+str(odd)+'/24'))
	    odd+=1
	print "Added h"+str(x+1)

    info( '---->>>>Adding switch\n' )

    for x in range(0,q):
        switches.append(network.addSwitch('s'+str(x+1)))
	print "Added s"+str(x+1)

    bandwidth=0
    for x in range(0,q):
	for y in range(0,p):
            network.addLink( hosts[p*x+y], switches[x] , bw=bandwidth+1)
	    bandwidth=(bandwidth+1)%2
	    print "h"+str(p*x+y+1)+"----s"+str(x)
            

    for x in range(0,q-1):
        network.addLink(switches[x],switches[x+1],bw=2)
	print "s"+str(x)+"-----s"+str(x+1) #joins the switches


    info('Starting the networkwork\n')
    network.start()

    info( 'Running CLI\n' )
    CLI(network)

    network.stop() #stops the networkwork
    info('networkwork stopped')

setLogLevel('info')
networkFun()
