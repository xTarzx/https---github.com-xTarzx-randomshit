# ZPF


- create zone

```console
ROUTER(config)# zone security <zone-name>
```

- identify traffic

```console
ROUTER(config)# class-map {type inspect} [match-any | match-all] <class-map-name>
```

```console
ROUTER(config-cmap)# match access-group (acl-# | <acl-name>)
ROUTER(config-cmap)# match protocol <protocol-name>
ROUTER(config-cmap)# match class-map <class-map-name>
```

- define action

```console
ROUTER(config)# policy-map type inspect <policy-map-name>
ROUTER(config-pmap)# class type inspect <class-map-name>
ROUTER(config-pmap-c)# (inspect | drop | pass)
```

- identify zone pair and associate policy

```console
ROUTER(config)# zone-pair security <zone-pair-name> source (<source-zone-name> | self) destination (<destination-zone-name> | self)

ROUTER(config-sec-zone-pair)# service-policy type inspect <policy-map-name>
```

- assign zone to interface


```console
ROUTER(config-if)# zone-member security <zone-name>
```