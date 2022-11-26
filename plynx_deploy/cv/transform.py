import cv2
import plynx.node
import numpy as np

from skimage.util import random_noise


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.output(name='img', var_type="py-image-file")
@plynx.node.param(name='coef_x', var_type=int, default=5)
@plynx.node.param(name='coef_y', var_type=int, default=5)
@plynx.node.operation(
    title="Box Blur",
)
def box_blur(img, coef_x, coef_y):
    return {
        "img": cv2.blur(img, (coef_x, coef_y)),
    }


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.output(name='img', var_type="py-image-file")
@plynx.node.param(name='coef_x', var_type=int, default=5)
@plynx.node.param(name='coef_y', var_type=int, default=5)
@plynx.node.param(name='sigma_x', var_type=float, default=0)
@plynx.node.param(name='sigma_y', var_type=float, default=0)
@plynx.node.operation(
    title="Gaussian Blur",
)
def gaussian_blur(img, coef_x, coef_y, sigma_x, sigma_y):
    return {
        "img": cv2.GaussianBlur(img, (coef_x, coef_y), sigmaX=sigma_x, sigmaY=sigma_y),
    }


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.output(name='img', var_type="py-image-file")
@plynx.node.param(name='kernel_size', var_type=int, default=5)
@plynx.node.operation(
    title="Median Blur",
)
def median_blur(img, kernel_size):
    return {
        "img": cv2.medianBlur(img, kernel_size),
    }


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.output(name='img', var_type="py-image-file")
@plynx.node.param(name='d', var_type=int, default=9)
@plynx.node.param(name='sigma_color', var_type=float, default=75)
@plynx.node.param(name='sigma_space', var_type=float, default=75)
@plynx.node.operation(
    title="Bilateral Filter (Blur)",
)
def bilateral_filter(img, d, sigma_color, sigma_space):
    return {
        "img": cv2.bilateralFilter(img, d=d, sigmaColor=sigma_color, sigmaSpace=sigma_space),
    }


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.output(name='img', var_type="py-image-file")
@plynx.node.param(name='amount', var_type=float, default=0.3)
@plynx.node.operation(
    title="Add Noise",
)
def add_noise(img, amount):
    noise_img = random_noise(img, mode="s&p", amount=amount)
    noise_img = np.array(255 * noise_img, dtype='uint8')
    return {
        "img": noise_img,
    }


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.output(name='img_1', var_type="py-image-file")
@plynx.node.output(name='img_2', var_type="py-image-file")
@plynx.node.output(name='img_3', var_type="py-image-file")
@plynx.node.operation(
    title="Sharpen image",
)
def sharpen_image(img):
    kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
    kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                                 [-1,2,2,2,-1],
                                 [-1,2,8,2,-1],
                                 [-1,2,2,2,-1],
                                 [-1,-1,-1,-1,-1]]) / 8.0
    return {
        "img_1": cv2.filter2D(img, -1, kernel_sharpen_1),
        "img_2":  cv2.filter2D(img, -1, kernel_sharpen_2),
        "img_3":  cv2.filter2D(img, -1, kernel_sharpen_3),
    }


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.output(name='edges', var_type="py-image-file")
@plynx.node.param(name='t_lower', var_type=float, default=100)
@plynx.node.param(name='t_upper', var_type=float, default=200)
@plynx.node.param(name='aperture_size', var_type=int, default=3)
@plynx.node.param(name='l2_gradient', var_type=bool, default=False)
@plynx.node.operation(
    title="Canny filter",
)
def canny(img, t_lower, t_upper, aperture_size, l2_gradient):
    return {
        "edges": cv2.Canny(
            img,
            threshold1=t_lower,
            threshold2=t_upper,
            apertureSize=aperture_size,
            L2gradient=l2_gradient
        ),
    }


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.input(name='edges', var_type="py-image-file")
@plynx.node.output(name='img', var_type="py-image-file")
@plynx.node.param(name='R', var_type=int, default=0)
@plynx.node.param(name='G', var_type=int, default=255)
@plynx.node.param(name='B', var_type=int, default=0)
@plynx.node.param(name='thickness', var_type=int, default=3)
@plynx.node.operation(
    title="Draw contours",
)
def draw_contours(img, edges, R, G, B, thickness):
    contours = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE
    )

    cv2.drawContours(img, contours[0], -1, (R, G, B), thickness=thickness)

    return {
        "img": img,
    }


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.output(name='gray', var_type="py-image-file")
@plynx.node.operation(
    title="To grayscale",
)
def to_gray(img):
    return {
        "gray": cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
    }


@plynx.node.input(name='gray', var_type="py-image-file")
@plynx.node.output(name='img', var_type="py-image-file")
@plynx.node.operation(
    title="To RGB image",
)
def to_rgb(gray):
    return {
        "img": cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR),
    }


@plynx.node.input(name='img', var_type="py-image-file")
@plynx.node.output(name='red', var_type="py-image-file")
@plynx.node.output(name='green', var_type="py-image-file")
@plynx.node.output(name='blue', var_type="py-image-file")
@plynx.node.operation(
    title="Split RGB channels",
)
def split_rgb_channels(img):
    blue, green, red = cv2.split(img)
    return {
        "red": red,
        "green": green,
        "blue": blue,
    }


@plynx.node.input(name='red', var_type="py-image-file")
@plynx.node.input(name='green', var_type="py-image-file")
@plynx.node.input(name='blue', var_type="py-image-file")
@plynx.node.output(name='img', var_type="py-image-file")
@plynx.node.operation(
    title="Merge RGB channels",
)
def merge_rgb_channels(red, green, blue):
    return {
        "img": cv2.merge([blue, green, red]),
    }


blurs = plynx.node.utils.Group(
    title="Blurs",
    items=[
        box_blur,
        gaussian_blur,
        median_blur,
        bilateral_filter,
    ]
)

noises = plynx.node.utils.Group(
    title="Noise",
    items=[
        add_noise,
    ]
)

edges = plynx.node.utils.Group(
    title="Edge detectors",
    items=[
        canny,
    ]
)

draws = plynx.node.utils.Group(
    title="Draw functions",
    items=[
        draw_contours,
    ]
)

others = plynx.node.utils.Group(
    title="Other",
    items=[
        sharpen_image,
        to_gray,
        to_rgb,
        split_rgb_channels,
        merge_rgb_channels,
    ]
)


COLLECTION = [
    blurs,
    noises,
    edges,
    draws,
    others,
]
