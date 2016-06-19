# rhythmbox-plugins-edit-file

See [installation instructions](edit-file/README.md).

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

Move the README file to README.md before altering it.

    git mv README README.md
    
Edit the edit-file/README.md to simplify instructions.

Get a copy of a correctly formatted plugin file:

    curl https://raw.githubusercontent.com/bgoodr/rhythmbox-plugins-sample-plugin/master/sample-python/sample-python.plugin > edit-file.plugin

And update it for content.

Change the code to use print and not the logging package, as otherwise -D option shows no output.

Test it out:

    ./install.sh; rhythmbox -D edit-file

At this point, it does exactly what the https://github.com/donaghhorgan/rhythmbox-plugins-open-containing-folder does which is open the folder.

Change the edit-file.py file to execute the file with audacity.
