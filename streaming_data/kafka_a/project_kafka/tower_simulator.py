import time
import json
import pandas as pd
from kafka import KafkaProducer
from datetime import datetime
import random

# 1. إعدادات كافكا
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

TOPIC_NAME = 'telecom-stream'
DATA_FILE = 'towers.csv'

print(f"🚀 Starting Smart Simulator...")

# 2. قراءة الملف مرة واحدة بس (عشان ناخد منه العناوين والأماكن)
try:
    # بنقرا الملف وناخد منه الأعمدة الثابتة بس
    static_df = pd.read_csv(DATA_FILE)
    static_df = static_df.fillna("")
    print(f"✅ Loaded {len(static_df)} towers catalog.")
except Exception as e:
    print(f"❌ Error loading file: {e}")
    exit()

def generate_live_data(row):
    """
    دالة بتاخد بيانات البرج الثابتة وتضيف عليها قراءات متغيرة
    """
    # تحويل الصف لـ Dictionary
    data = row.to_dict()
    
    # --- توليد داتا متغيرة (Simulation) ---
    
    # 1. قوة الإشارة (تتغير عشوائياً بين -120 و -50)
    data['signal_strength'] = random.randint(-120, -50)
    
    # 2. جودة الإشارة (تعتمد على القوة)
    if data['signal_strength'] > -70:
        data['signal_quality'] = "Excellent"
    elif data['signal_strength'] > -90:
        data['signal_quality'] = "Good"
    elif data['signal_strength'] > -105:
        data['signal_quality'] = "Poor"
    else:
        data['signal_quality'] = "Dead Zone"

    # 3. حالة البرج (لو الإشارة وحشة جداً يبقى فيه مشكلة)
    # بنعمل احتمالية 5% إن البرج يقع عشان نشوف الـ Alert
    if data['signal_strength'] < -110 or random.random() < 0.05:
        data['tower_status'] = "Inactive"
        data['is_anomaly'] = True
    else:
        data['tower_status'] = "Active"
        data['is_anomaly'] = False
        
    # 4. عدد المكالمات (رقم عشوائي)
    data['total_calls'] = random.randint(500, 5000)
    # المكالمات الواقعة (نسبة من التوتال)
    data['drop_calls'] = int(data['total_calls'] * random.uniform(0.01, 0.10))
    # حساب النسبة
    data['drop_rate'] = round((data['drop_calls'] / data['total_calls']) * 100, 2)
    
    # 5. سرعة النت والتحميل
    data['speed'] = round(random.uniform(5.0, 100.0), 2)
    data['avg_load'] = round(random.uniform(0.1, 0.9), 2)
    data['latency'] = round(random.uniform(20, 200), 2)

    # 6. تحديث الوقت للحظة الحالية
    data['updated_dt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['ingestion_time'] = time.time()
    
    return data

# 3. حلقة الإرسال المستمرة
def run_simulator():
    while True:
        # بنلف على كل برج في الكتالوج
        for index, row in static_df.iterrows():
            
            # بنخلق داتا جديدة للبرج ده
            live_message = generate_live_data(row)
            
            # إرسال لـ Kafka
            producer.send(TOPIC_NAME, value=live_message)
            
            # طباعة للمتابعة (كل 10 أبراج مثلاً عشان الزحمة)
            if index % 10 == 0:
                print(f"📡 Sending: {live_message['tower_id']} | Signal: {live_message['signal_strength']}dBm | Time: {live_message['updated_dt']}")
            
            # تأخير بسيط جداً عشان مانموتش الجهاز
            time.sleep(0.05) 
            
        print("🔄 Finished one cycle, restarting loop...")
        time.sleep(5) # استراحة ثانيتين بعد ما يخلص كل الأبراج

if __name__ == "__main__":
    run_simulator()