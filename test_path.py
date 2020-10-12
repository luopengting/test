import os


def get_relpath(path, base_path):
    r_path = os.path.relpath(path, base_path)

    if r_path == ".":
        return "./"
    return f"./{r_path}"


base_path = "/"
path = "/"
r_path = os.path.relpath(path, base_path)

print(r_path)
print("===: ", get_relpath(path, base_path))

base_path = "/data/luopengting/summaries/"
path = "/data/luopengting/summaries/demo_param_importances"
r_path = os.path.relpath(path, base_path)
print(r_path)
print("===: ", get_relpath(path, base_path))
