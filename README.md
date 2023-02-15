# Script for automatic mask generation of the desired parts with CIHP/LIP Segmentation

This script is to quickly generate masks with the selected items of the CIHP/LIP segmentation

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

├── src
│   ├── masks
│   ├── imageToMask_1.png
|   ├── ...
|   ├── imageToMask_n.png

**Example of input image**

![test1sweater1_vis.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16d0c67a-39fc-4213-a751-669a7af9a44b/test1sweater1_vis.png)

**Exampe script input**

`python3 cihpMaskGen.py --inpath ./ --outpath ./masks --top_inner`

**output**

![test1sweater1_vis_mask.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3856292d-ab28-4dee-95a6-7b29204cc5c5/test1sweater1_vis_mask.png)

# Script
