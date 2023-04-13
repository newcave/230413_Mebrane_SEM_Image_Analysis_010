import streamlit as st
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("K-water막여과정수장의 Membrane의 공극 열화를 이미지로 분석")

# Add a slider for the threshold value
    st.sidebar.header("Threshold")
    threshold = st.sidebar.slider("Set Threshold:", min_value=0, max_value=255, value=128, step=1)
    
    
    st.sidebar.header("Input Images")
    use_default_images = st.sidebar.checkbox("Use Default Images")

    if use_default_images:
        img1 = Image.open("img_org.png")
        img2 = Image.open("image01.png")
        img3 = Image.open("image02.png")
        img4 = Image.open("image03.png")
        img5 = Image.open("new_mem_rev.png")
    else:
        img1 = st.sidebar.file_uploader("Upload Image 1:", type=["png", "jpg", "jpeg"])
        img2 = st.sidebar.file_uploader("Upload Image 2:", type=["png", "jpg", "jpeg"])
        img3 = st.sidebar.file_uploader("Upload Image 3:", type=["png", "jpg", "jpeg"])
        img4 = st.sidebar.file_uploader("Upload Image 4:", type=["png", "jpg", "jpeg"])
        img5 = st.sidebar.file_uploader("Upload Image 5:", type=["png", "jpg", "jpeg"])

        if img1 and img2 and img3 and img4 and img5:
            img1 = Image.open(img1)
            img2 = Image.open(img2)
            img3 = Image.open(img3)
            img4 = Image.open(img4)
            img5 = Image.open(img5)
        else:
            st.warning("Please upload all 5 images or use the default images.")
            return

    process_images(img1, img2, img3, img4, img5, threshold)    
        
    img_list, black_ratios, black_ratio_diffs = process_images(img1, img2, img3, img4, img5, threshold)

    plot_images(img_list, black_ratios, black_ratio_diffs, threshold)     
        

   
        
def process_images(img1, img2, img3, img4, img5, threshold):
    # Resize all images to match the size of img1
    width, height = img1.size
    img2 = img2.resize((width, height))
    img3 = img3.resize((width, height))
    img4 = img4.resize((width, height))
    img5 = img5.resize((width, height))

    # Print the threshold value
    st.write(f"THRESHOLD OF PORE REPRESENTATION: {threshold}")

    # Calculate the number of black pixels in each image based on the threshold
    black_pixels1 = sum([1 for pixel in img1.getdata() if sum(pixel)/3 <= threshold])
    black_pixels2 = sum([1 for pixel in img2.getdata() if sum(pixel)/3 <= threshold])
    black_pixels3 = sum([1 for pixel in img3.getdata() if sum(pixel)/3 <= threshold])
    black_pixels4 = sum([1 for pixel in img4.getdata() if sum(pixel)/3 <= threshold])
    black_pixels5 = sum([1 for pixel in img5.getdata() if sum(pixel)/3 <= threshold])

    # Calculate the black pixel ratio for each image
    count1 = img1.size[0] * img1.size[1]
    count2 = img2.size[0] * img2.size[1]
    count3 = img3.size[0] * img3.size[1]
    count4 = img4.size[0] * img4.size[1]
    count5 = img5.size[0] * img5.size[1]

    black_ratio1 = black_pixels1 / count1
    black_ratio2 = black_pixels2 / count2
    black_ratio3 = black_pixels3 / count3
    black_ratio4 = black_pixels4 / count4
    black_ratio5 = black_pixels5 / count5

    # Compute the differences in black pixel ratios between the original and processed images
    black_ratio_diff1 = (black_ratio1 - black_ratio2) / black_ratio1
    black_ratio_diff2 = (black_ratio1 - black_ratio3) / black_ratio1
    black_ratio_diff3 = (black_ratio1 - black_ratio4) / black_ratio1
    black_ratio_diff4 = (black_ratio1 - black_ratio5) / black_ratio1

    # Prepare img_list, black_ratios and black_ratio_diffs for plot_images()
    img_list = [img1, img2, img3, img4, img5]
    black_ratios = [black_ratio1, black_ratio2, black_ratio3, black_ratio4, black_ratio5]
    black_ratio_diffs = [black_ratio_diff1, black_ratio_diff2, black_ratio_diff3, black_ratio_diff4]

    # Return img_list, black_ratios, and black_ratio_diffs
    return img_list, black_ratios, black_ratio_diffs

def plot_images(img_list, black_ratios, black_ratio_diffs, threshold):
    # Plot the images in a row
    fig, ax = plt.subplots(1, 5, figsize=(20, 4))
    for i, img in enumerate(img_list):
        ax[i].imshow(img)
        ax[i].axis('off')
        ax[i].set_title(f"Image {i+1}")
    
    # Display the image grid in Streamlit
    st.pyplot(fig)

    # Draw bar charts to show the pore ratio differences for each image
    fig, ax = plt.subplots()
    ax.bar(range(1, 6), black_ratios)
    ax.set_xticks(range(1, 6))
    ax.set_xticklabels([f"막 SEM image {i+1}" for i in range(5)])
    ax.set_ylabel('Pore Ratio Analyzed(%)')
    ax.set_title('막여과 공극의 비율 분석')

    # Display the bar chart in Streamlit
    st.pyplot(fig)

    # Plot line graphs to display the change in pore reduction for each image
    fig, ax = plt.subplots()
    ax.plot(range(2, 6), black_ratio_diffs, marker='o')
    ax.set_xticks(range(2, 6))
    ax.set_xticklabels([f"Image {i+1}" for i in range(1, 5)])
    ax.set_ylabel('막여과 오염에 따른 공극률의 감소(%)')
    ax.set_title('막여과 오염에 따른 공극률의 감소(%)')

    # Display the line graph in Streamlit
    st.pyplot(fig)


if __name__ == "__main__":
    main()

