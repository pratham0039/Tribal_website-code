import os

folder_path = 'images/reasi/TRIBAL HOUSEHOLD'  # Replace with the actual path to your folder

# Check if the folder exists
if os.path.exists(folder_path):
    # Get a list of all files in the folder
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Print the file names
    for file_name in file_names:
        print(f''' 
                                                              <li class="col-xs-6 col-sm-4 col-md-3" data-responsive='images/reasi/TRIBAL HOUSEHOLD/{file_name}' data-src='images/reasi/TRIBAL HOUSEHOLD/{file_name}'
                        data-sub-html='<b>Place: </b>Reasi
'><a href="">
                            <img class="img-responsive img-thumbnail" style="padding: 1px" src='images/reasi/TRIBAL HOUSEHOLD/{file_name}' height="150px" width="360px" />
                           </a>
                        <h5 class="img-responsive" style="display: ruby-text-group; font-size: .70em; width: 80%; height: 15px; margin-top: 0.85em; margin-bottom: .67em; color: white; margin-left: 0; margin-right: 0;">Reasi</h5>
                        
                        <div style="height: 20px"></div>
                    </li>
              
              
              
              
              ''')