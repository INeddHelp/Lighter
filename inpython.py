#def lighter(*files):
#    import os
#    import math
#    for file in files:
#        if os.path.isfile(file):
#            file_size = os.path.getsize(file)
#            if file_size <= 100 * 1024 * 1024:
#                print(file)
#            else:
#                file_name, file_ext = os.path.splitext(file)
#                num_parts = math.ceil(file_size / (100 * 1024 * 1024))
#                dir_name = f"{file_name}_parts"
#                os.makedirs(dir_name, exist_ok=True)
#                with open(file, 'rb') as f:
#                    for i in range(num_parts):
#                        part_path = f"{dir_name}/{file_name}_part{i + 1}{file_ext}"
#                        with open(part_path, 'wb') as part:
#                            part.write(f.read(100 * 1024 * 1024))
#                        print(part_path)
#        else:
#            print(f"File not found: {file}")
#
#