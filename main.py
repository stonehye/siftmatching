import sift_controller
import time
import cv2
import glob
from utils import *
from multiprocessing.pool import ThreadPool
import search

def Linear_search(query_path):
	sift = sift_controller.SIFT()
	result = sift.search(query_path)
	print("{} {}\n".format(img_path, ','.join(str(v) for v in result)))
	del sift
	
def Linear_search_prefetching(query_path):
	sift = sift_controller.SIFT()
	sift.inmemory_search(query_path)
	del sift

def Parallel_search_prefetching(query_path, num_threads):
	input_list = prefetching(query_path)
	pool = ThreadPool(processes=num_threads)
	pool.map(search.multiprocessing_search, input_list)



def test(case):
	correct_num = 0
	top_1_correct_num = 0
	top_5_correct_num = 0
	sift = sift_controller.SIFT()
	output_file = "noise_{}.txt".format(case)
	incorrect_txt = open(output_file, "w")
	forder_path = "./{}/*.jpg".format(case)
	image_list = glob.glob(forder_path)
	total_time = 0.

	for img_path in image_list:
		start_time = time.time()
		# case
		result = sift.search(img_path)
		end_time = time.time() - start_time
		total_time += end_time
		filename = img_path.split("/")[2]
		gt_label = filename.split("_")[2]
		top_1_result = [result[0]]
		top_5_result = result

		if isCorrect(gt_label, top_1_result):
			top_1_correct_num += 1
			top_5_correct_num += 1
		# print ("Correct: {}".format(gt_label))
		elif isCorrect(gt_label, top_5_result):
			top_5_correct_num += 1
		else:
			out_txt = "{} {}\n".format(img_path, ','.join(str(v) for v in result))
			# print ("Wrong: {}".format(gt_label))
			incorrect_txt.write(out_txt)
	# print("(top 1) {} : {} / {}".format(case, top_1_correct_num, len(image_list)))
	print("(top 5) {} : {} / {}".format(case, top_5_correct_num, len(image_list)))

	# print ("Total time : {}".format(total_time))
	incorrect_txt.close()


if __name__ == "__main__":

	case_list = ["border_output10", "border_output20", "border_output30", "caption_output", "flip_output", "logo_output10", "logo_output20", "logo_output30", "noise_output"]
	for case in case_list:
		test(case)
	
	img_path = "./ResizeData/741_RPI1477299693.jpg"

	#Linear search
	start = time.time()
	Linear_search(img_path)
	print("Total time: {}".format(time.time()-start))

	# # Linear search + inmemory prefetching
	# start = time.time()
	# Linear_search_prefetching(img_path)
	# print (time.time()-start)

	# Parallel search + inmemory prefetching
	# num_threads = cv2.getNumberOfCPUs()
	# start = time.time()
	# Parallel_search_prefetching(img_path, num_threads)
	# print(time.time()-start)

	