import serial,time

READ_TIMEOUT = 0
class show:
	sw_stack=open("show\\sw_stack.txt",'r+').readlines()
	sw_nostack=open("show\\sw_nostack.txt","r+").readlines()
	bgp=open("show\\bgp.txt","r+").readlines()
	eigrp=open("show\\eigrp.txt","r+").readlines()
	multicast=open("show\\multicast.txt","r+").readlines()
	nexus=open("show\\nexus.txt","r+").readlines()
	ospf=open("show\\ospf.txt","r+").readlines()
	otros=open("show\\otros.txt","r+").readlines()
	R_basic=open("show\\R_basic.txt","r+").readlines()
	vss=open("show\\vss.txt","r+").readlines()

def ser_conn():
	try:
		consola = serial.Serial(
		port="COM3",
		baudrate=9600,
		parity="N",
		stopbits=1,
		bytesize=8,
		timeout=READ_TIMEOUT
		)
	except:
		print("\nWRONG SERIAL PORT !!!!\n")
		time.sleep(1)
		ser_conn()
	time.sleep(1)
	return consola

def serial_Write(ser,config):
	try:
		for i in range(len(config)):
			ser.write(config[i]+'\n')
			output=ser.readline(10)
			print(output)
		time.sleep(1)
		result=ser.readlines(ser.inWaiting())
		return result
	except:
		pass

def main():
	archivos=['sw_stack','sw_nostack','bgp','eigrp','multicast','ospf','otros','R_basic','vss']
	search=[0,1]
	ser=ser_conn()
	for i in range(len(search)):
		print(eval("show."+archivos[search[i]]))
		result=serial_Write(ser,"show."+archivos[i])
		time.sleep(1)
		file=open("result_"+archivos[i]+".txt","w+")
		file.write(result)
		file.close()
	ser.close()
	
   

if __name__ == "__main__":
    main()
