import os
import math

# number of GPUs available
numGpus = 1

# number of image pairs to process
# numImgs = 20
imgNum = 3

# N = int(math.ceil(float(numImgs)/numGpus))
for j in range(1, numGpus + 1):
	cmd = ''

	# for i in range(1, N + 1):
	i = imgNum
	# idx = (i-1) * numGpus + j	
	idx = imgNum
	print('working on image pair index = ' + str(idx))

	part1_cmd = ' th neuralstyle_seg.lua -content_image examples/input/in'+str(idx)+'.png -style_image examples/style/tar'+str(idx)+'.png -content_seg examples/segmentation/in'+str(idx)+'.png -style_seg examples/segmentation/tar'+str(idx)+'.png -index '+str(idx)+' -num_iterations 1000 -save_iter 500 -print_iter 1 -gpu '+str(j-1)+' -serial examples/tmp_results &&'

	part2_cmd = ' th deepmatting_seg.lua -content_image examples/input/in'+str(idx)+'.png -style_image examples/style/tar'+str(idx)+'.png -init_image examples/tmp_results/out'+str(idx)+'\_t_1000.png -content_seg examples/segmentation/in'+str(idx)+'.png -style_seg examples/segmentation/tar'+str(idx)+'.png -index '+str(idx)+' -num_iterations 1000 -save_iter 500 -print_iter 1 -gpu '+str(j-1)+' -serial examples/final_results -f_radius 15 -f_edge 0.01 &&'

	cmd = cmd + part1_cmd + part2_cmd

	cmd = cmd[1:len(cmd)-1]
	print(cmd)
	os.system(cmd)
 
	 
