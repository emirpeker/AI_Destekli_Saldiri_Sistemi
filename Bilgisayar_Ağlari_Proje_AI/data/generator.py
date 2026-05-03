import pandas as pd
import random

def generate_universal_data(n_samples=15000):
    data = []
    
    for _ in range(n_samples):
        case = random.random()
        
        # --- DURUM 1: DDoS / FLOOD SALDIRISI (Label: 1) ---
        if case < 0.20:
            protocol = random.choice([1, 3]) # TCP veya ICMP
            interval = random.uniform(0.0001, 0.01) # Çok seri
            pkt_size = random.randint(32, 64)       # Küçük/Zayıf paketler
            dst_port = 0 if protocol == 3 else random.choice([80, 443, 21])
            label = 1

        # --- DURUM 2: PORT SCANNING / TARAMA (Label: 1) ---
        elif case < 0.40:
            protocol = 1 # Genelde TCP ile yapılır
            interval = random.uniform(0.01, 0.1)  # Flood kadar hızlı değil ama seri
            pkt_size = 40 # Standart SYN paketi boyutu
            dst_port = random.randint(1, 1024)    # Sürekli değişen portlar
            label = 1

        # --- DURUM 3: NORMAL ICMP (GÜVENLİ PİNG) (Label: 0) ---
        elif case < 0.60:
            protocol = 3 # ICMP
            interval = random.uniform(0.5, 2.0)    # Standart 1 saniye civarı
            pkt_size = random.choice([32, 64, 512, 1200]) # Değişken boyutlar
            dst_port = 0
            label = 0

        
        else:
            protocol = random.choice([1, 2]) # TCP veya UDP
            interval = random.uniform(0.1, 5.0)   # Rastgele insan trafiği
            # Hem küçük (ACK/DNS) hem büyük (Download) paketler
            pkt_size = random.choice([random.randint(40, 100), random.randint(500, 1500)])
            dst_port = random.choice([80, 443, 53, 22]) 
            label = 0

        data.append([protocol, dst_port, pkt_size, interval, label])
    
    return pd.DataFrame(data, columns=['protocol', 'dst_port', 'pkt_size', 'interval', 'label'])


df = generate_universal_data(15000)
df.to_csv('data/synthetic_network_traffic.csv', index=False)
print("veri oluştu")