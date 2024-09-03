from confluent_kafka import Producer
import json,os
conf={'bootstrap.servers':'localhost:9092'}
producer =Producer(**conf)
def delivery_report(err,msg):
    if err is not None:
        print("Delivery report:{err}")
    else:
        print(f"Delivery report{msg.topic()}{msg.partition()}")
def send_like_event(post_id):
    producer.produce('location_updates',key=str(post_id),
                      value=json.dumps({"post_id":post_id}),
    callback=delivery_report)
    print("Delivery report")
    producer.flush()

