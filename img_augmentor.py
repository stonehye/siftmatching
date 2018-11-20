import Augmentor
from PIL import Image
from PIL import ImageDraw
import os
import glob
import random
from utils import *


def add_logo(ori_img_path, logo_img_path):
	ori_img1 = Image.open(ori_img_path)
	ori_img2 = Image.open(ori_img_path)
	ori_img3 = Image.open(ori_img_path)

	logo_img = Image.open(logo_img_path)
	resize_logo_img1 = logo_img.resize((95, 95))
	resize_logo_img2 = logo_img.resize((134, 134))
	resize_logo_img3 = logo_img.resize((164, 164))

	ori_img1.paste(resize_logo_img1, (120, 10), resize_logo_img1)
	ori_img2.paste(resize_logo_img2, (10, 10), resize_logo_img2)
	ori_img3.paste(resize_logo_img3, (10, 10), resize_logo_img3)

	path_tmp = parse_glob(ori_img_path)
	# output_path = "./thumb/output/thumb_logo_" + path_tmp
	output_path1 = "./logo_output10/thumb_logo10_" + path_tmp
	output_path2 = "./logo_output20/thumb_logo20_" + path_tmp
	output_path3 = "./logo_output30/thumb_logo30_" + path_tmp

	ori_img1.save(output_path1)
	ori_img2.save(output_path2)
	ori_img3.save(output_path3)


def add_caption(ori_img_path):
	ori_img = Image.open(ori_img_path)
	draw = ImageDraw.Draw(ori_img)
	draw.text((10, 10), "Sogang University", fill=(0, 0, 0))
	draw.text((40, 140), "Multimedia System lab", fill=(0, 0, 0))
	path_tmp = parse_glob(ori_img_path)
	# output_path = "./thumb/output/thumb_caption_" + path_tmp
	output_path = "./caption_output/thumb_caption_" + path_tmp
	ori_img.save(output_path)


def add_border(ori_img_path):
	border_image1 = Image.open("resize_logo_300.jpg")
	border_image2 = Image.open("resize_logo_300.jpg")
	border_image3 = Image.open("resize_logo_300.jpg")
	ori_img = Image.open(ori_img_path)

	border_image1.paste(ori_img.resize((284, 284)), (8, 8))
	border_image2.paste(ori_img.resize((268, 268)), (16, 16))
	border_image3.paste(ori_img.resize((251, 251)), (25, 25))

	path_tmp = parse_glob(ori_img_path)
	# output_path = "./thumb/output/thumb_border_" + path_tmp
	output_path1 = "./border_output10/thumb_border10_" + path_tmp
	output_path2 = "./border_output20/thumb_border20_" + path_tmp
	output_path3 = "./border_output30/thumb_border30_" + path_tmp

	border_image1.save(output_path1)
	border_image2.save(output_path2)
	border_image3.save(output_path3)


if __name__ == "__main__":

	_THUMB_FOLDER = "./ResizeData"
	_OUTPUT_FOLDER_noise = "../noise_output"
	p_noise = Augmentor.Pipeline(_THUMB_FOLDER, _OUTPUT_FOLDER_noise)
	p_noise.random_erasing(probability=1.0, rectangle_area=0.5)
	p_noise.sample(1099)

	original_image_list = glob.glob("./ResizeData/*.jpg")
	for idx, img_path in enumerate(original_image_list):
		add_caption(img_path)
		add_logo(img_path, "minions_PNG84.png")
		add_border(img_path)
	print ("{} / {}".format(idx+1, len(original_image_list)))
