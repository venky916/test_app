from ilove import ILovePdf
PUBLIC_KEY="project_public_82ae2556e1edbf900d02672de7ce84db_HN0eOab3878b3fbe9e6e317463dc647b63254"
def test_compress():
    i = ILovePdf(PUBLIC_KEY)
    i.new_task("compress")
    i.add_file("sample.pdf")
    i.execute()
    i.download("out.pdf")

def test_merge():
    i = ILovePdf(PUBLIC_KEY)
    i.new_task("merge")
    for _ in range(3):
        i.add_file("sample.pdf")
    i.execute()
    i.download("out.pdf")
    
def test_imagepdf():
    i = ILovePdf(PUBLIC_KEY)
    i.new_task("imagepdf")
    i.add_file("test.jpg")
    i.execute()
    i.download()

test_compress()