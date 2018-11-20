import cv2
import pickle
import os
from multiprocessing import Pool
import time


def get_top_k_result(match_list=None, k=10):
	result = (sorted(match_list, key=lambda l: l[1], reverse=True))
	return result[:k]


def extract(img, sift):
	_, des = sift.detectAndCompute(img, None)
	return des


def read(featurepath):
	with open(featurepath, "rb") as dump:
		des = pickle.load(dump)
	return des


def func(params):
	match_list = []
	feature_path = os.path.join('./sift', params[1])
	features = read(feature_path)
	if (features.all()) == None:
		return
	bf = cv2.BFMatcher()
	matches = bf.knnMatch(params[0], features, k=2)
	similar_list = []
	for m, n in matches:
		if m.distance < 0.75 * n.distance:
			similar_list.append([m])
	match_list.append([params[1], len(similar_list)])
	return match_list


def search(query_path):
	sift = cv2.xfeatures2d.SIFT_create()
	query_img = cv2.imread(query_path, 0)
	query_des = extract(query_img, sift)
	match_list = []
	indexed_list = os.listdir('./sift')
	for idx, feature_file in enumerate(indexed_list):
		feature_path = os.path.join('./sift', feature_file)
		features = read(feature_path)
		if (features.all()) == None:
			continue
		bf = cv2.BFMatcher()
		matches = bf.knnMatch(query_des, features, k=2)
		similar_list = []
		for m, n in matches:
			if m.distance < 0.75 * n.distance:
				similar_list.append([m])
		match_list.append([feature_file, len(similar_list)])

		del features, similar_list

	result = get_top_k_result(match_list=match_list, k=5)
	print (query_path.split('_')[2], result)
	return result


def search1(query_path):
	sift = cv2.xfeatures2d.SIFT_create()
	query_img = cv2.imread(query_path, 0)
	query_des = extract(query_img, sift)
	indexed_list = os.listdir('./sift')
	start_time = time.time()
	pool = Pool(4)
	pool.map(func, [query_des, indexed_list])
	print ("--- {} seconds ---".format(time.time() - start_time))


def search2(query_path, indexed_file):
	sift = cv2.xfeatures2d.SIFT_create()
	query_img = cv2.imread(query_path, 0)
	query_des = extract(query_img, sift)
	feature_path = os.path.join('./sift', indexed_file)
	features = read(feature_path)
	if (features.all()) == None:
		return
	bf = cv2.BFMatcher()
	matches = bf.knnMatch(query_des, features, k=2)
	similar_list = []
	match_list = []
	for m, n in matches:
		if m.distance < 0.75 * n.distance:
			similar_list.append([m])
	match_list.append([indexed_file, len(similar_list)])
	return match_list


def multiprocessing_search(data):
	query_des = data[0]
	id = data[1]
	indexed_des = data[2]
	# start_time2 = time.time()
	bf = cv2.BFMatcher()
	matches = bf.knnMatch(query_des, indexed_des, k=2)
	similar_list = []
	for m, n in matches:
		if m.distance < 0.75 * n.distance:
			similar_list.append([m])
	ret = [id, len(similar_list)]
	return ret


