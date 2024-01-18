# importing the ilovepdf api
from pylovepdf.ilovepdf import ILovePdf
 
# public key
public_key = 'project_public_82ae2556e1edbf900d02672de7ce84db_HN0eOab3878b3fbe9e6e317463dc647b63254'
 
# creating a ILovePdf object
ilovepdf = ILovePdf(public_key, verify_ssl=True)
 
# assigning a new compress task
task = ilovepdf.new_task('compress')
 
# adding the pdf file to the task
task.add_file('new_resume.pdf')
 
# setting the output folder directory
# if no folder exist it will create one
task.set_output_folder('output_folder')
 
# execute the task
task.execute()
 
# download the task
task.download()
 
# delete the task
task.delete_current_task()