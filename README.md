![Logo](imgs-readme/logo.png)
<hr>

# Megalodon
Megalodon is an extensive library of all-that-is-to-sharks. It contains various shark datasets, a model zoo and pre-trained networks for various tasks.

# Shark Species Analysis
The dataset is highly imbalanced due to some lesser known species of sharks. It is dependent on the images available on Google. For the sake of sample, some images are available in the repository. All the images are not published and will not be published. However, the numpy files and the code would be available for use-cases.
The frequency distribution of different species is shown in the graph.

<img src="imgs-readme/dist.png" width="600" height="400"/>

# Finegrained Images
Although spotting differences between various sharks is pretty easy given their distinct features: Hammerhead Shark vs White Shark. Similarly, it is relatively easy to spot differences between Nurse Shark and White or Tiger Shark. However it is not so easy to spot differences between White Shark and Tiger Shark. This is because of striking similarity between the two types (shown in sample images below). It would be interesting to explore the classification results on such a dataset. 

<table style="width:100%">
  <tr>
    <th>Nurse Shark</th>
    <th>White Shark</th>
    <th>Tiger Shark</th>
  </tr>
  <tr>
    <td><img src="Finegrained-Images/data/Nurse Shark/4.jpg" width="200" height="200" /></td>
     <td><img src="Finegrained-Images/data/White Shark/19.jpg" width="200" height="200" /></td>
    <td><img src="Finegrained-Images/data/Tiger Shark/21.jpg" width="200" height="200"/></td>
  </tr>
</table>

</body>
</html>

# Shark Calls

# Data
The entire dataset is available in the ```Extensive-Data``` folder. It has a single .csv file ```dataset.csv```. The .csv file is described below.

<table style="width:100%">
  <tr>
    <th>Column Name</th>
    <th>Row Data</th>
  </tr>
  
  <tr>
    <td>Shark Specie</td>
    <td>String: the name of shark</td>
  </tr>

  <tr>
    <td>Image</td>
    <td>URL: the link to the image</td>
  </tr>

  <tr>
    <td>Shark Call</td>
    <td>URL: the link to the shark call</td>
  </tr>
  
  <tr>
    <td>Textual Description</td>
    <td>String: the description of the shark specie.</td>
  </tr>
</table>