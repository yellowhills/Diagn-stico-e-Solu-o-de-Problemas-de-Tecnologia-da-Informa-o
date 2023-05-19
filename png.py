from PIL import Image

def compress_image(input_image_path, output_image_path, quality):
    with Image.open(input_image_path) as image:
        image.save(output_image_path, "JPEG", optimize=True, quality=quality)

def decompress_image(input_image_path, output_image_path):
    with Image.open(input_image_path) as image:
        image.save(output_image_path)

# Exemplo de uso
input_path = "input.jpg"
output_path = "compressed.jpg"
decompressed_path = "decompressed.jpg"
compression_quality = 50

# Comprimir a imagem
compress_image(input_path, output_path, compression_quality)

# Descomprimir a imagem
decompress_image(output_path, decompressed_path)
