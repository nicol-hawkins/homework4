def main():
    for page in pages:
        file_name = page["filename"]
        output = page["output"]
        title = page["title"]

        # read in the content which
        # is located is now stored in file_name
        content = open(file_name).read()
        template = page_builder(content, title)
        
        # write page by opening the output(docs)
        # by accessing it within the dictionary.
        # write it to template cause templates
        # contains the function page_builder,
        # which actually constructs the pages.
        open(page["output"], "w+").write(template)
       

# This function constructs are webpage by replacing
# empty braces with actual content and titles within
# the newly constructed base template.
def page_builder(content, title):
    template = open("templates/base.html").read()
    template_plus_content = template.replace("{{content}}", content)
    finished_page = template_plus_content.replace("{{title}}", title)
    return finished_page


pages = [
{
    "filename": "content/about.html",
    "output": "docs/about.html",
    "title": "About Me",
},
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "My Blog",
},
    {
    "filename": "content/resume.html",
    "output": "docs/resume.html",
    "title": "My Resume",
},
]
   
if __name__ == "__main__":
    main()





