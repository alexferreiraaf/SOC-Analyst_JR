import ipaddress
import re 
import requests 

def extrair_ips(arquivo): 
	ips = set() 
	regex = r"\b(?:\d{1,3}\.){3}\d{1,3}\b" 
	with open( 
		arquivo,
 		"r", 
		encoding="utf-8", 
	) as f: 
		for linha in f: 
			encontrados = re.findall( 
				regex, 
				linha, 
			) 
			
			for ip in encontrados: 
				ips.add(ip) 
		return sorted(list(ips)) 
	def validar_ip(ip): 
		try: 
			ipaddress.IPv4Address(ip) 
			return True 
		except ValueError: 
			return False 
	def consultar_virustotal(ip, api_key): 
		url = ( 
			f"https://www.virustotal.com/api/v3/ip_addresses/{ip}" 
		) 
		headers = { 
			"x-apikey": api_key 
		} 
	
		try: 
			resposta = requests.get(
				url, 
				headers=headers, 
				timeout=30, 
			) 

			if resposta.status_code != 200: 

				print( 
					f"Erro na consulta do IP {ip}: " 
					f"{resposta.status_code}" 
				) 
				
				return 0, 0 
			dados = resposta.json() 
			stats = ( 
				dados["data"]["attributes"]["last_analysis_stats"] 
			) 
			
			malicious = stats.get("malicious", 0) 
			suspicious = stats.get("suspicious", 0) 
			return malicious, suspicious 
		except Exception as erro: 
			print(erro) 
			return 0, 0 
		def classificar_risco(score): 
			if score == 0: 
				return "BAIXO" 
			if 1 <= score <= 5: 
				return "MÉDIO" 
			return "ALTO"
