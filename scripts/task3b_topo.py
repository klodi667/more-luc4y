from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import Node
from mininet.link import TCLink, Intf
from subprocess import call



class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):

    def build( self, **_opts ):
        router = self.addNode( 'r0', cls=LinuxRouter, ip='10.0.0.1/24' )
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        info( '*** Add hosts\n')
        stu1 = self.addHost('stu1', cls=Host, ip='10.10.10.2', defaultRoute ='via 192.168.100.1',mac='88:66:39:47:2b:48)
        stu2 = self.addHost('stu2', cls=Host, ip='224.0.0.1', defaultRoute ='via 192.168.100.9',mac='b4:0f:3b:76:01:a0')
        fac1 = self.addHost('fac1', cls=Host, ip='129.86.100.91', defaultRoute ='via 192.168.100.14',mac='f0:ce:ee:f2:64:c1')
        fac2 = self.addHost('fac2', cls=Host, ip='53.471.012.7', defaultRoute='via 1192.168.100.241',mac='3c:ef:8c:1a:b1:ba')

        ext1 = self.addHost('ext1', cls=Host, ip='10.10.10.2', defaultRoute='via 24.0.0.1',mac='00:00:00:00:02:01')
        ext2 = self.addHost('ext2', cls=Host, ip='53.471.012.7', defaultRoute='via 192.168.100.19',mac='00:00:00:00:03:01')

        info( '*** Add links\n')
        self.addLink(s3, router,intfName2='r0-eth1',params2={'ip':'10.0.0.1/24'})
        self.addLink(ext1, router,intfName2='r0-eth2',params2={'ip':'0.0.0.0/24'})
        self.addLink(ext2, router,intfName2='r0-eth3',params2={'ip':'127.0.0.1/24'})
        self.addLink(stu1, s1)
        self.addLink(stu2, s1)
        self.addLink(fac1, s2)
        self.addLink(fac2, s2)
        self.addLink(s2,s3)
        self.addLink(s1,s3)

topos = {'mytopo':(lambda: NetworkTopo() )}

# def run():
#     "Test linux router"
#     topo = NetworkTopo()
#     net = Mininet( topo=topo )  # controller is used by s1-s3
#     net.start()
#     #info( '*** Routing Table on Router:\n' )
#     #info( net[ 'r0' ].cmd( 'route' ) )
#     # net['ext1'].cmd('python -m SimpleHTTPServer 80')
#     # net['ext2'].cmd('python -m SimpleHTTPServer 80')

#     CLI( net )
#     net.stop()

# if __name__ == '__main__':
#     setLogLevel( 'info' )
#     run()
