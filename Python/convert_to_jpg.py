from PIL import Image

def convert_webp_to_jpg(input_path, output_path):
    image = Image.open(input_path)
    image.convert("RGB").save(output_path, "JPEG")
    print("Konversi selesai.")

# Mengganti dengan path file .webp input dan path file .jpg output
input_path = 'path_ke_file_input.webp'
output_path = "path_ke_file_output.jpg"

# Memanggil fungsi convert_webp_to_jpg
convert_webp_to_jpg(input_path, output_path)
