from pathlib import Path


def adapt_path(input_path):
    """
    input_path: str or Path
        e.g. ~/tmp/NSC/data/dataset_L0_exp_set_0.h5
        e.g. /home/username/tmp/NSC/data/dataset_L0_exp_set_0.h5
        e.g. home/username/tmp/NSC/data/dataset_L0_exp_set_0.h5
        e.g. ./src/username/tmp/NSC/data/dataset_L0_exp_set_0.h5

    output_path: replace with correct username
    """
    home_dir = Path.home()
    if "home" in str(input_path):
        relative_path = str(input_path).split("home")[1].split("/")[2:]
        # output_path = Path("/".join(["~"] + relative_path)).expanduser()
        output_path = Path("/".join([str(home_dir)] + relative_path))
    elif "~" in str(input_path):
        # output_path = Path(input_path).expanduser()
        relative_path = str(input_path).split("~")[1:]
        # print(f"relative_path: {relative_path}")
        output_path = Path("/".join([str(home_dir)] + relative_path))
    else:
        output_path = Path(input_path)

    # replace tmp with data
    if "/tmp/" in str(output_path):
        output_path = Path(str(output_path).replace("/tmp/", "/data/"))

    return output_path


print(adapt_path("./src/username/tmp/NSC/data/dataset_L0_exp_set_0.h5"))
