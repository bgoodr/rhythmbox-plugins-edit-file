# rhythmbox-plugins-edit-file
Rhythmbox edit file plugin

# How this plugin was created

Download rb-edit-file_0.2.zip from http://www.martinvogel.de/blog/index.php?/archives/57-Rhythmbox-Plugin-edit-file-zum-Bearbeiten-von-MP3-und-OGG-Dateien.html

Extract it and check in the original source. zip file is http://www.martinvogel.de/blog/uploads/ZIP-Archive/rb-edit-file_0.2.zip

Do some renaming to be compatible with what I see in other plugins:

    git mv rb-edit-file edit-file
    git mv rb-edit-file.py edit-file.py
    git mv rb-edit-file.rb-plugin edit-file.plugin

Add the install.sh file:

    cd edit-file
    curl https://raw.githubusercontent.com/bgoodr/rhythmbox-plugins-sample-plugin/master/sample-python/install.sh > install.sh
    chmod a+x install.sh

The edit-file.py looks like it is completely busted and not working at
all in Rhythmbox 3.3, so replace it with the code in
donaghhorgan/rhythmbox-plugins-open-containing-folder and change it to
call audacity instead of opening the directory. 

    curl https://raw.githubusercontent.com/donaghhorgan/rhythmbox-plugins-open-containing-folder/master/OpenContainingFolder.py > edit-file.py

Search and replace all references to opening folders with editing files inside the .py file.



