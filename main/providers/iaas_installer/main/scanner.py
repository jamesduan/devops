
import nmap

def getScanState(ip='', port=''):

	nm = nmap.PortScanner()
	nm.scan(ip, port)
	state_result = nm[ip].state()
	tcp_port_state = nm[ip].tcp(int(port))['state']
	return state_result, tcp_port_state

