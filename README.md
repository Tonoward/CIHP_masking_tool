# Script for automatic mask generation of the desired parts with CIHP/LIP Segmentation

This script is to quickly generate masks with the selected items of the CIHP(Crowd Instance-level Human Parsing)/LIP(Look in person) segmentation

# Usage

it takes as arguments the input path with a batch of images and a directory as output path, selected body part is added as arguments

```jsx
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

At least one item to mask is needed for the script to run.

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
