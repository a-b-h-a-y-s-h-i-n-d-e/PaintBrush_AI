import numpy as np
import tensorflow as tf  
import tensorflow_hub as hub
from PIL import Image


hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def process_image(image_path):
    image = Image.open(image_path)
    image = np.array(image).astype(np.float32)[np.newaxis, ...] / 255.
    image = tf.image.resize(image, (256, 256))
    return image

def inference(content_path, style_path):
    content_image = process_image(content_path)
    style_image = process_image(style_path)

    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0]

    # now converting tensor to image
    stylized_image_np = tf.squeeze(stylized_image).numpy() * 255
    stylized_image_np = stylized_image_np.astype(np.uint8)
    stylized_image_pil = Image.fromarray(stylized_image_np)

    resized_image = stylized_image_pil.resize((300, 200), Image.Resampling.LANCZOS)
    return resized_image