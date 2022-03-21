# INTER-VLAN

## layer 2

### switch

-   assign vlan to a port

    ```console
    SWITCH(config)# interface <interface>
    SWITCH(config-if)# switchport mode access
    SWITCH(config-if)# switchport access vlan <vlan>
    ```

### router

-   configuring subinterfaces with 802.1Q encapsulation

    ```console
    ROUTER(config)# interface <interface>.<vlan>
    ROUTER(config-if)# encapsulation dot1Q <vlan>
    ```

    _remember to configure ip address for the subinterface_
    _and enable physical interface_

    ```console
    ROUTER(config)# interface <interface>
    ROUTER(config-if)# no shutdown
    ```

## layer 3

### switch

-   configure port as routed

    ```console
    SWITCH(config)# interface <interface>
    SWITCH(config-if)# no switchport
    ```

_remember to configure ip address for the subinterface_

-   configure SVI

    ```console
    SWITCH(config)# interface vlan <vlan>
    SWITCH(config-if)# ip address <ip> <mask> ;ipv4
    SWITCH(config-if)# ipv6 address <ip>/<prefix> ;ipv6
    ```

-   configure trunking

    > on router switch
    >
    > ```console
    > SWITCH(config)# interface <interface>
    > SWITCH(config-if)# switchport mode trunk
    > SWITCH(config-if)# switchport trunk native vlan <vlan>
    > SWITCH(config-if)# switchport trunk encapsulation dot1q
    > ```

    > other switches
    >
    > ```console
    > SWITCH(config)# interface <interface>
    > SWITCH(config-if)# switchport mode trunk
    > SWITCH(config-if)# switchport trunk native vlan <vlan>
    > ```

-   enable routing on router switch

    ```console
    SWITCH(config)# ip routing ;ipv4
    SWITCH(config)# ipv6 unicast-routing ;ipv6
    ```

# LACP

-   EtherChannel with LACP

    ```console
    SWITCH(config)# interface range <interface range>
    SWITCH(config-if-range)# channel-group <group n> mode active
    SWITCH(config)# interface port-channel <group n>
    SWITCH(config-if)# switchport mode trunk
    SWITCH(config-if)# switchport trunk allowed vlan <vlans>
    ```

# DHCPv4

## router as dhcp server

-   Excluded ipv4 addresses

    ```console
    ROUTER(config)# ip dhcp excluded-address <ip-address> [ip-address-range]
    ```

-   create dhcp pool for LAN

    ```console
    ROUTER(config)# ip dhcp pool <pool-name>
    ROUTER(dhcp-config)# network <LAN-address> <LAN-mask>
    ROUTER(dhcp-config)# default-router <ip-address>
    ROUTER(dhcp-config)# dns-server <ip-address>
    ```

## router dhcp relay

    ```console
    ROUTER(config)# interface <LAN-interface>
    ROUTER(config-if)# ip helper-address <dhcp-router-address>
    ```

## router as dhcp client

    ```console
    ROUTER(config)# interface <interface>
    ROUTER(config-if)# ip address dhcp
    ```
# Switch Security

    
