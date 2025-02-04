![Screenshot 2025-02-04 202538](https://github.com/user-attachments/assets/e775b9d7-e126-4ead-ab59-c3851d490b09)

# Pokédex Classifier

## Overview

This project is a Pokédex-inspired Pokémon classifier built using TensorFlow with EfficientNetB0 as the base model. The frontend is designed using PyQt6, replicating the UI/UX of a Pokédex. Users can upload an image of a Pokémon, and the classifier predicts its name. Additionally, Pokémon attributes are fetched using an open-source RESTful API.

## Features
- **Image Classification :** Uses a TensorFlow model with **EfficientNetB0** to classify Pokémon.
- **Pokédex UI :** Designed using **PyQt6** with a background image resembling a Pokédex.
- **File Upload :** Users can select an image from their file system.
- **Pokémon Attribute Fetching :** Fetch Pokémon details via [PokéAPI](https://pokeapi.co/).
- **Real-time Prediction :** The model predicts and displays the Pokémon name along with its attributes.

## Model and Dataset Details
- **Framework :** TensorFlow
- **Base Model :** EfficientNetB0
- **Dataset :** [1000 Pokemon Dataset](https://www.kaggle.com/datasets/noodulz/pokemon-dataset-1000)

## Future Improvements
- Optimizing the model by experimenting with advanced techniques such as fine-tuning, or incorporating more powerful architectures to increase prediction accuracy.
- Expand the model by incorporating additional Pokémon classes to enhance its classification capabilities.
- Design a better GUI for the application.
