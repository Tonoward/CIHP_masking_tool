# Script for automatic mask generation of the desired parts with CIHP/LIP Segmentation

This script is to quickly generate masks with the selected items of the CIHP(Crowd Instance-level Human Parsing)/LIP(Look into person) segmentation

Some references:

[Look into person](https://github.com/Engineering-Course/LIP_JPPNet)

[CIHP parsing](https://github.com/Engineering-Course/CIHP_PGN)

# Usage

it takes as arguments the input path with a batch of images and a directory as output path, selected item(s) are added as arguments

```
python3 --inpath <input_path> --outpath <output_path> <mask_item>
```

### Available argument items:

- —hair
- —hat
- —face
- —torso
- —top_inner
- —top_outer
- —arm_left
- —arm_right
- —dress
- —bottom_pants
- —bottom_shorts
- —leg_left
- —leg_right
- —shoe_left
- —shoe_right

At least one item to mask is needed for the script to run. It is possible to add multiple items

### Option to dilate masks

You can provide an amount of dilation for the resulting masks with the ```--dilation``` argument followed by an integer as dilation value

# Example

In this directory tree

```
src
├── masks
├── imageToMask_1.png
├── ...
├── imageToMask_n.png
```

**Example of input image**

![example_input_img](https://github.com/Tonoward/CIHP_masking_tool/blob/main/inputimg_example_1.png?raw=true)

**Exampe script input**

`python3 cihpMaskGen.py --inpath ./ --outpath ./masks --top_inner`

**output**

![example_output_img](https://github.com/Tonoward/CIHP_masking_tool/blob/main/outputimg_example_1.png?raw=true)
