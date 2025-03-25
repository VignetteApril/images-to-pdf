# Image to PDF Converter

This Python script converts multiple images from a specified directory into a single PDF file. It supports various image formats and allows customization of sorting and output settings.

## Features

- Converts multiple images to a single PDF file.
- Supports image formats: JPG, JPEG, PNG, BMP, WebP, TIFF.
- Sorts images by filename (natural sort) or modification time.
- Customizable output filename, image extensions, and sorting method.
- High-quality PDF output with configurable DPI and image quality.

## Prerequisites

- Python 3.x
- `Pillow` library (for image processing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-to-pdf-converter.git
   cd image-to-pdf-converter
   ```

2. Install the required dependencies:
   ```bash
   pip install pillow
   ```

## Usage

Run the script from the command line with the following arguments:

```bash
python main.py <input_dir> [options]
```

### Arguments

- **`input_dir`**: Path to the directory containing the images.
- **`-o`, `--output`**: Output PDF filename (default: `output.pdf`).
- **`-e`, `--ext`**: Image extensions to include, separated by commas (default: `jpg`).
- **`--sort-by`**: Sorting method for images (`name` or `mtime`, default: `name`).

### Examples

1. Convert all `.jpg` images in the `images` directory to a PDF:
   ```bash
   python main.py images
   ```

2. Convert `.png` and `.jpg` images, sort by modification time, and save as `my_output.pdf`:
   ```bash
   python main.py images -o my_output.pdf -e png,jpg --sort-by mtime
   ```

## Output

The script generates a PDF file in the specified output location. A success message is displayed with the number of pages and the absolute path of the PDF file.

## Error Handling

- The script validates the input directory and checks for supported image files.
- If an error occurs (e.g., invalid directory or no images found), an error message is displayed, and the script exits.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, report issues, or suggest improvements!