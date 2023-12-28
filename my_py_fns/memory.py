import gc
import torch


def torch_var_size(var, unit="KB"):
    if unit == "KB":
        size_ = var.element_size() * var.nelement() // 1024
        size_ = f"{size_}KB"

    elif unit == "MB":
        size_ = var.element_size() * var.nelement() // 1024 // 1024
        size_ = f"{size_}MB"
    else:
        raise ValueError("unit must be KB or MB")

    return size_


def clean_cache():
    gc.collect()
    torch.cuda.empty_cache()


def report_memory():
    total_mem = 0
    for obj in gc.get_objects():
        try:
            if torch.is_tensor(obj) or (hasattr(obj, "data") and torch.is_tensor(obj.data)):
                mem = obj.element_size() * obj.nelement()
                total_mem += mem
                print(f"Object: {obj}, occupies {mem} bytes on GPU")
        except Exception as e:
            pass
    print(f"Total memory occupied by tensors: {total_mem} bytes")
