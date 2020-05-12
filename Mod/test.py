import netaddr

mac = '04-33-85-1F-65-7D'
value = netaddr.EUI(mac).oui.registration().org
print(value)
