# CV2_template_matching

Simple script to find a template item in a given image.
While implementation is easy and training is not needed, the image finder just return the "max_result" of a correlation score, hence it's very easy it returns false positive if items have different scale or different rotation.

In the example i provided with this script, even a little movement of Blanka made the script fail, even worse, it recognize the item in ken!

This script was made starting from the input of the terrific blog https://www.pyimagesearch.com/

![image](https://user-images.githubusercontent.com/57464184/115237741-32014680-a11d-11eb-8c10-968fdbd99a5d.png)
