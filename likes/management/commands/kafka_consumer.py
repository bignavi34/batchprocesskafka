from django.core.management.base import BaseCommand
from confluent_kafka import Consumer,KafkaException
import json
import os
import time
from collections import defaultdict
from django.db import transaction
from likes.models import Post
class Command(BaseCommand):
    help="run a location update"
    def process_batch(self,like_batch):
        with transaction.atomic():
            for k,v in like_batch.items():
                post=Post.objects.get(id=k)
                post.like+=v
                post.save()
        print(like_batch)
        
    def handle(self, *args,**options):
        like_batch=defaultdict(int)
        conf={'bootstrap.servers':'localhost:9092',
              'group.id':"location_updates",
              'auto.offset.reset':'earliest',
             }

        consumer=Consumer(conf)
        consumer.subscribe(['location_updates'])
        total_message=0
        try:
            while True:
                msg=consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(msg.error())
                    continue
                data=json.loads(msg.value().decode('utf-8'))
                post_id=data['post_id']
                like_batch[post_id]+=1
                total_message+=1
                print(data)
                if total_message >=10:
                    self.process_batch(like_batch)
                    like_batch.clear()
                    total_message=0
                    
        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()