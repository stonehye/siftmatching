import glob
import sift_controller
import os


def index():
	SIFT = sift_controller.SIFT()
	SIFT.dump_onefile()

	for img_path in glob.glob("./ResizeData/*.jpg"):
		img_name = img_path.split("/")[-1]
		SIFT.dump_eachfile(img_name)


# if __name__ == "__main__":
# # 	index()