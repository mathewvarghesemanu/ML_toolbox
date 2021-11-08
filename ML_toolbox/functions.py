import matplotlib

def plot_side_by_side(image1,image2,label1,label2):
    fig=plt.figure(figsize=(20,20))
    ax1=fig.add_subplot(1,2,1)
    ax1.set_title(label1)
#     ax1.set_axis_off
    ax1.imshow(image1)
    ax2=fig.add_subplot(1,2,2)
    ax2.set_title(label2)
#     ax2.set_axis_off
    ax2.imshow(image2)
    return True

plot_side_by_side(image1=image,image2=added_image,label1="Original Image",label2="Added Image")