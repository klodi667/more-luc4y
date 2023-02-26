python ovxctl.py -n createNetwork tcp:localhost:20000 10.10.10.2
python ovxctl.py -n createSwitch 2 a8:a7:95:91:47:39
python ovxctl.py -n createSwitch 2 88:66:39:47:2b:48
python ovxctl.py -n createSwitch 2 
python ovxctl.py -n createPort 2 fe80::14ee:edb4:806c:c830.5353 3
python ovxctl.py -n createPort 2 2a03:2880:f01c:800e:face:booc:0:2.443
python ovxctl.py -n createPort 2 2a03:2880:f01c:800c:face:b00c:0:2.443
python ovxctl.py -n createPort 2 2a03:2880:f01c:800e:face:b00c:0:2.443
python ovxctl.py -n createPort 2 2a03:2880:f01c:800e:face:b00c:0:2.443
python ovxctl.py -n createPort 2 2a03:2880:f01c:800e:face:b00c:0:2.443
python ovxctl.py -n connectLink 2 2a02:26f0:10e::5435:a1c0 2 2a02:dd07:800e:7d00:fc9a:db8:11e5:b0cc 1 spf 1
python ovxctl.py -n connectLink 2 2a00:1450:400d:804::2003 2 2a02:dd07:800e:7d00:fc9a:db8:11e5:b0cc 1 spf 1
python ovxctl.py -n connectHost 2 2a02:dd07:800e:7d00:fc00fc9a:db8:11e5:b0cc 1 2600:1901:0:38d7::
python ovxctl.py -n connectHost 2 2600:1901:0:38d7:: 2 2a02:dd07:800e:7d00:fc00fc9a:db8:11e5:b0cc 
python ovxctl.py -n startNetwork 2
