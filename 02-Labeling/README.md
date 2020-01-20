# LABELING 

At first I used labelimg for taguera the images. This program is still a valid option. More in [LabelImg Github Project Page](https://github.com/tzutalin/labelImg)

![LabelImg](/02-Labeling/images/demo3.jpg)

### Download VoTT
Now I started use VoTT [releases](https://github.com/Microsoft/VoTT/releases) You can download and install the version for your operating system. Under `Assets` select the package for your operating system: 
- `vott-2.x.x-darwin.dmg` for Mac users, 
- `vott-2.x.x-win32.exe` for Windows users and 
- `vott-2.x.x-linux.snap` for Linux users.

Installing `*.snap` files requires the snapd package manager which is available at [snapcraft.io](https://snapcraft.io/docs/installing-snapd).

### Create a New Project

Create a **New Project** and call it `Annotations`. It is highly recommended to use `Annotations` as your project name. If you like to use a different name for your project, you will have to modify the command line arguments of subsequent scripts accordingly. 

Under **Source Connection** choose **Add Connection** and put `Images` as **Display Name**. Under **Provider** choose **Local File System** and select [`CarPartsDetectionChallenge/Data/Source Images/Training_Images`](/Data/Images/Training_Images) and then **Save Connection**. For **Target Connection** choose the same folder as for **Source Connection**. Hit **Save Project** to finish project creation. 

![New Project](/02-Labeling/images//New_Project.gif)

### Export Settings
Navigate to **Export Settings** in the sidebar and then change the **Provider** to `Comma Separated Values (CSV)`, then hit **Save Export Settings**. 

![New Project](/02-Labeling/images/Export_Settings.gif)


### Labeling
First create a new tag on the right and give it a relevant tag name. In our example, we choose `Cat_Face`. Then draw bounding boxes around your objects. You can use the number key **1** to quickly assign the first tag to the current bounding box. 

![New Project](/02-Labeling/images/Labeling.gif)

### Export Results
Once you have labeled enough images press **CRTL+E** to export the project. You should now see a folder called [`vott-csv-export`](/Data/Images/Training_Images/vott-csv-export) in the [`Training_Images`](/Data/Images/Training_Images) directory. Within that folder, you should see a `*.csv` file called [`Annotations-export.csv`](/Data/Images/Training_Images/vott-csv-export/Annotations-export.csv) which contains file names and bounding box coordinates. 

## Convert to YOLO Format
As a final step, convert the VoTT csv format to the YOLOv3 format. To do so, run the conversion script from within the [`CarPartsDetectionChallenge/1_Image_Annotation`](/1_Image_Annotation/) folder: