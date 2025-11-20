import re
import csv
from collections import Counter
from datetime import datetime

# --- 1. MOCK (SIMULAÇÃO) DA BIBLIOTECA python-evtx ---
# Em um ambiente real, você instalaria: pip install python-evtx
# E usaria: from Evtx.Evtx import Evtx

class MockRecord:
    def __init__(self, event_id, user, ip, timestamp):
        self.event_id = event_id
        self.user = user
        self.ip = ip
        self.timestamp = timestamp

    def xml(self):
        # Simula a estrutura exata do XML gerado pelo Windows para Eventos 4625
        return f"""
        <Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'>
          <System>
            <EventID>{self.event_id}</EventID>
            <TimeCreated SystemTime='{self.timestamp}'/>
          </System>
          <EventData>
            <Data Name='SubjectUserSid'>S-1-0-0</Data>
            <Data Name='TargetUserName'>{self.user}</Data>
            <Data Name='WorkstationName'>DESKTOP-SOC</Data>
            <Data Name='IpAddress'>{self.ip}</Data>
            <Data Name='IpPort'>0</Data>
          </EventData>
        </Event>
        """

class MockEvtx:
    def __init__(self, filename):
        self.filename = filename

    def records(self):
        # Gera logs falsos misturando sucessos (4624) e falhas (4625)
        dados_ficticios = [
            (4624, "admin", "192.168.1.5", "2025-11-20 10:00:00"), # Sucesso (Ignorar)
            (4625, "admin", "192.168.1.50", "2025-11-20 10:05:00"), # Falha 1
            (4625, "admin", "192.168.1.50", "2025-11-20 10:05:05"), # Falha 2
            (4625, "root", "45.33.22.11", "2025-11-20 10:10:00"),   # Falha 3
            (4625, "guest", "45.33.22.11", "2025-11-20 10:10:05"),  # Falha 4
            (4625, "user2", "10.0.0.200", "2025-11-20 11:00:00"),   # Falha 5
        ]
        for eid, user, ip, time in dados_ficticios:
            yield MockRecord(eid, user, ip, time)

# --- 2. SOLUÇÃO NÍVEL 4 (Adaptada para XML) ---

def parse_windows_evtx(arquivo_evtx):
    tentativas = []
    
    # REGEX AJUSTADO PARA XML:
    # Ao usar .xml(), o python-evtx retorna tags XML.
    # O regex original do enunciado esperava texto formatado (como no visualizador de eventos).
    # Aqui usamos regex robusto para pegar o conteúdo dentro das tags <Data Name='...'>.
    
    # Captura <EventID>4625</EventID>
    regex_event_id = re.compile(r"<EventID>(\d+)</EventID>")
    
    # Captura <Data Name='TargetUserName'>USUARIO</Data>
    regex_user = re.compile(r"<Data Name='TargetUserName'>([^<]+)</Data>")
    
    # Captura <Data Name='IpAddress'>IP</Data>
    regex_ip = re.compile(r"<Data Name='IpAddress'>([\d.]+)</Data>")

    print(f"📂 Processando arquivo Windows: {arquivo_evtx}...")

    # Usamos o MockEvtx no lugar do Evtx real
    # Em produção: for record in Evtx(arquivo_evtx).records():
    for record in MockEvtx(arquivo_evtx).records():
        xml_content = record.xml()
        
        # 1. Verificar se é Event ID 4625 (Falha de Logon)
        match_id = regex_event_id.search(xml_content)
        if match_id and match_id.group(1) == '4625':
            
            # 2. Extrair Usuário e IP
            match_user = regex_user.search(xml_content)
            match_ip = regex_ip.search(xml_content)
            
            if match_user and match_ip:
                usuario = match_user.group(1)
                ip = match_ip.group(1)
                tentativas.append((usuario, ip))

    return tentativas

def gerar_relatorio_windows(tentativas):
    if not tentativas:
        print("⚠️ Nenhuma falha de logon encontrada.")
        return

    contador = Counter(tentativas)
    arquivo_saida = "relatorio_windows_4625.csv"
    
    with open(arquivo_saida, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Usuário (TargetUserName)", "IP Origem", "Total Falhas", "Data Coleta"])
        
        # Ordenar por maior número de tentativas
        for (user, ip), total in sorted(contador.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([user, ip, total, datetime.now().strftime("%Y-%m-%d %H:%M")])
            
    print(f"✅ Relatório Windows gerado: {arquivo_saida}")
    
    # Prévia
    print("\n📋 Prévia (Top Incidências):")
    for (user, ip), total in sorted(contador.items(), key=lambda x: x[1], reverse=True):
        print(f"   - Usuário: {user:<10} | IP: {ip:<15} | Falhas: {total}")

if __name__ == "__main__":
    # Nome do arquivo é simbólico aqui, pois estamos usando o Mock
    logs = parse_windows_evtx("Security.evtx")
    gerar_relatorio_windows(logs)
