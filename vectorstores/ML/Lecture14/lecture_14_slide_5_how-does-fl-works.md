# Slide 5 of Lecture 14 contains information about the How does FL works?.

Federated learning unfolds in iterative rounds: multiple participants keep their data local while downloading a shared, often pre-trained, model from a coordinating server. Each party fine-tunes the model on its private dataset, summarizes and encrypts the updated parameters, and sends these updates back to the server, which decrypts, averages, and merges them into the centralized model. The process repeats until convergence, enabling collaborative training without exposing raw data.
