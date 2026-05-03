import pandas as pd
import pickle
import os

def get_analysis_results(csv_file_path):
    
    with open('models/ids_model.pkl', 'rb') as f:
        model = pickle.load(f)

    
    df = pd.read_csv(csv_file_path)
    df['interval'] = df['Time'].diff().fillna(0.5)

    def map_proto(p):
        p = str(p).upper()
        if 'ICMP' in p: return 3
        if 'UDP' in p: return 2
        return 1

    df['proto_num'] = df['Type'].apply(map_proto)
    
    # 3. Tahminleri Yap
    results = []
    for i, row in df.iterrows():
        features = pd.DataFrame([[row['proto_num'], 80, row['Size'], row['interval']]], 
                                columns=['protocol', 'dst_port', 'pkt_size', 'interval'])
        
        pred = model.predict(features)[0]
        results.append("🚨 SALDIRI" if pred == 1 else "✅ GÜVENLİ")
    
    df['DURUM'] = results
    return df