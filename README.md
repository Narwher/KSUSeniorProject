#
## Kennesaw State University Senior Project Spring 2020

A distributed machine learning program for learning and playing emulated games.

**The Team**

```
Benjamin Hermes - benmhermes@gmail.com
Josh Berezinski -
Efren Portugal -
Kurtis Webb -
Jay Harris - jwharris96@gmail.com
```



#### /src/Host.py
The master program which clients connect to. The host acts as a single control point for the machine learning network.
##### Execution
python -u Host.py

#### /src/Client.py
Client program which executes neural networks and interfaces with emulators.
##### Execution
python -u Client.py

#### /networks/
Directory housing various neural network implementations. They are selected by the Client
###### /networks/nn_sigmoid.py
Simple, Feed-Forward neural network using Sigmoid function.
