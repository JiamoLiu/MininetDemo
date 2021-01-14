from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
 


class myTopo(Topo):
    def build(self):
        switch = self.addswitch('s1')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        self.addLink(h1,switch)
        self.addLink(h2,switch)


if __name__ == "__main__":
    setLogLevel('info')

    topo = myTopo()
    net = Mininet(topo = topo, link = TCLink)
    net.start()

    net.pingAll()