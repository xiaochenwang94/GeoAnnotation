# GeoAnnotation
This project name as GeoAnntation which is a implementation of anntation algorithm.
It's reproducing the KDE(Kernel Density Estimation) algorithm on the paper

[Semantic Annotation of Mobility Data using Social Media](http://dl.acm.org/citation.cfm?id=2741675) by Fei Wu.

#### Prerequisites
python3
flask (version==0.10)
numpy
pandas

#### The architecture of this project
The following list show the files in this project.
* Annotation.py implementation of KDE(Kernel Density Estimation) algorithm.
* view.py use flask architecture to show the result in browser.

directories:
* data/ 
* templates/
* static/

#### How to Run the Experiments:
		git clone https://github.com/xiaochenwang94/GeoAnnotation
		cd GeoAnntation
		python view.py

		right click the point you want to annotate.
		wait 5~15 seconds

#### Presentation of current result
I'm still working on making this project more powerful. So, here is the presentation of current result.

This sample anntates STAPLES Center at 2016-04-14. The result shows that kobe take 60 scores and Kobe
Bryant was retired at that day. 
![image](https://github.com/xiaochenwang94/GeoAnnotation/blob/master/img/annotation.png)

#### Programming Style
I use basic OOP(Object Oriented Programming) tricks to build my program. Something like... I put all about
``KDE`` into a class(Anntation) which you can find in file ``Anntation.py``.

#### References
[Semantic Annotation of Mobility Data using Social Media](http://dl.acm.org/citation.cfm?id=2741675) by Fei Wu, Zhenhui Li ,Wang-Chien Lee ,Hongjian Wang ,Zhuojie Huang.















