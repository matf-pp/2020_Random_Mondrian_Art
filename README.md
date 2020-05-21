# 2020_Random_Mondrian_Art
# Random Mondrian Art

This project uses recursion to generate pseudo‐random art in a [Mondrian style](https://en.wikipedia.org/wiki/Piet_Mondrian).  Your program’s output will be an HTML document that contains rectangle primitives (perhaps among others) within an SVG tag. 

The main strategy for recursion is:
* If the region is wider than half the initial canvas size and the region is taller than half the initial canvas 
height: 
 * Use recursion to split the region into 4 smaller regions (a vertical split and a horizontal split) with 
the split location is chosen randomly 
* Else: if the region is wider than half the initial canvas size: 
Use recursion to split the region into 2 smaller regions using a vertical line with the split location chosen randomly 
* Else: if the region is taller than half the initial canvas size:
Use recursion to split the region into 2 smaller regions using a horizontal line with the split 
location is chosen randomly 
* Else: if the region is big enough to split both horizontally and vertically, and both a horizontal and vertical 
split is randomly selected: 
Use recursion to split the region into 4 smaller regions (a vertical split and a horizontal split) with the split location is chosen randomly 
* Else: if the region is big enough to split horizontally, and a horizontal split is selected: 
Use recursion to split the region into 2 smaller regions using a vertical line with the split location chosen randomly 
* Else: if the region is big enough to split vertically, a vertical split is selected: 
Use recursion to split the region into 2 smaller regions using a horizontal line with the split location is chosen randomly 
* Else:fill the current region (randomly, either white or colored, and if colored, with a random 
determination of picked color, with a pattern or not). 

## Language

The project is written in [Python 3.8.2](https://www.python.org/) and packages which are used:
* [Numpy](https://numpy.org/) for randomization
* [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/) for GUI

## Dependencies

###### To install NumPy and PyQt5:

```bash
pip install numpy PyQt5
```
## Launching
### Windows :
   Execute file <br/>
    ![icon][ic] randomMondrianArt.exe
  
  
 ### Linux:
   ```bash
cd  2020_Random_Mondrian_Art-master
python3 gui.py
```

## Examples

#### Example withouth patterns:
![example_1][ex1]
#### Example with patterns:
![example_2][ex2]


[ex1]: https://raw.githubusercontent.com/matf-pp/2020_Random_Mondrian_Art/65e3799881a65aab6b9fbf420ce5465f0af07295/example_1.svg
[ex2]: https://raw.githubusercontent.com/matf-pp/2020_Random_Mondrian_Art/65e3799881a65aab6b9fbf420ce5465f0af07295/example_2.svg
[ic]:https://raw.githubusercontent.com/matf-pp/2020_Random_Mondrian_Art/master/icon.png

## Authors and acknowledgment
This project is a university assignment from the subject [Programming Paradigms](http://www.programskijezici.matf.bg.ac.rs/ProgramskeParadigmeR.html)
* Profesor: [doc dr Milena Vujošević Janičić](http://poincare.matf.bg.ac.rs/~milena/)
* Assistant: [Marjana Šolajić](http://poincare.matf.bg.ac.rs/~marjana/)

Students authors of the project:
* Ana Milićević (mr16042@alas.matf.bg.ac.rs)
* Miloš Kutlešić (mr16182@alas.matf.bg.ac.rs)
* Uroš Dimitrijević (mr16193@alas.matf.bg.ac.rs)
