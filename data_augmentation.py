import imageio
import imgaug as ia
import imgaug.augmenters as iaa
import os


# Specify the input directory containing images
input_path = "./{your_directory_path}"
output_path = "./output_directory"  # Specify the output directory for augmented images

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

img_list = list()
for i in os.listdir(input_path):
    input_img = imageio.imread(os.path.join(input_path, i))
    
    print(f"Image shape: {input_img.shape}")
    
    hflip = iaa.Fliplr(p=1.0)
    input_hf = hflip.augment_image(input_img)

    vflip = iaa.Flipud(p=1.0)
    input_vf = vflip.augment_image(input_img)

    hue = iaa.AddToHueAndSaturation((-50, 50), per_channel=True)
    hue_input = hue.augment_image(input_img)
    
    temp_list = list()
    for i in range(15):  #modify range to chose how much random rotation you want!!
        cwRot = iaa.Affine(rotate=(-90, 90))
        input_CwRot = cwRot.augment_image(input_img)    
        
        temp_list.append(input_CwRot)

    # Append augmented images to img_list
    if len(temp_list)==1:
        img_list.extend([input_img, input_hf, input_vf, hue_input,temp_list[0]])
    else:
        img_list.extend([input_img, input_hf, input_vf, hue_input])
        img_list+=temp_list
        

# Save augmented images to the output directory
for idx, img in enumerate(img_list):
    output_filename = os.path.join(output_path, f"augmented_{idx}.png")
    imageio.imwrite(output_filename, img)

print(f"Saved {len(img_list)} augmented images to {output_path}")


