# DeepLearning

PROJECT DESCRIPTION
==============================================================================================
This a description of my project design, methods, and results for the NVIDIA Jeston TX2 assignment
==============================================================================================


OBJECTIVE:  

Take still images of objects from the apartment with the NVIDIA TX2 camera, run them through a pre-existing Digital Neural Network (DNN) and determine if objects are successfully classified by the DNN



DATA: 
 
I collected 20 small objects from around my apartment that would fit within the field of view of the NVIDIA TX2 camera.  Objects were various shapes, colors, and materials.  Half of the objects were recyclable, and the other half were not.  Ten pictures were taken of each object, so that different perspectives were captured of the same object.  A total of 200 Test Images were created, half were in the 'Recyclable' category and half were in the 'Non-Recyclable' category.  The steps in the following 'PROCESSING STEPS FOR PROJECT' indicate how the images were taken. 

   - All original 200 Test Images can be found in their respective directories:

		/home/learner/Documents/datasets_objects/nonrecycle_recycle/test/nonrecycle
		/home/learner/Documents/datasets_objects/nonrecycle_recycle/test/recycle	



PROCESSING STEPS FOR PROJECT:  
	 
   - From the NVIDIA Hello AI World tutorial website on Github, I cloned an existing code repository (which had various DNNs, PyTorch, classification models, sample data, etc.), performed the install, and then compiled the project.  See the 'journal_sal.txt' file for more details on how this was done, with issues and resolutions [1]

   - Next, I gathered all objects that would become my Test Images, and placed each object into either a 'recyclable' or 'non-recycleble' group.  Exactly ten recyclable objects were placed in the 'recyclable' group and ten in the 'non-recyclable' group  

   - I then set a flat staging area in-front of the NVIDA camera (with a blank background) so that each object could be placed on a stable surface with no 'noise' in the background

   - Turned on the NVIDA TX2 camera with the 'Data Capture Control' tool 

   - With the NVIDA 'Data Capture Control' tool, I set objects in-front of the camera and took pictures of each object for the non-recycled group at various angles/rotation.  Ten pictures were taken of each object at various rotations and angles, for a total of 100 Test images considered non-recyclable.  The number of total Test images was subjective, but various angles were taken to determine later if one position rendered a different classification than another.  Images were stored in the directory mentioned in the 'DATA' section.  The image file, 'Group_NonRecycle_Test_Images.JPG' on Github shows all of the objects selected [2]

   - With the NVIDA 'Data Capture Control' tool, I set objects in-front of the camera and took pictures of each object for the recycled group at various angles/rotation.  Ten pictures were taken of each object at various rotations and angles, for a total of 100 Test images considered recyclable.  The number of total Test images was subjective, but various angles were taken to determine later if one position rendered a different classification than another.  Images were stored in the directory mentioned in the 'DATA' section.  The image file, 'Group_Recycle_Test_Images.JPG' on Github shows all of the objects selected [2]

   - Next, a new directory was created (/home/learner/Documents/Hello/Images_Input) and all 200 of the Test Images were copied to this directory.  The 'Images_Input' folder was the staging directory for a batch process job to grab each of the images and process them through a DNN.  The DNN selected to process the Test Images was the 'resnet-18' network, which was one of the existing DNNs downloaded from the NVIDIA Github site.  The 'resnet-18' network was selected out of the many existing networks, because it is the default network used by the 'imagenet-console.py' script, which was used to model the creation of a new python script to perform the batch processing job

   - A python script called 'demo.py' was created in the 'Images_Input' folder to perform a batch process job on all of the Test Images and do three things:
        1 - Look for image files (.jpg) in the staging directory ('Images_Input') 
        2 - Copy image files (.jpg) from the staging directory to the output directory (/home/learner/Documents/Hello/Images_Output) and rename each image to 'output_<existing filename>.jpg'.  
        3 - Process each 'output_' file through the existing DNN ('resnet-18') and stamp the image with the name of what it thinks it is, along with percent certainty

        NOTE:  While the 'demo.py' file can also identify .jpeg, .img, and .png files, only .jpg files work.  Older iterations of the 'demo.py' file can be found in the following directory:  /home/learner/Documents/Hello/Images_Input/Old_Python_Script_Versions

      - A Terminal window was then opened to the same location as the 'demo.py' script, and in the command line, entered, 'python3 demo.py'.  When the 'demo.py' file was executed, all 200 staged Test images were then processed, examined, and then logged into an Excel spreadsheet for analysis, 'Analysis_Resnet18_8_15_2019.xlsx'

      NOTE:  Processing all 200 Test images took approximately 3 minutes. Since a project requirement was to have a processing time of under 2 minutes, only 100 Test images (50% of the 'recyclable' category and 50% of the 'non-recyclable' category) are currently found in the image input staging directory ('Images_Input').  Processing 100 of the Test images takes approximately 1 minute and 30 seconds



ANALYSIS OF RESULTS:  

There were various questions that could be asked of the data, and lots of different ways to look at the results of the processed images.  The two questions I asked of the data were:

   1)  Did images with higher certainty percentages result in a higher percentage of correct identifications, than those images with lower certainty percentages? --- The question here is to see that when the model was very certain about the answer, did that lead to a higher percentage of correctly identified images, then when the model was uncertain of the answer. 

   2)  Did 'straight on upright' pictures of objects result in a higher percentage of correct identifications, than images taken at different angles? --- The thought is that most DNNs are trained with images that are straight on and upright of an object, and would likely yield a higher percentage of correct identifications, than images taken at different angles


   - In the 'Analysis_Resnet18_8_15_2019.xlsx' spreadsheet file, new columns were made to answer these two questions:

        'Model Label Correct' - Value of 'Not Correct' means the 'Model Label' did not match the actual object, a value of 'Correct' means it did
	
        '10% or Less' - Calculated column based on a value of the 'Percentage' column at 10% or less.  The 'Percentage' value is the percent of certainty applied by the model

        '25% or Less' - Calculated column based on a value of the 'Percentage' column at 25% or less.  The 'Percentage' value is the percent of certainty applied by the model

        '75% or Greater' - Calculated column based on a value of the 'Percentage' column at 75% or greater.  The 'Percentage' value is the percent of certainty applied by the model

        '90% or Greater' - Calculated column based on a value of the 'Percentage' column at 90% or greater.  The 'Percentage' value is the percent of certainty applied by the model


Based on these new data calculated data columns, some pivot tables were created in Excel.  Pivot tables on the 'Pivot_Table_High_Low' tab were used to answer the first question, and the tables on the 'Pivot_Table_Orientation' were used to answer the second question.

On the 'Pivot_Table_High_Low' tab, the data of interest was the 'Yes' column (those rows that meet the 'Percentage' threshold), and examining the number of times the model was 'Correct' and 'Not Correct'.  For these tables, a percentage was calculated which is the number of 'Correct' rows over the total of rows that meet the percentage threshold. The four resulting percentages show a trend that when the model had a higher percentage of certainty (the 'Percent' value was higher), there was a higher percentage of objects identified correctly, especially when comparing those with values of '10% or less' to those of '90% or greater'.  It was surprising that the '25% or less' category had a slightly lower percentage than the '10% or less' category.  It should also be noted that of all four categories, the '90% or greater' category had the least number of images with a 'Percentage' greater than 90%, at only eight instances.

On the 'Pivot_Table_Orientation' tab, all images are organized by their picture orientation, and whether the image was correctly identified by the model ('Correct') or incorrectly identified by the model ('Not Correct').  Then for each image orientation category, the number of 'Correct' images is divided by the total for the image orientation category to create a percentage.  It was expected that the 'Straight on upright' category would have the highest percentage of correctly identified images, but instead placed third.  The 'Straight on sideways' category had the highest percentage of '40.91%' which was very unexpected.  It should also be noted that the 'Straight on upright' orientation had almost three times as many images as the 'Straight on sideways' category.  It should also be considered that when the pictures were taken, not each image could have been taken at the same angle, that the angles of an object can be the same at different rotations (like a pint glass), and that when the pictures were taken a fair balance was not made to ensure that there were the same number of images for each image orientation category.



CONCLUSION:  

The results from this experiment indicate that a higher certainty percentage determined by the 'resnet-18' network could lead to higher percentages of images correctly identified.  However, more images and other 'Percentage' categories should be examined, instead of just the data extremes (low end and high end of percentages).  Also, other DNN networks should be examined, along with different objects to see if this trend is the same.

To me, there isn't enough data collected to make a judgement on the second question.  A fair and balanced number of images across all different orientation categories should be made, along with various objects and different DNNs.  There wasn't sufficient data to fairly compare each of the image orientation categories to each other.  

Based on this simple experiment, one cannot make any sweeping generalizations about Artificial Intelligence, or even this specific DNN (resnet-18).  The results from these two looks of the data are interesting, and more data collection with further scientific analysis is needed to comment on trends or patterns, or to see if what was discovered is similar to other networks, or how the image orientation plays a role in identification by the DNN.



IMPROVEMENTS / IDEAS FOR ADDITIONAL PROJECTS:

During this process, I also collected 'Recyclable' and 'Non-Recyclable' images for Validation and Training (\home\learner\Documents\datasets_objects\nonrecycle_recycle), and 'retrained' the resnet-18 network to create a new model (\home\learner\Documents\datasets_objects\nonrecycle_recycle\resnet18.onnx).  A group pictures of objects for Validation and Training can be seen in the images on Github ('Group_NonRecycle_Training_Validation.JPG' and 'Group_Recycle_Training_Validation.JPG').  Given more time, it would be interesting to run the 200 Test Images that were collected against the retrained model, and determine if the model correctly identifies an object as 'Recyclable' or 'Non-Recyclable'.  The idea is that this could be the first step to a larger project or tool, where a person could take a picture of an object in their house, indicate the municipality that they live in, and then have the image compared to a master database, and be informed if the object can be recycled in their municipality



REFERENCES:

   [1] - NVIDIA Jetson-Hello AI World - Building the Project from Source - https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md

   [2] - NVIDIA Jetson-Hello AI World - Collecting your own Datasets - https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-collect.md

