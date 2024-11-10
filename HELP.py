import os

# Specify the folder path
folder_path = 'images/poonch'  # Replace with your folder path

# List of supported image file extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

# Create a list to store image filenames
image_files = []

# Loop through all files in the directory
for filename in os.listdir(folder_path):
    # Check if the file is an image by checking its extension
    if filename.lower().endswith(image_extensions):
        # Append the full path of the image file
        image_files.append(filename)

# Open a file to write the HTML output
with open('image_list.html', 'w') as file:
    # Write the list of image filenames as HTML
    for image in image_files:
        file.write(f'''
  <li class="col-xs-6 col-sm-4 col-md-3" data-responsive='images/poonch/{image}' data-src='images/poonch/{image}'
                        data-sub-html='<b>Place: </b>poonch
'><a href="">
                            <img class="img-responsive img-thumbnail" style="padding: 1px" src='images/poonch/{image}' height="150px" width="360px" />
                           </a>
                        <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">poonch</h5>

                        <div style="height: 20px"></div>
                    </li>

''')

print("HTML list of images has been saved to 'image_list.html'")
