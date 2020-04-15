#! usr/bin/env python

import netfilter

def process_packet(packet):
    print(packet)

queue = netfilterqueue.NetfilterQueue()

queue.bind(0, process_packet)

queue.run()
