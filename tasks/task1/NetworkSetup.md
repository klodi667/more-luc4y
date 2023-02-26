# Network Setup:

## Task 1:
### Installing OVS on Raspberry pi:

Make sure Raspberry pi is connected to the internet.
```sh
$ sudo apt-get install openvswitch-switch
```
- Check whether OVS is properly installed in Raspberry Pi. To check run the command below  
```sh
$ ovs-vsctl add-br ovs-br1
```

#### OVS installation done:

### Assigning IP to Raspberry pi:

1. Using DHCP server: 
If raspberry pi is able to get IP address from some DHCP server and a IP will be assigned to raspberry pi.
--------------

2. Assigning Static IP address:

```sh
$ sudo vim /etc/dhcpcd.conf
```
- Insert the details below in /etc/dhcpcd.conf file. Change the parameters according to your network.
```
interface eth0
static ip_address=192.168.1.4/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```
 
### Connecting OVS with controller:

```sh
$ ovs-vsctl set-controller <BRIDGE> tcp:$CONTROLLER_ADDRESS:$CONTROLLER_PORT
```
For assinging multiple controllers to OVS:

```sh
$ ovs-vsctl set-controller <BRIDGE> tcp:$CONTROLLER_ADDRESS1:$CONTROLLER_PORT1 \
tcp:$CONTROLLER_ADDRESS2:$CONTROLLER_PORT2 \
tcp:$CONTROLLER_ADDRESS3:$CONTROLLER_PORT3 ...
```

### Creating bridge and creating ports/Interfaces and assigning IP addresses to them

- Creating a bridge
```sh
$ sudo ovs-vsctl add-br <BRIDGE_NAME>
``` 
When a bridge is created using OVS, by default a port of same name is created i.e when a bridge named br0 is created 
so port named br0 is created and it has interface br0.

- Connecting bridge to eth0 

```sh
$ sudo ovs-vsctl add-port <BRIDGE_NAME> eth0
```

- Adding a new port, Internal Interface to an existing bridge

```sh
$ sudo ovs-vsctl add-port <BRIDGE_NAME> <PORT_NAME> -- set Interface <PORT_NAME> type=internal
$ sudo ip link set <PORT_NAME> up 
            or 
$ sudo ifconfig <PORT_NAME> up 
```

- Adding an IP address to an Interface

```sh
$ sudo ip addr add 192.168.0.123/24 dev <PORT_NAME>
            or
$ sudo ifconfig <PORT_NAME> 192.168.0.123 netmask 255.255.255.0
```

- Adding default gateway to an Interface

```sh
$ sudo ip route add default via <GW> dev <Interface>
```

- Removing an IP address assigned to an Interface

```sh
$ sudo ifconfig <PORT_NAME> 0
```

- Listing all Interfaces

```sh
$ sudo ovs-vsctl list Interface
```

## Installing OpenVirteX for Network Slicing:

Use this [link](https://ovx.onlab.us/getting-started/installation/) for installing and starting OpenVirteX.




