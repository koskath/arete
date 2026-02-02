# Slide 19 of Lecture 13 contains information about the Code Snippet.

This slide shows a canonical convolutional base built by stacking `Conv2D` and `MaxPooling2D` layers that accept `(image_height, image_width, color_channels)` tensors, making the architecture suitable for RGB CIFAR inputs.

`# Convolutional base using a common pattern: a stack of Conv2D and MaxPooling2D layers.`
`# CNN takes tensors of shape (image_height, image_width, color_channels), color_channels refers to (R,G,B) to support the format of CIFAR images.`
`model = models.Sequential()`
`model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))`
`model.add(layers.MaxPooling2D((2, 2)))`
`model.add(layers.Conv2D(64, (3, 3), activation='relu'))`
`model.add(layers.MaxPooling2D((2, 2)))`
`model.add(layers.Conv2D(64, (3, 3), activation='relu'))`

After these convolution and pooling blocks, the output is flattened and sent through dense layers for classification, so the sequence of `Conv2D` (32 filters, 3×3 kernel, ReLU), `MaxPooling2D` (2×2), `Conv2D` (64 filters, 3×3, ReLU), `MaxPooling2D` (2×2), and another `Conv2D` with 64 filters progressively extracts rich features from the 32×32 RGB inputs while downsampling the spatial dimensions.
