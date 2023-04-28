#from pathlib import Path
#import math
#
#
#def lighter(*file_paths):
#    max_size = 100 * 1024 * 1024  # 100.00 MB in bytes
#    parts_list = []
#
#    for file_path in file_paths:
#        full_path = Path(file_path).resolve()
#
#        if full_path.is_dir():
#            # Iterate over all files in the directory
#            for file in full_path.glob('*'):
#                if file.is_file():
#                    file_size = file.stat().st_size
#
#                    if file_size <= max_size:
#                        parts_list.append([str(file)])
#                    else:
#                        file_name, file_ext = file.stem, file.suffix
#                        num_parts = math.ceil(file_size / max_size)
#
#                        dir_name = f"{file_name}_parts"
#                        Path(dir_name).mkdir(exist_ok=True)
#
#                        parts = []
#                        with open(file, 'rb') as f:
#                            for i in range(num_parts):
#                                part_path = f"{dir_name}/{file_name}_part{i + 1}{file_ext}"
#                                with open(part_path, 'wb') as part:
#                                    part.write(f.read(max_size))
#                                parts.append(str(part_path))
#
#                        parts_list.append(parts)
#        elif full_path.is_file():
#            file_size = full_path.stat().st_size
#
#            if file_size <= max_size:
#                parts_list.append([str(full_path)])
#            else:
#                file_name, file_ext = full_path.stem, full_path.suffix
#                num_parts = math.ceil(file_size / max_size)
#
#                dir_name = f"{file_name}_parts"
#                Path(dir_name).mkdir(exist_ok=True)
#
#                parts = []
#                with open(full_path, 'rb') as f:
#                    for i in range(num_parts):
#                        part_path = f"{dir_name}/{file_name}_part{i + 1}{file_ext}"
#                        with open(part_path, 'wb') as part:
#                            part.write(f.read(max_size))
#                        parts.append(str(part_path))
#
#                parts_list.append(parts)
#        else:
#            print(f"File not found: {file_path}")
#
#    print(parts_list)
#
#
#lighter("Exposing The Puppet Masters.webm")

# make me a lighter function that takes a file path and splits it into 100MB parts

def lighter(*files):
    import os
    import math
    for file in files:
        if os.path.isfile(file):
            file_size = os.path.getsize(file)
            if file_size <= 100 * 1024 * 1024:
                print(file)
            else:
                file_name, file_ext = os.path.splitext(file)
                num_parts = math.ceil(file_size / (100 * 1024 * 1024))
                dir_name = f"{file_name}_parts"
                os.makedirs(dir_name, exist_ok=True)
                with open(file, 'rb') as f:
                    for i in range(num_parts):
                        part_path = f"{dir_name}/{file_name}_part{i + 1}{file_ext}"
                        with open(part_path, 'wb') as part:
                            part.write(f.read(100 * 1024 * 1024))
                        print(part_path)
        else:
            print(f"File not found: {file}")


lighter("/home/leonardo/Desktop/Lighter/lighter/Exposing\\ The\\ Puppet\\ Masters.webm")

# Q: I found a bug, it does not find the file Exposing The Puppet Masters.webm even tho it is in the same directory as the script can you fix it?
