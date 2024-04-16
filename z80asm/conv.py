import sys

def bin_to_hex(bin_file):
    """
    將二進位制檔案轉換為 0x 文字檔。

    Args:
        bin_file: 二進位制檔案路徑。

    Returns:
        None.
    """

    with open(bin_file, "rb") as f:
        bin_data = f.read()

    hex_data = ["0x{:02x}".format(b) for b in bin_data]

    for i in range(0, len(hex_data), 16):
        print(", ".join(hex_data[i:i + 16]), end="")
        print(",")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file")
    else:
        input_file = sys.argv[1]
        bin_to_hex(input_file)
