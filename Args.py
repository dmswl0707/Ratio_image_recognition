import torch
import torch.nn as nn


Args = {"name" : 'optimizer_Adam_ResNet152_customed_CAWR',
        #"Act_fu" : nn.ReLU(),
        "mean": (0.485, 0.456, 0.406),
        "std":(0.229, 0.224, 0.225),
        #"beta" : 1.0,
        "lr" : 0,  # 스크래치는 논문 그대로 , 전이학습은 1/10로...

        #"eta_min" : 0.00001,
        #"weight_decay" : 0.001,
        "batch_size": 80, #80
        "Epoch" : 100,
        #"num_fold" : 5,
        "patience" : 20,
        "device" : torch.device('cuda' if torch.cuda.is_available() else 'cpu'),
        }


